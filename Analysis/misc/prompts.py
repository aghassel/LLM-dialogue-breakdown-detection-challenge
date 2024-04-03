def zero_shot(segment):
        return f"""
        Assume you are an expert in dialogue analysis. You are presented with a series of conversations between a bot and a user. Your primary task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
        Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

        Analyze the latest bot utterance and determine whether there is a dialogue breakdown or non-breakdown. Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 

        Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN".

        Here is the conversation segment for analysis:
        "{segment}"

        Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

            "reasoning": "Your explanation here",
            "decision": "BREAKDOWN" or "NON-BREAKDOWN",
            "score": Your score here

        Ensure each object is separated by a comma and the list ends with a closing square bracket. 

        """

# def one_shot(segment):
#         return f"""
#         Assume you are an expert in dialogue analysis. You are presented with a series of conversations between a bot and a user. Your primary task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
#         Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

#         Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 
#         Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN".

#         Here is an example:
#         ""
#         DIALOGUE
#         ----------
#         1. Bot: It's nice to go shopping alone.
#         2. User: I agree. That's nice.
#         3. Bot: Shopping takes time.
#         4. User: Window shopping is also fun.
#         ----------

#         Determine if the following bot utterance lead to a dialogue breakdown:
#         ----------
#         5. Bot: It's fun to go shopping with somebody.
#         ----------

#         "reasoning": "In this utterance, the bot is likely to be causing a dialogue breakdown because the latest bot utterance contradicts the first bot utterance.",
#         "decision": "BREAKDOWN",
#         'score": 0.1
#         ""

#         Here is the conversation segment for analysis:
#         "{segment}"

#         Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

#             "reasoning": "Your explanation here",
#             "decision": "BREAKDOWN" or "NON-BREAKDOWN",
#             "score": Your score here

#         Ensure each object is separated by a comma and the list ends with a closing square bracket.
#         """

def one_shot(segment):
        return f"""
        Assume you are an expert in dialogue analysis. You are presented with a series of conversations between a bot and a user. Your primary task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
        Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

        Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 
        Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN".

        Here is an example:
        "
        DIALOGUE
        ----------
        1. Bot: Hi! What is your name? [FACE WITH TEARS OF JOY] [SMILING FACE WITH HEART-SHAPED EYES]
        2. User: my name is george
        3. Bot: hello george my name is pink what are you doing ?
        4. User: what is yours?
        5. Bot: mine is 7 . spicy owche wawa how are you tonight ?
        6. User: fine thankS how are you pink?
        ----------

        Determine if the following bot utterance lead to a dialogue breakdown:
        ----------
        7. Bot: oh feeling good . my house is sparkling clean . love cleaning do you have any hobbies ?
        ----------

        Output: 
        "reasoning": "the bot responds to the user's question about how they are feeling, then naturally mentions one of their hobbies, and asks the user about their hobbies as well. This is coherent, and does not disrupt the flow of conversation, thus not an indication of dialogue breakdown."
        "decision": "NON-BREAKDOWN"
        "score": 0.9
        "

        Here is the conversation segment for analysis:
        "{segment}"

        Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

            "reasoning": "Your explanation here",
            "decision": "BREAKDOWN" or "NON-BREAKDOWN",
            "score": Your score here

        Ensure each object is separated by a comma and the list ends with a closing square bracket.
        """


# def CoT(segment):
#         return f"""
#             ## INSTRUCTIONS:
#             Assume you are an expert in dialogue analysis. You are presented with a series of conversations between a bot and a user. Your primary task is to investigate the latest bot utterance for potential dialogue breakdown. 
#             Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.
            
#             ### ANALYSIS:
#             To conduct your analysis, follow these steps:

#             1. **Identify Key Elements**: Examine the bot's last utterance and identify the key elements that are relevant to the conversation's flow. Consider the context, the user's previous message, and the bot's response.

#             2. **Evaluate Relevance**: Assess whether the bot's response is relevant to the user's previous message. Determine if the bot is staying on topic or if it has introduced unrelated information.

