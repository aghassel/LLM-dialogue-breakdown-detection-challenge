import os
import pandas as pd
import json

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

load_dotenv(find_dotenv())
MISTRAL_API_KEY = os.environ.get('MISTRAL_API_KEY')

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-medium"
client = MistralClient(api_key=api_key)

from Analysis.misc.text_extraction import create_dialogue_segments
from Analysis.misc.prompts import zero_shot, CoT, one_shot, two_shot, two_shot_CoT, four_shot, four_shot_CoT

def process_file(segment, output_path, model_name='gpt-3.5-turbo-1106'):

    prompt = f"""
    Assume you are an expert in dialogue analysis. You are presented with a series of conversations between a bot and a user. Your primary task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
    Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

    Analyze each bot utterance and determine whether there is a dialogue breakdown or non-breakdown. Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 

    Include your decision as either "decision: [BREAKDOWN]" or "decision: [NON-BREAKDOWN]".

    Here is the conversation segment for analysis:
    "{segment}"

    Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

        "reasoning": "Your explanation here",
        "decision": "BREAKDOWN/NON-BREAKDOWN",
        "score": Your score here

    Ensure each object is separated by a comma and the list ends with a closing square bracket. 

    """

    response = client.chat(
        model=model,
         messages=[ChatMessage(role="user", content=prompt)],
    )

    return response.choices[0].message.content

file_path = 'db/eval_unlabelled/Bot001_007.log.txt'
dialogue_segments, bot_responses = create_dialogue_segments(file_path)

df = pd.DataFrame(columns=['segment', 'reasoning', 'decision', 'score'])

output_path = 'db/test/mistral.csv'

for segment, bot_response in zip(dialogue_segments, bot_responses):
    response_json = process_file(segment, output_path) 
    print(bot_response)
    print(response_json)
    response_data = json.loads(response_json)
    if isinstance(response_data, list) and len(response_data) > 0:
        first_response_item = response_data[0]
        reasoning = first_response_item.get('reasoning', '')
        decision = first_response_item.get('decision', 'UNKNOWN')
        score = first_response_item.get('score', 0)
    else:
        raise ValueError(f"Unexpected response type: {type(response_json)}")
    new_row = pd.DataFrame([{
        'segment': bot_response,
        'reasoning': reasoning,
        'decision': decision,
        'score': score
    }])

    df = pd.concat([df, new_row], ignore_index=True)

df.to_csv(output_path, index=False)

