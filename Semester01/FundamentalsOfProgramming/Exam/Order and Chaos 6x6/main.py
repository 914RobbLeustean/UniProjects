from BoardRepository import BoardRepository
from GameController import GameController
from GameUI import GameUI
import unittest

def run_tests():
    #Load test modules
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    #Adding tests to the test suite
    from testing_chaos import TestFindBlockingMove
    suite.addTests(loader.loadTestsFromTestCase(TestFindBlockingMove))

    #Running the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)



repository = BoardRepository()
controller = GameController(repository)
ui = GameUI(controller)
ui.start_game()
#run_tests()