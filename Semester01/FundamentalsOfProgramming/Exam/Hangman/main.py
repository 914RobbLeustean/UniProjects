import unittest
from hangman_game_ui import HangmanGameUI
from sentence_repository import SentenceRepository
from hangman_game_controller import HangmanGameController

def run_tests():
    #loading test modules
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    #adding tests
    from test_hangman import TestSentenceRepository, TestHangmanGameController
    suite.addTests(loader.loadTestsFromTestCase(TestSentenceRepository))
    suite.addTests(loader.loadTestsFromTestCase(TestHangmanGameController))

    #running the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

#Load sentences and start the game
repo = SentenceRepository("sentences.txt")
controller = HangmanGameController(repo.get_sentences())
ui = HangmanGameUI(controller, repo)

ui.play()
#run_tests()
