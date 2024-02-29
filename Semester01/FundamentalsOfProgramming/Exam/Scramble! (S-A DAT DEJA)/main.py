import unittest
from sentence_repository import SentenceRepository
from scramble_game_controller import ScrambleGameController
from scramble_game_ui import ScrambleGameUI

def run_tests():
    #Load test modules
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    #Adding tests to the test suite
    from test_scramble_game import TestSentenceRepository, TestScrambleGameController
    suite.addTests(loader.loadTestsFromTestCase(TestSentenceRepository))
    suite.addTests(loader.loadTestsFromTestCase(TestScrambleGameController))

    # Runing the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
    
repository = SentenceRepository("sentences.txt")
controller = ScrambleGameController(repository)
ui = ScrambleGameUI(controller)
#ui.start_game()
run_tests()   