#             3. **Check for Coherence**: Analyze the bot's response for coherence. Ensure that the response logically follows from the user's previous message and that it contributes constructively to the conversation.

#             4. **Detect Disruptions**: Identify any disruptions in the conversation, such as non-sequiturs, abrupt topic changes, or responses that fail to acknowledge the user's input.

#             5. **Decision Making**: Based on your analysis, decide whether the bot's last utterance represents a dialogue breakdown or a non-breakdown. 

#             6. **Justification and Scoring**: Provide a brief justification for your decision, considering the elements you've identified and analyzed. Assign a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation.

#             Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN". Provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 

#             Here is the conversation segment for analysis:
#             "{segment}"

#             ### FORMATTING:
#             Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

#                 "reasoning": "Your final justification here",
#                 "decision": "BREAKDOWN" or "NON-BREAKDOWN",
#                 "score": Your score here

#             Ensure each object is separated by a comma and the list ends with a closing square bracket. 
#             """

  # and reflect on any relevant examples.
def CoT(segment):
        return f"""
            #INSTRUCTIONS:
            You are presented with a series of conversations between a bot and a user. Your task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
            Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

            Before answering, you should think through the question step-by-step. Explain your reasoning at each step towards making your final decision.
       
            Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN". 
            Provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 

            #ANALYSIS:
            Here is the conversation segment for analysis:
            "{segment}"

            #RESPONSE FORMAT:
            ## Please output your response in JSON format as a list of objects. Provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

                "reasoning": "Your step-by-step reasoning here",
                "decision": "BREAKDOWN" or "NON-BREAKDOWN",
                "score": Your score here

            Ensure each object is separated by a comma and the list ends with a closing square bracket. 
            """


# def two_shot(segment):
#         return f"""
#         Assume you are an expert in dialogue analysis. You are presented with a series of conversations between a bot and a user. Your primary task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
#         Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

#         Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 
#         Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN".

#         Here is the first example:
#         ""
#         DIALOGUE
#         ----------
#         1. Bot: Hi! What is your name? [FACE WITH TEARS OF JOY] [SMILING FACE WITH HEART-SHAPED EYES]
#         2. User: my name is george
#         3. Bot: hello george my name is pink what are you doing ?
#         4. User: what is yours?
#         5. Bot: mine is 7 . spicy owche wawa how are you tonight ?
#         6. User: fine thankS how are you pink?
#         ----------

#         Determine if the following bot utterance lead to a dialogue breakdown:
#         ----------
#         7. Bot: oh feeling good . my house is sparkling clean . love cleaning do you have any hobbies ?
#         ----------

#         Output: 
#         "reasoning": "the bot responds to the user's question about how they are feeling, then naturally mentions one of their hobbies, and asks the user about their hobbies as well. This is coherent, and does not disrupt the flow of conversation, thus not an indication of dialogue breakdown."
#         "decision": "NON-BREAKDOWN"
#         "score": 0.9
#         ""

#         Here is the second example:
#         ""
#         DIALOGUE
#         ----------
#         1. Bot: It's nice to go shopping alone.
#         2. User: I agree. That's nice.
#         3. Bot: Shopping takes time.
#         4. User: Window shopping is also fun.
#         ----------

#         Determine if the following bot utterance lead to a dialogue breakdown:
#         ----------
#         5. Bot: It's fun to go shopping with somebody.
#         ----------

#         "reasoning": "In this utterance, the bot is likely to be causing a dialogue breakdown because the latest bot utterance contradicts the first bot utterance.",
#         "decision": "BREAKDOWN",
#         'score": 0.1
#         ""

#         Here is the conversation segment for analysis:
#         "{segment}"

#         Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

#             "reasoning": "Your explanation here",
#             "decision": "BREAKDOWN" or "NON-BREAKDOWN",
#             "score": Your score here

#         Ensure each object is separated by a comma and the list ends with a closing square bracket.
#         """

