from hangman_game_controller import HangmanGameController

class HangmanGameUI:
    def __init__(self, controller, repository):
        self.controller = controller
        self.repository = repository

    def main_menu(self):
        while True:
            print("\n1. Play Hangman")
            print("2. Add a New Sentence")
            print("3. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.play()
            elif choice == '2':
                self.add_sentence_ui()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose again.")
    
    def play(self):
        self.controller.select_sentence()
        while not (self.controller.is_win() or self.controller.is_lose()):
            print("\nCurrent sentence:", self.controller.get_display_sentence())
            print("Hangman status:", self.controller.hangman)
            guess = input("Guess a letter: ").upper().strip()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please guess a single letter.")
                continue
            if guess in self.controller.guessed_letters:
                print(f"You've already guessed '{guess}'. Try a different letter.")
                continue
            self.controller.guess_letter(guess)
        if self.controller.is_win():
            print("Congratulations! You've guessed the sentence:", self.controller.sentence)
        else:
            print("Game over! The sentence was:", self.controller.sentence)
    
    def add_sentence_ui(self):
        sentence = input("Enter a new sentence: ").strip()
        if self.repository.add_sentence(sentence):
            print("Sentence added successfully.")
        else:
            print("Failed to add sentence.")


