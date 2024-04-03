import os
import pandas as pd
import json

from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI()
from Analysis.misc.text_extraction import create_dialogue_segments

def process_file(segment, output_path, model_name='gpt-3.5-turbo-0125'):

    # prompt = f"""
    # Assume you are an expert in dialogue analysis. You are presented with a series of conversations between a bot and a user. Your primary task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
    # Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

    # Analyze each bot utterance and determine whether there is a dialogue breakdown or non-breakdown. Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 

    # Include your decision as either "decision: [BREAKDOWN]" or "decision: [NON-BREAKDOWN]".

    # Here is the conversation segment for analysis:
    # "{segment}"

    # Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

    #     "reasoning": "Your explanation here",
    #     "decision": "BREAKDOWN/NON-BREAKDOWN",
    #     "score": Your score here

    # Ensure each object is separated by a comma and the list ends with a closing square bracket. 

    # """

    prompt = f"""
    # Instructions:
    You are presented with a series of utterances between a bot and a user. Recall three relevant examples, then scrutinize the latest bot utterance for potential dialogue breakdown.
    Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

    #Analysis:
    Here is the conversation segment for analysis:
    {segment}

    ## Relevant Examples:
    Recall three examples of dialogue interactions relevant to the conversation segments provided. Your examples should demonstrate varying degrees of dialogue coherence and relevance. For each example:
    - After "Example: ", describe the interaction 
    - After "Analysis: ", explain the coherence or breakdown in the conversation and give a score with justification.

    ## Answer the initial conversation segment:
    
    Analyze the latest bot utterance and determine whether there is a dialogue breakdown or non-breakdown. Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 
    Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN".

    Please output your response in JSON format as a list of objects. For the examples, place them in the 'examples' field, each separated by a comma. For the bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

            "examples": "Put each example and analysis separated by a comma here",
            "reasoning": "Your explanation here",
            "decision": "BREAKDOWN" or "NON-BREAKDOWN",
            "score": Your score here

        Ensure each object is separated by a comma and the list ends with a closing square bracket.
    """

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "system", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"},
        seed=0 
    )

    return response.choices[0].message.content

file_path = 'db/eval_unlabelled/Bot001_007.log.txt'
dialogue_segments, bot_responses = create_dialogue_segments(file_path)

df = pd.DataFrame(columns=['segment', 'examples','reasoning', 'decision', 'score']) #modify this for analogical reasoning

output_path = 'db/test/anal2.csv'

for segment, bot_response in zip(dialogue_segments, bot_responses):
    response_json = process_file(segment, output_path) # model_name='gpt-4-turbo-preview'
    print(bot_response)
    print(response_json)
    response_data = json.loads(response_json)
    new_row = pd.DataFrame([{
        'segment': bot_response,
        'examples': response_data.get('examples', ''),
        'reasoning': response_data.get('reasoning', ''),
        'decision': response_data.get('decision', ''),
        'score': response_data.get('score', '')
    }])

    df = pd.concat([df, new_row], ignore_index=True)

df.to_csv(output_path, index=False)

