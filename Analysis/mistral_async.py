import os
import glob
import json
import asyncio
import pandas as pd
import argparse
import logging
from dotenv import load_dotenv, find_dotenv
from mistralai.async_client import MistralAsyncClient
from mistralai.models.chat_completion import ChatMessage
from aiolimiter import AsyncLimiter
import re

from Analysis.misc.text_extraction import create_dialogue_segments
from Analysis.misc.prompts import zero_shot, CoT, one_shot, two_shot, two_shot_CoT, four_shot, four_shot_CoT

load_dotenv(find_dotenv())
MISTRAL_API_KEY = os.environ.get('MISTRAL_API_KEY')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

limiter = AsyncLimiter(5, 1)  # 5 requests per second

MODEL_NAMES = {
    'medium': 'mistral-medium',
}

def select_prompt(prompt_type, segment):
    if prompt_type == 'CoT':
        return CoT(segment=segment)
    elif prompt_type == 'zero_shot':
        return zero_shot(segment=segment)
    elif prompt_type == 'one_shot':
        return one_shot(segment=segment)
    elif prompt_type == 'two_shot':
        return two_shot(segment)
    elif prompt_type == 'two_shot_CoT':
        return two_shot_CoT(segment)
    elif prompt_type == 'four_shot':
        return four_shot(segment)
    elif prompt_type == 'four_shot_CoT':
        return four_shot_CoT(segment)
    else:
        raise ValueError(f"Unknown prompt type: {prompt_type}")

async def process_file_async(client, limiter, segment, model_name, prompt_type, retries=3, backoff=60):
    attempt = 0
    while attempt < retries:
        try:
            async with limiter:
                prompt = select_prompt(prompt_type, segment)
                response = await client.chat(
                    model=model_name,
                    messages=[ChatMessage(role="user", content=prompt)],
                )
                return response.choices[0].message.content
            
        except Exception as e:
            logging.error(f"Error in process_file_async: {str(e)}")
            wait = backoff * (2 ** attempt)
            logging.info(f"Retrying after {wait} seconds. Attempts left: {retries - attempt - 1}")
            await asyncio.sleep(wait)
            attempt += 1

    logging.error("Maximum retries reached. Failing...")
    raise Exception("Failed to process file after multiple retries.")

async def analyze_file(semaphore, client, limiter, file_path, output_folder, model_name, prompt_type):
    async with semaphore:
        dialogue_segments, bot_responses = create_dialogue_segments(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_csv_path = os.path.join(output_folder, f"{base_name}.csv")
        df = pd.DataFrame(columns=['segment', 'reasoning', 'decision', 'score'])

        for segment_index, (segment, bot_response) in enumerate(zip(dialogue_segments, bot_responses)):
            retry_count = 0
            while retry_count < 5:
                try:
                    bot_response = bot_response.replace('"', "'").replace('\n', ' ').replace(',', ';')
                    response_json = await process_file_async(client, limiter, segment, model_name, prompt_type)
                    response_data = json.loads(response_json)
                    reasoning = response_data[0].get('reasoning', '')
                    decision = response_data[0].get('decision', 'UNKNOWN')
                    score = response_data[0].get('score', 0)
                    new_row = pd.DataFrame([{
                        'segment': bot_response,
                        'reasoning': reasoning,
                        'decision': decision,
                        'score': score
                    }])
                    df = pd.concat([df, new_row], ignore_index=True)
                    break
                except Exception as e:
                    logging.error(f"Error processing segment {segment_index} in {base_name}: {str(e)} - Retry {retry_count+1}/5")
                    retry_count += 1
                    if retry_count >= 5:
                        logging.error(f"Failed to process {base_name} segment: {segment_index} after 5 retries.")
        
        df.to_csv(output_csv_path, index=False)

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, choices=MODEL_NAMES.keys(), required=True, help='Model name')
    parser.add_argument('--prompt_type', type=str, required=True, help='Type of prompt')
    parser.add_argument('--input_folder', type=str, default='db/eval_unlabelled/', help='Input folder containing text files')
    args = parser.parse_args()

    full_model_name = MODEL_NAMES[args.model_name]
    output_folder = f"results/{args.prompt_type}/{args.model_name}"
    os.makedirs(output_folder, exist_ok=True)

    all_file_paths = glob.glob(f"{args.input_folder}/*.txt")
    file_paths = [path for path in all_file_paths]
    print(f"Processing {len(file_paths)} files")

    client = MistralAsyncClient(api_key=MISTRAL_API_KEY)
    semaphore = asyncio.Semaphore(10)

    await asyncio.gather(*[
        analyze_file(semaphore, client, limiter, file_path, output_folder, full_model_name, args.prompt_type)
        for file_path in file_paths
    ])

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
