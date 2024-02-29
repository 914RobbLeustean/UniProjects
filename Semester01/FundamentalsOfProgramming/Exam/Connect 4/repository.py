class Connect4Repository:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = self.create_board()
    
    def create_board(self):
        return [[0 for _ in range(self.columns)] for _ in range(self.rows)]
    
    def drop_piece(self, column, piece):
        for row in reversed(range(self.rows)):
            if self.board[row][column] == 0:
                self.board[row][column] = piece
                return True
        return False
    
    def is_valid_location(self, column):
        return self.board[0][column] == 0
    
    def check_win(self, piece):
        #Check horizontal locations
        for c in range(self.columns-3):
            for r in range(self.rows):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True
        #Check vertical locations
        for c in range(self.columns):
            for r in range(self.rows-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True
        #Check positively sloped diagonals
        for c in range(self.columns-3):
            for r in range(self.rows-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True
        #Check negatively sloped diagonals
        for c in range(self.columns-3):
            for r in range(3, self.rows):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True
        return False
    
    def is_full(self):
        return all(self.board[0][c] != 0 for c in range(self.columns))