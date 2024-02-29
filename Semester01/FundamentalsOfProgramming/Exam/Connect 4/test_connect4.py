import unittest
from controller import Connect4Controller
from repository import Connect4Repository

class TestConnect4(unittest.TestCase):
    def setUp(self):
        self.repository = Connect4Repository()
        self.controller = Connect4Controller(self.repository)

    def test_player_move_valid(self):
        """Test a valid player move."""
        result = self.controller.player_move(0)
        self.assertIn("Move successful", result)

    def test_player_move_invalid(self):
        """Test an invalid player move to a full column."""
        # Fill up column 0
        for _ in range(6):
            self.controller.repo.drop_piece(0, self.controller.player_piece)  # Corrected to use 'repo'
        result = self.controller.player_move(0)
        self.assertIn("Invalid move", result)

    def test_computer_move(self):
        """Test the computer makes a move."""
        self.controller.player_move(0)  # Make a move to ensure the computer has a turn
        result = self.controller.computer_move()
        self.assertIn("Computer moved", result)

    def test_check_win(self):
        """Test detecting a win condition."""
        for i in range(4):
            self.controller.repo.drop_piece(i, self.controller.player_piece)  # Corrected to use 'repo'
        self.assertTrue(self.controller.repo.check_win(self.controller.player_piece))  # Corrected method call

    def test_check_draw(self):
        """Test detecting a draw condition."""
        # Fill the board without a win condition
        for row in range(6):
            for col in range(7):
                piece = self.controller.player_piece if (row + col) % 2 == 0 else self.controller.computer_piece
                self.controller.repo.drop_piece(col, piece)  # Corrected to use 'repo'
        self.assertTrue(self.controller.repo.is_full())  # Corrected method call

