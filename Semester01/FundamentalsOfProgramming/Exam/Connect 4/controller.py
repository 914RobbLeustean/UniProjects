import random

class Connect4Controller:
    def __init__(self, repository):
        self.repo = repository
        self.player_piece = 1
        self.computer_piece = 2
        self.game_over = False
        self.turn = 0  # 0 for player, 1 for computer
    
    def player_move(self, column):
        """
        Processes a move by the player.
        Parameters: column: An integer representing the column where the player wants to drop their piece.
        Returns: A string message indicating the outcome of the move (success, invalid move, player wins, or draw). 
        """
        
        if self.repo.is_valid_location(column):
            self.repo.drop_piece(column, self.player_piece)
            if self.repo.check_win(self.player_piece):
                self.game_over = True
                return "Player wins!"
            if self.repo.is_full():
                self.game_over = True
                return "Game is a draw!"
            self.turn = 1
            return "Move successful."
        else:
            return "Invalid move. Try again."
    
    def computer_move(self):
        """
        Calculates and executes a move by the computer based on the current board state.
        Immediate Win Check: If the computer can win in the next move, it takes that move.
        Block Opponent's Win: If the player is about to win in their next move, the computer blocks that move.
        Center Preference: Favor placing pieces in the center columns, as this generally allows for more opportunities to connect four.
        Random Fallback: If none of the above conditions are met, the computer will make a random valid move.
        Parameters: None.
        Returns: A string message indicating the outcome of the computer's move (computer moved, computer wins, or draw). 
        """
        
        for col in range(self.repo.columns):
            if self.repo.is_valid_location(col):
                # Simulate the move in that column for win
                self.repo.drop_piece(col, self.computer_piece)
                if self.repo.check_win(self.computer_piece):
                    self.game_over = True
                    return "Computer wins!"
                self.repo.board[next(r for r in range(self.repo.rows) if self.repo.board[r][col] != 0)][col] = 0

        for col in range(self.repo.columns):
            if self.repo.is_valid_location(col):
                # Simulate the move in that column for block
                self.repo.drop_piece(col, self.player_piece)
                if self.repo.check_win(self.player_piece):
                    self.repo.board[next(r for r in range(self.repo.rows) if self.repo.board[r][col] != 0)][col] = 0
                    self.repo.drop_piece(col, self.computer_piece)
                    if self.repo.check_win(self.computer_piece) or self.repo.is_full():
                        self.game_over = True
                    self.turn = 0
                    return "Computer moved."
                self.repo.board[next(r for r in range(self.repo.rows) if self.repo.board[r][col] != 0)][col] = 0
        
        # Prefer center column
        if self.repo.is_valid_location(3):
            self.repo.drop_piece(3, self.computer_piece)
            if self.repo.check_win(self.computer_piece):
                self.game_over = True
                return "Computer wins!"
            if self.repo.is_full():
                self.game_over = True
                return "Game is a draw!"
            self.turn = 0
            return "Computer moved."
        
        # Fallback to random move
        column = random.choice([c for c in range(self.repo.columns) if self.repo.is_valid_location(c)])
        self.repo.drop_piece(column, self.computer_piece)
        if self.repo.check_win(self.computer_piece):
            self.game_over = True
            return "Computer wins!"
        if self.repo.is_full():
            self.game_over = True
            return "Game is a draw!"
        self.turn = 0
        return "Computer moved."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    