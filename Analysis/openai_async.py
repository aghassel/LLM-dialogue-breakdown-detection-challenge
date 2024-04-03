import os
import glob
import json
import asyncio
import pandas as pd
import argparse
import logging
import openai
from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta

from Analysis.misc.text_extraction import create_dialogue_segments
from Analysis.misc.prompts import zero_shot, CoT, one_shot, two_shot, two_shot_CoT, four_shot, four_shot_CoT, analog_reason

load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

openai.api_key = os.getenv('OPENAI_API_KEY')
client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MODEL_NAMES = {
    'gpt3': 'gpt-3.5-turbo-0125',
    'gpt4': 'gpt-4-0125-preview',
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
    elif prompt_type == 'analog_reason':
        return analog_reason(segment)
    else:
        raise ValueError(f"Unknown prompt type: {prompt_type}")

async def process_file_async(client, segment, model_name, prompt_type, retries=3, backoff=60):
    attempt = 0 
    while attempt < retries:
        try:
            prompt = select_prompt(prompt_type, segment)
            
            response = await client.chat.completions.create(
                messages=[{"role": "system", "content": prompt}],
                model=model_name,
                temperature=0,
                response_format={"type": "json_object"},
                seed=0 
            )
            return response.choices[0].message.content
        
        except openai.RateLimitError as e:
            logging.error(f"Error in process_file_async: {str(e)}")
            wait = backoff * (2 ** attempt)
            logging.info(f"Rate limit hit. Retrying after {wait} seconds. Attempts left: {retries - attempt - 1}")
            await asyncio.sleep(wait)
            attempt += 1 
        
        except Exception as e:
            logging.error(f"Unhandled exception in process_file_async: {str(e)}")
            raise

    logging.error("Maximum retries reached. Failing...")
    raise Exception("Failed to process file after multiple retries.")

async def analyze_file(semaphore, client, file_path, output_folder, model_name, prompt_type):
    async with semaphore:
        dialogue_segments, bot_responses = create_dialogue_segments(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_csv_path = os.path.join(output_folder, f"{base_name}.csv")
        df = pd.DataFrame(columns=['segment', 'reasoning', 'decision', 'score']) #modify this for analogical reasoning

        for segment, bot_response in zip(dialogue_segments, bot_responses):
            try:
                response_json = await process_file_async(client, segment, model_name, prompt_type)
                response_data = json.loads(response_json)
                bot_response = bot_response.replace('"', "'").replace('\n', ' ').replace(',', ';')
                new_row = pd.DataFrame([{
                    'segment': bot_response,
                    #'examples': response_data.get('examples', ''),  # 'examples': 'Put each example and analysis separated by a comma here
                    'reasoning': response_data.get('reasoning', ''),
                    'decision': response_data.get('decision', ''),
                    'score': response_data.get('score', '')
                }])
                df = pd.concat([df, new_row], ignore_index=True)
            except Exception as e:
                logging.error(f"Error processing segment {segment}: {str(e)}")
        df.to_csv(output_csv_path, index=False)

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, choices=MODEL_NAMES.keys(), required=True, help='Model name')
    parser.add_argument('--prompt_type', type=str, required=True, choices=['CoT', 'zero_shot', 'one_shot', 'two_shot', 'two_shot_CoT', 'four_shot', 'four_shot_CoT', 'analog_reason'], help='Type of prompt')
    parser.add_argument('--input_folder', type=str, default='db/eval_unlabelled/', help='Input folder containing text files')
    args = parser.parse_args()

    full_model_name = MODEL_NAMES[args.model_name]
    output_folder = f"results/{args.prompt_type}/{args.model_name}"
    os.makedirs(output_folder, exist_ok=True)

    client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    file_paths = glob.glob(f"{args.input_folder}/*.txt")
    semaphore = asyncio.Semaphore(50)  # limit number of files processed concurrently
    await asyncio.gather(*[analyze_file(semaphore, client, file_path, output_folder, full_model_name, args.prompt_type) for file_path in file_paths])

if __name__ == "__main__":
    asyncio.run(main())
