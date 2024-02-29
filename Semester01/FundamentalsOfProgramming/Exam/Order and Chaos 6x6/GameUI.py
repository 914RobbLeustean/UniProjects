from GameController import GameController
import random

class GameUI:
    def __init__(self, controller: GameController):
        self.controller = controller

    def display_board(self):
        board = self.controller.repository.get_board()
        for row in board:
            print(" | ".join(row))
            print("-" * 22)

    def get_player_move(self):
        while True:
            try:
                row = int(input("Enter row (0-5): "))
                col = int(input("Enter column (0-5): "))
                symbol = input("Enter symbol (X/O): ").upper()
                if symbol not in ["X", "O"]:
                    raise ValueError("Invalid symbol")
                return row, col, symbol
            except ValueError as e:
                print(f"Invalid input: {e}")

    def get_chaos_move(self):
        blocking_move = self.controller.find_blocking_move()
        if blocking_move:
            row, col, symbol = blocking_move
            # Ensure the blocking move is executed on the board
            if self.controller.play_turn(row, col, symbol):
                print(f"Chaos blocks at {row},{col} with {symbol}")
                return
            else:
                print("Error applying blocking move. This should never happen.")
        
        # If no blocking move is found or applying the blocking move failed, make a random valid move
        while True:
            row, col = random.randint(0, 5), random.randint(0, 5)
            symbol = random.choice(['X', 'O'])
            if self.controller.play_turn(row, col, symbol):
                print(f"Chaos moves at {row},{col} with {symbol}")
                break


    def start_game(self):
        turn = "Order"  # Order starts
        while True:
            self.display_board()
            if turn == "Order":
                row, col, symbol = self.get_player_move()
                if not self.controller.play_turn(row, col, symbol):
                    print("Invalid move, try again.")
                    continue
            else:  # Chaos's turn
                self.get_chaos_move()

            if self.controller.check_win_condition():
                print(f"Order wins!")
                break
            elif self.controller.board_full():
                print("Chaos wins!")
                break

            turn = "Chaos" if turn == "Order" else "Order"