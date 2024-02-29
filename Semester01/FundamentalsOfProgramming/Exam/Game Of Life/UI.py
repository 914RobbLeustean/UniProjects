from Repository import GameOfLifeGrid
from Controller import GameOfLifeController
import unittest
from test_game_of_life import TestGameOfLifeTick

def run_tests():
    """Runs the unit tests for the Game of Life logic."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGameOfLifeTick)
    unittest.TextTestRunner().run(suite)

class GameOfLifeUI:
    def __init__(self, controller):
        self.controller = controller

    def start(self):
        print("Welcome to the Game of Life!")
        self.controller.grid.display()  # Display the empty grid at the start
        while True:
            command_input = input("Enter command: ")
            command = command_input.split()
            if not command:
                print("No command entered.")
                continue
            cmd = command[0]
            if cmd == "place" and len(command) >= 3:
                pattern = command[1]
                position = command[2]
                try:
                    self.controller.place_pattern(pattern, position)
                    self.controller.grid.display()  # Display grid after placing a pattern
                except ValueError as e:
                    print(f"Error: {e}")
            elif cmd == "tick":
                n = 1
                if len(command) > 1:
                    try:
                        n = int(command[1])
                    except ValueError:
                        print("Invalid number of generations. Defaulting to 1.")
                self.controller.advance_generations(n)
                self.controller.grid.display()  # Display grid after ticking
            elif cmd == "display":
                self.controller.grid.display()
            elif cmd == "exit":
                print("Exiting the Game of Life.")
                break
            else:
                print("Unknown command.")
        
grid = GameOfLifeGrid()
Controller = GameOfLifeController(grid)
ui = GameOfLifeUI(Controller)
#ui.start()
run_tests()