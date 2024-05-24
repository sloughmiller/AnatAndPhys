import ui
import json
import os

class FlashcardApp(ui.View):
    def __init__(self):
        self.flashcards = self.load_flashcards('flashcards.json')
        self.current_index = 0
        self.showing_answer = False

        # Create and configure the question/answer label
        self.label = ui.Label(frame=(0, 0, self.width, self.height))
        self.label.flex = 'WH'
        self.label.alignment = ui.ALIGN_CENTER
        self.label.number_of_lines = 0
        self.add_subview(self.label)
        
        # Show the first question
        self.update_label()

    def load_flashcards(self, filename):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        with open(path, 'r') as file:
            flashcards = json.load(file)
        return flashcards

    def update_label(self):
        if self.showing_answer:
            self.label.text = self.flashcards[self.current_index]['answer']
        else:
            self.label.text = self.flashcards[self.current_index]['question']

    def next_flashcard(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.showing_answer = False
        self.update_label()

    def touch_ended(self, touch):
        if self.showing_answer:
            self.next_flashcard()
        else:
            self.showing_answer = True
            self.update_label()

def main():
    # Set up the main view
    root_view = FlashcardApp()
    root_view.present('fullscreen')

if __name__ == '__main__':
    main()
