from GameController import GameController
import random

class GameUI:
    def __init__(self, controller: GameController):
        self.controller = controller
        
    def display_board(self):
        board = self.controller.repository.get_board()
        for row in board:
            print(" | ".join(row))
            print("-" * 17)
            
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
                print(f"Invalid inp;ut: {e}")
    
    def get_order_move(self):
        winning_move = self.controller.order_winning_moves()
        if winning_move:
            row, col, symbol = winning_move
            #Ensure the winning move is executed
            if self.controller.play_turn(row, col, symbol):
                print(f"Order wins at {row},{col} with symbol {symbol}")
                return
            else:
                print("Error placing winning move. This shouldn't happen.")
        
        #If no winning move is found, make a good valid move.
        symbol = self.controller.most_common_symbol()
        position = self.controller.find_optimal_position(symbol)
        if position:
            row, col = position
            if self.controller.play_turn(row, col, symbol):
                print(f"Order places {symbol} at {row}, {col} strategically.")
            else:
                print("Error placing strategic move. This should be a valid move.")
        else:
            print("No valid strategic moves available. This is an unexpected state.")
                               
    
    def start_game(self):
        turn = "Order"
        while True:
            self.display_board()
            if turn == "Chaos":
                row, col, symbol = self.get_player_move()
                if not self.controller.play_turn(row, col, symbol):
                    print("Invalid move, try")
                    continue
            else: #Order turn
                self.get_order_move()
                
            if self.controller.check_win_condition():
                print(f"Order wins!")
                break
            elif self.controller.board_full():
                print("Chaos wins!")
                break
            
            turn = "Chaos" if turn == "Order" else "Order"            