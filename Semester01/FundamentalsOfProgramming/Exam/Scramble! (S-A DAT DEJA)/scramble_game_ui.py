from scramble_game_controller import ScrambleGameController
from sentence_repository import SentenceRepository
class ScrambleGameUI:
    def __init__(self, controller: ScrambleGameController):
        self.controller = controller

    def start_game(self):
        self.controller.start_new_game()
        while not self.controller.check_victory() and self.controller.get_score() > 0:
            print(f"Scrambled sentence: {self.controller.get_current_sentence()}")
            print(f"Score: {self.controller.get_score()}")
            self.process_user_input()
            
            if self.controller.check_victory():
                print("Congratulations, you've unscrambled the sentence!")
                break
            elif self.controller.get_score() <= 0:
                print("Game over. You've run out of score.")
                break

    def process_user_input(self):
        user_input = input("Enter your command (swap, undo last swap): ")
        if user_input.startswith("swap"):
            try:
                _, positions = user_input.split()
                pos1, pos2 = map(int, positions.split('-'))
                if not self.controller.swap_letters(pos1, pos2):
                    print("Invalid swap. Try again.")
            except ValueError:
                print("Invalid input format. Please follow the 'swap pos1-pos2' format.")
        elif user_input.strip() == "undo":
            if not self.controller.undo_last_swap():
                print("Nothing to undo.")
