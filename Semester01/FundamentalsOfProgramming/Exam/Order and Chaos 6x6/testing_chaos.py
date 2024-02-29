import unittest
from GameController import GameController
from BoardRepository import BoardRepository

class TestFindBlockingMove(unittest.TestCase):
    def setUp(self):
        self.repository = BoardRepository()
        self.controller = GameController(self.repository)

    def place_symbols(self, positions, symbol):
        """Utility method to place symbols on the board for setup."""
        for row, col in positions:
            self.repository.place_symbol(row, col, symbol)

    def test_blocking_row(self):
        """Test find_blocking_move when Order is about to win in a row."""
        #Setup a board where Order is about to win in a row
        self.place_symbols([(0, 0), (0, 1), (0, 2), (0, 3)], 'X')
        blocking_move = self.controller.find_blocking_move()
        self.assertEqual(blocking_move, (0, 4, 'O'), "Should block Order's win in a row.")

    def test_blocking_column(self):
        """Test find_blocking_move when Order is about to win in a column."""
        #Setup a board where Order is about to win in a column
        self.place_symbols([(0, 0), (1, 0), (2, 0), (3, 0)], 'X')
        blocking_move = self.controller.find_blocking_move()
        self.assertEqual(blocking_move, (4, 0, 'O'), "Should block Order's win in a column.")
    
    def test_blocking_diagonal(self):
        """Test find_blocking_move when Order is about to win in a diagonal"""
        #Setup a board where Order is about to win in a diagonal
        self.place_symbols([(0,0),(1,1),(2,2),(3,3)], 'X')
        blocking_move = self.controller.find_blocking_move()
        self.assertEqual(blocking_move, (4,4, 'O'), "Should block Order's win in a diagonal")

    def test_no_blocking_needed(self):
        """Test find_blocking_move when no immediate blocking is needed."""
        # Setup a board where there is no immediate win for Order
        self.place_symbols([(0, 0), (1, 2), (2, 2)], 'X')
        blocking_move = self.controller.find_blocking_move()
        self.assertIsNone(blocking_move, "Should not find a blocking move when none is needed.")

if __name__ == '__main__':
    unittest.main()
