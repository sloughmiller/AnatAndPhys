import json

def load_flashcards(filename):
    with open(filename, 'r') as file:
        flashcards = json.load(file)
    return flashcards

def quiz_user(flashcards):
    for flashcard in flashcards:
        print(f"Question: {flashcard['question']}")
        input("Press Enter to see the answer...")
        print(f"Answer: {flashcard['answer']}")
        print("\n")

def main():
    filename = 'flashcards.json'
    flashcards = load_flashcards(filename)
    quiz_user(flashcards)

if __name__ == "__main__":
    main()
