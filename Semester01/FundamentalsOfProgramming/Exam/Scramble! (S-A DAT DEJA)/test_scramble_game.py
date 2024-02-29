import unittest
from sentence_repository import SentenceRepository
from scramble_game_controller import ScrambleGameController

class TestSentenceRepository(unittest.TestCase):
    def setUp(self):
        self.repository = SentenceRepository("sentences.txt")

    def test_load_sentences(self):
        sentences = self.repository.load_sentences()
        self.assertTrue(len(sentences) > 0, "Should load sentences from file")

class TestScrambleGameController(unittest.TestCase):
    def setUp(self):
        self.repository = SentenceRepository("sentences.txt")
        self.controller = ScrambleGameController(self.repository)
        self.controller.start_new_game()

    def test_scramble_sentence(self):
        original = self.controller.original_sentence
        scrambled = self.controller.current_sentence
        
        if len(original.split()) > 1 or len(original) > 5:
            self.assertNotEqual(original, scrambled, "Scrambled sentence should differ from original")
        else:
            self.skipTest("Original sentence too short to guarantee scrambling.")


    def test_swap_letters(self):
        original = self.controller.original_sentence
        #Assuming the game starts as intended
        #Find two letters that can be swapped
        pos1, pos2 = 1, 2  #Example positions
        self.assertTrue(self.controller.swap_letters(pos1, pos2), "Swap should be successful")
        self.assertNotEqual(original, self.controller.get_current_sentence(), "Sentence should change after swap")

if __name__ == '__main__':
    unittest.main()
