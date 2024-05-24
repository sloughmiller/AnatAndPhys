import re
import json

def parse_document(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Define patterns to identify questions and answers
    question_pattern = re.compile(r'\d+\.\s+([^\n]+)')
    answer_pattern = re.compile(r'[a-z]\.\s+([^\n]+)')

    questions = question_pattern.findall(content)
    answers = answer_pattern.findall(content)

    flashcards = []

    for i in range(len(questions)):
        question = questions[i].strip()
        if i < len(answers):
            answer = answers[i].strip()
        else:
            answer = 'No answer provided'
        
        flashcards.append({
            'question': question,
            'answer': answer
        })

    return flashcards

def save_flashcards(flashcards, output_path):
    with open(output_path, 'w') as file:
        json.dump(flashcards, file, indent=4)

# Usage
file_path = 'CellBiology.txt'  # Path to your document
output_path = 'flashcards.json'  # Path to save the flashcards

flashcards = parse_document(file_path)
save_flashcards(flashcards, output_path)

print(f"Flashcards saved to {output_path}")
