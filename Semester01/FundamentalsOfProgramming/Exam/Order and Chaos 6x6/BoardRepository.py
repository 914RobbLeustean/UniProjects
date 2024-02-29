class BoardRepository:
    def __init__(self):
        self.board = [[" " for _ in range(7)] for _ in range(6)]

    def place_symbol(self, row, col, symbol):
        if self.is_valid_position(row, col) and self.is_empty(row, col):
            self.board[row][col] = symbol
            return True
        return False

    def is_valid_position(self, row, col):
        return 0 <= row < 6 and 0 <= col < 6

    def is_empty(self, row, col):
        return self.board[row][col] == " "

    def is_full(self):
        return all(self.board[row][col] != " " for row in range(6) for col in range(6))

    def get_board(self):
        return self.board
