import random
from sentence_repository import SentenceRepository

class HangmanGameController:
    """
    Purpose: Initializes the HangmanGameController instance.
    Parameters: sentences: A list of strings representing the sentences available for the game.
    Behavior: Sets up the game with an empty state, ready to start a new game when required. 
    """
    
    def __init__(self, sentences):
        self.sentences = sentences
        self.sentence = ""
        self.guessed_letters = set(" ")
        self.hangman = ""
        self.max_errors = len("HANGMAN")

    def select_sentence(self):
        """
        Purpose: Randomly selects a sentence from the list provided at initialization and prepares the game state for a new round.
        Behavior: Identifies the first and last letters of each word in the selected sentence and reveals them, along with any appearances of those letters in the sentence. 
        """
        
        if not self.sentences:
            raise ValueError("No valid sentences available.")
        self.sentence = random.choice(self.sentences).upper()
        #Reset guessed letters for a new game
        self.guessed_letters = set(" ")
        #Identify and reveal first and last letters of each word
        for word in self.sentence.split():
            if len(word) > 1:  #Check to avoid single-letter words adding the same letter twice
                self.guessed_letters.add(word[0])
                self.guessed_letters.add(word[-1])
            else:
                #For single letter words just add the letter
                self.guessed_letters.add(word)

    def guess_letter(self, letter):
        """
        Purpose: Processes a user's guess.
        Parameters: letter: A single character string representing the user's guess.
        Returns: True if the letter is in the sentence, False otherwise.
        Behavior: Updates the game's state based on the guess, including adding the letter to the set of guessed letters and updating the hangman state if the guess is incorrect.
 
        """
        
        if letter in self.sentence:
            self.guessed_letters.add(letter)
            return True
        else:
            self.hangman += "HANGMAN"[len(self.hangman)]
            return False

    def is_win(self):
        """
        Purpose: Checks if the user has won the game.
        Returns: True if the user has successfully guessed all letters in the sentence, False otherwise. 
        """
        
        return all(letter in self.guessed_letters or letter == " " for letter in self.sentence)

    def is_lose(self):
        """
        Purpose: Checks if the user has lost the game.
        Returns: True if the hangman word is fully revealed (indicating the user has made too many incorrect guesses), False otherwise. 
        """
        return len(self.hangman) == self.max_errors

    def get_display_sentence(self):
        """
        Purpose: Provides the current state of the sentence for display to the user.
        Returns: A string representing the sentence with unguessed letters replaced by underscores and spaces properly shown. 
        """
        return "".join([letter if letter in self.guessed_letters else "_" for letter in self.sentence])