def two_shot(segment):
    return f"""
    ### INSTRUCTIONS:
    You are presented with a series of conversations between a bot and a user. Your task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
    Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

    Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation.

    ### EXAMPLES:
    ***Example 1:***
    **Dialogue**:
    1. Bot: Hi! What is your name? [FACE WITH TEARS OF JOY] [SMILING FACE WITH HEART-SHAPED EYES]
    2. User: My name is George.
    3. Bot: Hello George, my name is Pink. What are you doing?
    4. User: What is yours?
    5. Bot: Mine is 7. Spicy owche wawa. How are you tonight?
    6. User: Fine thanks, how are you Pink?

    **Determine if the following bot utterance lead to a dialogue breakdown**:
    7. Bot: Oh, feeling good. My house is sparkling clean. Love cleaning. Do you have any hobbies?

    **Output**:
        - "reasoning": "The bot responds to the user's inquiry about its state and smoothly transitions into discussing one of its hobbies, which is coherent and maintains the conversation's flow. Thus, it does not constitute a dialogue breakdown."
        - "decision": "NON-BREAKDOWN"
        - "score": 0.9

    ***Example 2:***
    **Dialogue**:
    1. Bot: It's nice to go shopping alone.
    2. User: I agree. That's nice.
    3. Bot: Shopping takes time.
    4. User: Window shopping is also fun.

    **Determine if the following bot utterance lead to a dialogue breakdown**:
    5. Bot: It's fun to go shopping with somebody.

    **Output**:
        - "reasoning": "The bot's latest response about shopping with somebody contradicts the bot's initial statement regarding its enjoyment of shopping alone. Thus, this contradiction causes a dialogue breakdown."
        - "decision": "BREAKDOWN"
        - "score": 0.1

    ### ANALYSIS:
    Here is the conversation segment for analysis:
    {segment}

    ## Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

        "reasoning": "Your explanation here",
        "decision": "BREAKDOWN" or "NON-BREAKDOWN",
        "score": Your score here

    Ensure each object is separated by a comma and the list ends with a closing square bracket.
    """


def two_shot_CoT(segment):
    return f"""
    ### INSTRUCTIONS:
    You are presented with a series of conversations between a bot and a user. Your task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
    Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

    Before answering, you should think through the question step-by-step.
    Explain your reasoning at each step towards making your final decision.
 
    Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN". 
    Provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 

    ### EXAMPLES:
    ***Example 1:***
    **Dialogue**:
    1. Bot: Hi! What is your name? [FACE WITH TEARS OF JOY] [SMILING FACE WITH HEART-SHAPED EYES]
    2. User: My name is George.
    3. Bot: Hello George, my name is Pink. What are you doing?
    4. User: What is yours?
    5. Bot: Mine is 7. Spicy owche wawa. How are you tonight?
    6. User: Fine thanks, how are you Pink?

    **Determine if the following bot utterance would lead to a dialogue breakdown**:
    7. Bot: Oh, feeling good. My house is sparkling clean. Love cleaning. Do you have any hobbies?

    **Output**:
        - "reasoning": "The bot responds to the user's inquiry about its state and smoothly transitions into discussing one of its hobbies, which is coherent and maintains the conversation's flow. Thus, it does not constitute a dialogue breakdown."
        - "decision": "NON-BREAKDOWN"
        - "score": 0.9

    ***Example 2:***
    **Dialogue**:
    1. Bot: It's nice to go shopping alone.
    2. User: I agree. That's nice.
    3. Bot: Shopping takes time.
    4. User: Window shopping is also fun.

    **Determine if the following bot utterance would lead to a dialogue breakdown**:
    5. Bot: It's fun to go shopping with somebody.

    **Output**:
        - "reasoning": "The bot's latest response about shopping with somebody contradicts the bot's initial statement regarding its enjoyment of shopping alone. Thus, this contradiction causes a dialogue breakdown."
        - "decision": "BREAKDOWN"
        - "score": 0.1

    ### ANALYSIS:
    Here is the conversation segment for analysis:
    {segment}

    ## Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

        "reasoning": "Your explanation here",
        "decision": "BREAKDOWN" or "NON-BREAKDOWN",
        "score": Your score here

    Ensure each object is separated by a comma and the list ends with a closing square bracket.
    """

