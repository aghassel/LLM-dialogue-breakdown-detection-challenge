import glob

def read_dialogues(folder_path):
    dialogues = []
    for file in glob.glob(f"{folder_path}/*.txt"):
        with open(file, 'r', encoding='utf-8') as f:
            dialogues.append(f.read())
    return dialogues

def create_dialogue_segments(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        dialogue = file.read()
    lines = dialogue.split('\n')
    segments = []
    bot_responses = []
    current_segment = []

    for i, line in enumerate(lines):
        # Split the line at the first period to separate the speaker
        parts = line.split('.', 1)
        if len(parts) == 2:
            current_segment.append(line)  # Add line to the current segment

            if parts[1].strip().startswith("Bot:"):
                # Split the segment into conversation history and bot's response
                conversation_history = "\n".join(current_segment[:-1])
                bot_response = current_segment[-1]
                segment = f"\n**DIALOGUE**\n{conversation_history}\n\n" \
                          f"**Determine if the following bot utterance would lead to a dialogue breakdown**:\n" \
                          f"{bot_response}\n"
                segments.append(segment)
                bot_responses.append(bot_response)

    return segments, bot_responses
