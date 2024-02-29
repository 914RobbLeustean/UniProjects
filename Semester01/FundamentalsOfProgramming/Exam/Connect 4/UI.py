from repository import Connect4Repository
from controller import Connect4Controller
import unittest
import test_connect4

class Connect4UI:
    def __init__(self, controller):
        self.controller = controller
    
    def print_board(self):
        for row in self.controller.repo.board:
            print(row)
    
    def start_game(self):
        while not self.controller.game_over:
            if self.controller.turn == 0:
                self.print_board()
                column = int(input("Player 1 Make your Selection (0-6): "))
                print(self.controller.player_move(column))
            else:
                print("Computer's turn.")
                print(self.controller.computer_move())
        self.print_board()
        print("Game over.")

def run_tests():
        """Runs the unit tests for the Connect 4 game logic."""
        # Load the test cases from the test module
        test_suite = unittest.TestLoader().loadTestsFromModule(test_connect4)
        # Create a test runner that outputs to the console
        test_runner = unittest.TextTestRunner()
        # Run the tests
        test_runner.run(test_suite)

repository = Connect4Repository()
controller = Connect4Controller(repository)
ui = Connect4UI(controller)
ui.start_game()
#run_tests()