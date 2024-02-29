from BoardRepository import BoardRepository

class GameController:
    def __init__(self,repository: BoardRepository):
        self.repository = repository
        
    def play_turn(self, row, col, symbol):
        return self.repository.place_symbol(row, col, symbol)
    
    def board_full(self):
        return self.repository.is_full()
    
    def order_winning_moves(self):
        """
        
        """
        
        board = self.repository.get_board()
        for symbol in ['X', 'O']:
            for i in range(6):
                for j in range(2):
                    #Check rows for potential win
                    if self.check_sequence(board[i][j:j+5], symbol):
                        return(i,j + board[i][j:j+5].index(' '), 'O' if symbol == 'O' else 'X')
                    #Check for columns for potential win
                    column = [board[x][i] for x in range(j, j+5)]
                    if self.check_sequence(column, symbol):
                        return(j + column.index(' '), i, 'O' if symbol == 'O' else 'X')
                    #Check diagonals for potential win
                    if i < 2 and j < 2: #Onyl makes sense from the top left part of the board
                        diagonal = [board[i+x][j+x] for x in range(5)]
                        if self.check_sequence(diagonal,symbol):
                            return(i+diagonal.index(' '), j + diagonal.index(' '), 'O' if symbol == 'O' else 'X')
                        anti_diagonal = [board[i+x][j+4-x] for x in range(5)]
                        if self.check_sequence(anti_diagonal, symbol):
                            return (i+anti_diagonal.index(' '), j+4-anti_diagonal.index(' '), 'O' if symbol == 'O' else 'X')
            return None
    
    def most_common_symbol(self):
        board = self.repository.get_board()
        symbols = {'X' : 0, 'O' : 0}
        for row in board:
            for cell in row:
                if cell in symbols:
                    symbols[cell] += 1
        #Choose X by default if X = O
        most_common = max(symbols, key=symbols.get)
        return most_common if symbols[most_common] > 0 else 'X'
    
    def find_optimal_position(self, symbol):
        board = self.repository.get_board()
        max_neighbors = -1
        best_position = None
        for row in range(6):
            for col in range(6):
                if board[row][col] == ' ': #Empty square
                    neighbors = self.count_neighbors(row, col, symbol, board)
                    if neighbors > max_neighbors:
                        max_neighbors = neighbors
                        best_position = (row,col)
        return best_position
    
    def count_neighbors(self, row, col, symbol, board):
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),
                      (1,1), (1,-1)]
        neighbors = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 6 and 0 <= c < 6 and board[r][c] == symbol:
                neighbors += 1
        return neighbors
    
    def place_most_common_symbol(self):
        symbol = self.most_common_symbol()
        if symbol:
            position = self.find_optimal_position(symbol)
            if position:
                self.play_turn(position[0], position[1], symbol)
                print(f"Order places {symbol} at {position[0]}, {position[1]}")
                return True
        return False
      
    def check_sequence(self, segment, symbol):          
        """
        Determines if either player, Order or Chaos, has won the game. Order wins if there are 5 consecutive pieces of the same type (either X or O) in a row, column, or diagonal. 
        Chaos wins if the board is filled without this condition being met.
        Parameters: None
        Returns:
            A string "Order" if Order wins.
            A string "Chaos" if Chaos wins (the board is full and Order hasn't met its win condition).
            None if the game is still ongoing (no winner yet).
            """

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

        if self.repository.is_full():
            return "Chaos"
        return None
    
    def board_full(self):
        return self.repository.is_full()        