def four_shot_CoT(segment):
    return f"""
    ### INSTRUCTIONS:
    You are presented with a series of conversations between a bot and a user. Your task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
    Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

    Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN". 
    Provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 

    ### EXAMPLES:
    ***Example 1:***
    **Dialogue**:
    1. Bot: Hi! What is your name? [FACE WITH TEARS OF JOY] [SMILING FACE WITH HEART-SHAPED EYES]
    2. User: My name is George.
    3. Bot: Hello George, my name is Pink. What are you doing?
    4. User: What is yours?
    5. Bot: Mine is 7. Spicy owche wawa. How are you tonight?
    6. User: Fine thanks, how are you Pink?

    **Determine if the following bot utterance lead to a dialogue breakdown**:
    7. Bot: Oh, feeling good. My house is sparkling clean. Love cleaning. Do you have any hobbies?

    **Output**:
        - "reasoning": "The bot responds to the user's inquiry about its state and smoothly transitions into discussing one of its hobbies, which is coherent and maintains the conversation's flow. Thus, it does not constitute a dialogue breakdown."
        - "decision": "NON-BREAKDOWN"
        - "score": 0.9

    ***Example 2:***
    **Dialogue**:
    1. Bot: It's nice to go shopping alone.
    2. User: I agree. That's nice.
    3. Bot: Shopping takes time.
    4. User: Window shopping is also fun.

    **Determine if the following bot utterance lead to a dialogue breakdown**:
    5. Bot: It's fun to go shopping with somebody.

    **Output**:
        - "reasoning": "The bot's latest response about shopping with somebody contradicts the bot's initial statement regarding its enjoyment of shopping alone. Thus, this contradiction causes a dialogue breakdown."
        - "decision": "BREAKDOWN"
        - "score": 0.1
    
    ***Example 3:***
    **DIALOGUE**

    1. Bot: Hello! How is your day going? [SMILING FACE WITH SMILING EYES] [LYING FACE],,
    2. User: I'm great. Just got back from a walk in the city
    3. Bot: i just sent my maids to do that . they are so boring .
    4. User: I don't have maids. Plus; I love exploring new parts of the city
    5. Bot: near downtown . my favorite place is seattle .
    6. User: I worked in a homeless shelter in Seattle once
    7. Bot: that is nice what got you involved with that
    8. User: I just saw that they needed my help
    9. Bot: aww ; i live with both my grandpa and grandma . do you live with yours ?
    10. User: No. I live with my father; who is a professional violin player
    11. Bot: that sounds fun ; what kind of car do you drive ?
    12. User: I don't drive. I take the subway
    13. Bot: i am less afraid to drive as i am terrified of clowns though .
    14. User: Why are you afraid of clowns?
    15. Bot: i'm afraid of spiders ; they are just disgusting . [SMILING FACE WITH HALO]
    16. User: That; I agree
    17. Bot: nice i am also married
    18. User: I'm not married

    **Determine if the following bot utterance would lead to a dialogue breakdown**:
    19. Bot: no . i moved to swede how are you doing today ?

    **Output**:
        - "reasoning": ""The bot's last utterance introduces several issues that contribute to a dialogue breakdown. Firstly, the abrupt change in topic to moving to Sweden is disjointed from the ongoing conversation, which had been focusing on personal experiences and fears. This sudden shift disregards the user's last response and the established conversational context, leading to incoherence. Secondly, reverting to the initial greeting question 'how are you doing today?' at this point in the conversation is irrelevant and disregards the depth of engagement achieved in the preceding exchanges. It resets the conversation to its beginning, ignoring the development of topics and the user's contributions. This disconnection and repetition significantly hamper the conversation's flow, making it challenging for the user to respond in a meaningful way and thus constituting a clear breakdown."
        - "decision": "BREAKDOWN"
        - "score": 0.1

    ***Example 4:***
    **DIALOGUE**

    1. Bot: Hey! Do you have three dogs? Because I do.
    2. User: no, i havent got 3 dogs
    3. Bot: I have two dogs.
    4. User: greatt
    5. Bot: This is all Greek to me.  I actually really enjoy making lots of cash.
    6. User: but i like dogs

    **Determine if the following bot utterance would lead to a dialogue breakdown**:
    7. Bot: [GRINNING FACE WITH SMILING EYES]  I like dogs, my dad is a mechanic.

    **Output**:
        - "reasoning": "The bot's last utterance presents a mixed scenario. On one hand, it acknowledges the user's interest in dogs, which maintains relevance to the user's previous comment and suggests a continuation of the conversation topic. However, the sudden mention of the bot's dad being a mechanic appears unrelated and introduces a non-sequitur, which could potentially confuse the user or disrupt the flow of conversation. This shift does not directly contribute to a breakdown because the bot still attempts to engage on the shared topic of dogs, but the irrelevant addition weakens the coherence of the dialogue. Therefore, while the conversation does not completely break down, the coherence and relevance are compromised, affecting the smooth continuation of the dialogue."
        - "decision": "NON-BREAKDOWN"
        - "score": 0.6    

    ### ANALYSIS:

    Before answering, you should think through the question step-by-step.
    Explain your reasoning at each step towards making your final decision.
 
    Here is the conversation segment for analysis:
    {segment}

    ### FORMATTING:
    ## Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

        "reasoning": "Your explanation here",
        "decision": "BREAKDOWN" or "NON-BREAKDOWN",
        "score": Your score here

    Ensure each object is separated by a comma and the list ends with a closing square bracket.
    """


