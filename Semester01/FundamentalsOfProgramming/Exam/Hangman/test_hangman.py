import unittest
from sentence_repository import SentenceRepository
from hangman_game_controller import HangmanGameController

class TestSentenceRepository(unittest.TestCase):
    def setUp(self):
        self.test_sentences = ["Python este fun", "Maine merg la mare", "Testarea nu este cool"]
        self.filename = "test_sentences.txt"
        with open(self.filename, 'w') as file:
            for sentence in self.test_sentences:
                file.write(sentence + "\n")
        self.repository = SentenceRepository(self.filename)

    def test_load_sentences(self):
        #Test if sentences are loaded correctly
        loaded_sentences = self.repository.get_sentences()
        self.assertEqual(len(loaded_sentences), len(self.test_sentences))

    def test_add_sentence(self):
        #Test adding a valid sentence
        new_sentence = "Coudul meu merge"
        self.assertTrue(self.repository.add_sentence(new_sentence))
        self.assertIn(new_sentence, self.repository.get_sentences())

    

class TestHangmanGameController(unittest.TestCase):
    def setUp(self):
        self.sentences = ["Python este fun", "Testarea nu este cool"]
        self.controller = HangmanGameController(self.sentences)

    def test_select_sentence(self):
        self.controller.select_sentence()
        self.assertIn(self.controller.sentence, self.sentences)

    def test_guess_letter(self):
        self.controller.select_sentence()
        # Assuming the selected sentence is "Python is fun"
        self.controller.sentence = "PYTHON ESTE FUN"  #specific sentence for testing
        self.assertTrue(self.controller.guess_letter('P'))
        self.assertFalse(self.controller.guess_letter('Z'))
        self.assertIn('P', self.controller.guessed_letters)
        self.assertEqual(self.controller.hangman, 'H' if 'Z' in self.controller.guessed_letters else "")

    def test_win_lose_conditions(self):
        self.controller.select_sentence()
        self.controller.sentence = "CAT"
        self.controller.guess_letter('C')
        self.controller.guess_letter('A')
        self.controller.guess_letter('T')
        self.assertTrue(self.controller.is_win())
        self.assertFalse(self.controller.is_lose())


if __name__ == '__main__':
    unittest.main()
