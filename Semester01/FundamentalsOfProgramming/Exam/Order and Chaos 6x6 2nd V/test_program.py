from BoardRepository import BoardRepository
from GameController import GameController
import unittest

class TestCheckWinCondition(unittest.TestCase):
    def setUp(self):
        self.repository = BoardRepository()
        self.controller = GameController(self.repository)

    def place_symbols(self, positions, symbol):
        """Utility method for placing symbols on the board."""
        for row, col in positions:
            self.repository.place_symbol(row, col, symbol)

    def test_order_wins_row(self):
        """Test Order wins with a row of 5 consecutive symbols."""
        self.place_symbols([(0, i) for i in range(5)], 'X')
        self.assertEqual(self.controller.check_win_condition(), "Order")

    def test_order_wins_column(self):
        """Test Order wins with a column of 5 consecutive symbols."""
        self.place_symbols([(i, 0) for i in range(5)], 'X')
        self.assertEqual(self.controller.check_win_condition(), "Order")

    def test_order_wins_diagonal(self):
        """Test Order wins with a diagonal of 5 consecutive symbols."""
        self.place_symbols([(i, i) for i in range(5)], 'X')
        self.assertEqual(self.controller.check_win_condition(), "Order")

    def test_chaos_wins(self):
        """Test Chaos wins when the board is full without Order winning."""
        # Fill the board in a pattern that doesn't allow 5 in a row for either symbol
        for row in range(6):
            for col in range(6):
                symbol = 'X' if (row + col) % 2 == 0 else 'O'
                self.repository.place_symbol(row, col, symbol)
        self.assertEqual(self.controller.check_win_condition(), "Chaos")

    def test_no_winner(self):
        """Test that no winner is reported when the game is still ongoing."""
        self.place_symbols([(0, 0), (0, 1), (0, 2)], 'X')
        self.assertIsNone(self.controller.check_win_condition())