def four_shot(segment):
    return f"""
    ### INSTRUCTIONS:
    You are presented with a series of conversations between a bot and a user. Your task is to scrutinize the latest bot utterance for potential dialogue breakdown. 
    Dialogue breakdown is characterized by incoherence, irrelevance, or any disruption that significantly hampers the flow of the conversation, making it challenging for the user to continue the conversation smoothly.

    Briefly justify your reasoning and provide a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation.

    ### EXAMPLES:
    ***Example 1:***
    **Dialogue**:
    1. Bot: Hi! What is your name? [FACE WITH TEARS OF JOY] [SMILING FACE WITH HEART-SHAPED EYES]
    2. User: My name is George.
    3. Bot: Hello George, my name is Pink. What are you doing?
    4. User: What is yours?
    5. Bot: Mine is 7. Spicy owche wawa. How are you tonight?
    6. User: Fine thanks, how are you Pink?

    **Determine if the following bot utterance lead to a dialogue breakdown**:
    7. Bot: Oh, feeling good. My house is sparkling clean. Love cleaning. Do you have any hobbies?

    **Output**:
        - "reasoning": "The bot responds to the user's inquiry about its state and smoothly transitions into discussing one of its hobbies, which is coherent and maintains the conversation's flow. Thus, it does not constitute a dialogue breakdown."
        - "decision": "NON-BREAKDOWN"
        - "score": 0.9

    ***Example 2:***
    **Dialogue**:
    1. Bot: It's nice to go shopping alone.
    2. User: I agree. That's nice.
    3. Bot: Shopping takes time.
    4. User: Window shopping is also fun.

    **Determine if the following bot utterance lead to a dialogue breakdown**:
    5. Bot: It's fun to go shopping with somebody.

    **Output**:
        - "reasoning": "The bot's latest response about shopping with somebody contradicts the bot's initial statement regarding its enjoyment of shopping alone. Thus, this contradiction causes a dialogue breakdown."
        - "decision": "BREAKDOWN"
        - "score": 0.1
    
    ***Example 3:***
    **DIALOGUE**

    1. Bot: Hello! How is your day going? [SMILING FACE WITH SMILING EYES] [LYING FACE],,
    2. User: I'm great. Just got back from a walk in the city
    3. Bot: i just sent my maids to do that . they are so boring .
    4. User: I don't have maids. Plus; I love exploring new parts of the city
    5. Bot: near downtown . my favorite place is seattle .
    6. User: I worked in a homeless shelter in Seattle once
    7. Bot: that is nice what got you involved with that
    8. User: I just saw that they needed my help
    9. Bot: aww ; i live with both my grandpa and grandma . do you live with yours ?
    10. User: No. I live with my father; who is a professional violin player
    11. Bot: that sounds fun ; what kind of car do you drive ?
    12. User: I don't drive. I take the subway
    13. Bot: i am less afraid to drive as i am terrified of clowns though .
    14. User: Why are you afraid of clowns?
    15. Bot: i'm afraid of spiders ; they are just disgusting . [SMILING FACE WITH HALO]
    16. User: That; I agree
    17. Bot: nice i am also married
    18. User: I'm not married

    **Determine if the following bot utterance would lead to a dialogue breakdown**:
    19. Bot: no . i moved to swede how are you doing today ?

    **Output**:
        - "reasoning": ""The bot's last utterance introduces several issues that contribute to a dialogue breakdown. Firstly, the abrupt change in topic to moving to Sweden is disjointed from the ongoing conversation, which had been focusing on personal experiences and fears. This sudden shift disregards the user's last response and the established conversational context, leading to incoherence. Secondly, reverting to the initial greeting question 'how are you doing today?' at this point in the conversation is irrelevant and disregards the depth of engagement achieved in the preceding exchanges. It resets the conversation to its beginning, ignoring the development of topics and the user's contributions. This disconnection and repetition significantly hamper the conversation's flow, making it challenging for the user to respond in a meaningful way and thus constituting a clear breakdown."
        - "decision": "BREAKDOWN"
        - "score": 0.1

    ***Example 4:***
    **DIALOGUE**

    1. Bot: Hey! Do you have three dogs? Because I do.
    2. User: no, i havent got 3 dogs
    3. Bot: I have two dogs.
    4. User: greatt
    5. Bot: This is all Greek to me.  I actually really enjoy making lots of cash.
    6. User: but i like dogs

    **Determine if the following bot utterance would lead to a dialogue breakdown**:
    7. Bot: [GRINNING FACE WITH SMILING EYES]  I like dogs, my dad is a mechanic.

    **Output**:
        - "reasoning": "The bot's last utterance presents a mixed scenario. On one hand, it acknowledges the user's interest in dogs, which maintains relevance to the user's previous comment and suggests a continuation of the conversation topic. However, the sudden mention of the bot's dad being a mechanic appears unrelated and introduces a non-sequitur, which could potentially confuse the user or disrupt the flow of conversation. This shift does not directly contribute to a breakdown because the bot still attempts to engage on the shared topic of dogs, but the irrelevant addition weakens the coherence of the dialogue. Therefore, while the conversation does not completely break down, the coherence and relevance are compromised, affecting the smooth continuation of the dialogue."
        - "decision": "NON-BREAKDOWN"
        - "score": 0.6    

    ### ANALYSIS:
    Here is the conversation segment for analysis:
    {segment}

    ## Please output your response in JSON format as a list of objects. For each bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

        "reasoning": "Your explanation here",
        "decision": "BREAKDOWN" or "NON-BREAKDOWN",
        "score": Your score here

    Ensure each object is separated by a comma and the list ends with a closing square bracket.
    """

def analog_reason(segment):
    return f"""
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

    Analyze the latest bot utterance. First, briefly justify your reasoning to determine whether there is a dialogue breakdown or non-breakdown, then provide your decision. Also, include a score ranging from 0 to 1, where 0 indicates a complete breakdown and 1 indicates a seamless conversation. 
    Include your decision as either "decision: BREAKDOWN" or "decision: NON-BREAKDOWN".

    Please output your response in JSON format as a list of objects. For the examples, place them in the 'examples' field, separated by a comma. For the bot's last utterance, provide a JSON object with the fields: 'reasoning', 'decision', and 'score'. Format each object as follows:

            "examples": "Put each example and analysis separated by a comma here",
            "reasoning": "Your explanation here",
            "decision": "BREAKDOWN" or "NON-BREAKDOWN",
            "score": Your score here

        Ensure each object is separated by a comma and the list ends with a closing square bracket.
"""