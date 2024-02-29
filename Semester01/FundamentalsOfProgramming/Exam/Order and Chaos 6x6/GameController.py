from BoardRepository import BoardRepository

class GameController:
    def __init__(self, repository: BoardRepository):
        self.repository = repository

    def play_turn(self, row, col, symbol):
        return self.repository.place_symbol(row, col, symbol)

    def find_blocking_move(self):
        """
        Determines whether the opponent (Order) is one move away from winning by having four consecutive symbols in a row, column, or diagonal. If so it places the opposite
        symbol on the 5th position to stop Order from winning.
        Parameters: None
        Returns: A tuple (row, col, symbol) indicating the position (row and column) where Chaos should place a symbol to block Order's win with the opposite symbol of the four
        consecutive ones. If no such "threat" exists, it returns 'None'.
        
        """
        
        board = self.repository.get_board()
        for symbol in ['X', 'O']:  # Iterate through both symbols to check for Order's potential win
            for i in range(6):
                for j in range(2): #We use this for since there can be multiple ways of winning. Either starting from pos 0-4 or pos 1-5
                    # Check rows for potential win
                    if self.check_sequence(board[i][j:j+5], symbol): #
                        return (i, j + board[i][j:j+5].index(' '), 'O' if symbol == 'X' else 'X') #We return the row index where the winning seq. is found, as well with the column index
                    # Check columns for potential win
                    column = [board[x][i] for x in range(j, j+5)]
                    if self.check_sequence(column, symbol):
                        return (j + column.index(' '), i, 'O' if symbol == 'X' else 'X')
                    # Check diagonals for potential win
                    if i < 2 and j < 2:
                        diagonal = [board[i+x][j+x] for x in range(5)]
                        if self.check_sequence(diagonal, symbol):
                            return (i + diagonal.index(' '), j + diagonal.index(' '), 'O' if symbol == 'X' else 'X')
                        anti_diagonal = [board[i+x][j+4-x] for x in range(5)]
                        if self.check_sequence(anti_diagonal, symbol):
                            return (i + anti_diagonal.index(' '), j + 4 - anti_diagonal.index(' '), 'O' if symbol == 'X' else 'X')
        return None
    
    def check_sequence(self, segment, symbol):
        """Check if a segment contains 4 of the same symbol and one empty space."""
        return segment.count(symbol) == 4 and segment.count(' ') == 1
    
    def check_segment(self, segment, symbol):
        """Check if a segment contains 4 symbols and an empty space"""
        return segment.count(symbol) == 4 and segment.count(' ') == 1       
    
    def check_win_condition(self):
        board = self.repository.get_board()
        # Check rows, columns, diagonals for 5 consecutive symbols
        for i in range(6):
            for j in range(2):
                # Check row
                if len(set(board[i][j:j+5])) == 1 and board[i][j] != " ":
                    return "Order"
                # Check column
                if len(set(board[j+k][i] for k in range(5))) == 1 and board[j][i] != " ":
                    return "Order"

        # Check diagonals
        for i in range(2):
            for j in range(2):
                if len(set(board[i+k][j+k] for k in range(5))) == 1 and board[i][j] != " ":
                    return "Order"
                if len(set(board[i+k][j+4-k] for k in range(5))) == 1 and board[i][j+4] != " ":
                    return "Order"

        return None
    def check_win_condition_chaos(self):
        if self.repository.is_full():
                return "Chaos"

    def board_full(self):
        return self.repository.is_full()
