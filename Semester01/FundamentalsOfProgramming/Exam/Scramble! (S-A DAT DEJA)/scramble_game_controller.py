import random
from sentence_repository import SentenceRepository

class ScrambleGameController:
    """
    Purpose: Initializes the ScrambleGameController with a reference to a SentenceRepository instance.
    Parameters: repository: An instance of SentenceRepository used to access the sentences. 
    """
    def __init__(self, repository: SentenceRepository):
        self.repository = repository
        self.original_sentence = ""
        self.current_sentence = ""
        self.score = 0
        

    def start_new_game(self):
        """
        Purpose: Starts a new game session by selecting a random sentence and scrambling it.
        Effects: Sets original_sentence, current_sentence, and initializes score based on the length of the non-space characters in the scrambled sentence. 
        """
        
        self.original_sentence = self.repository.get_random_sentence()
        self.current_sentence = self.scramble_sentence(self.original_sentence)
        self.score = len([ch for ch in self.current_sentence if ch != ' '])  #Score equals the number of letters

    def scramble_sentence(self, sentence):
        """
        Purpose: Scrambles the given sentence by randomly shuffling the letters in each word, except for the first and last letters.
        Parameters: sentence: A string representing the sentence to scramble.
        Returns: A scrambled version of the input sentence as a string. 
        """
        
        words = sentence.split()
        scrambled_words = [self.scramble_word(word) for word in words]
        return ' '.join(scrambled_words)

    def scramble_word(self, word):
        """
        Purpose: Helper function to scramble a single word, used by scramble_sentence.
        Parameters: word: A string representing the word to scramble.
        Returns: A scrambled version of the word as a string. 
        """
        
        if len(word) > 2:
            middle_chars = list(word[1:-1])
            random.shuffle(middle_chars)
            return word[0] + ''.join(middle_chars) + word[-1]
        return word

    def swap_letters(self, pos1, pos2):
        """
        Purpose: Swaps two letters in the current scrambled sentence based on their positions.
        Parameters: pos1: An integer representing the position of the first letter to swap.
                     pos2: An integer representing the position of the second letter to swap.
        Returns: True if the swap was successful, False otherwise (e.g, invalid positions, trying to swap the first and last letter of any word).
        Effects: Modifies current_sentence to reflect the swap and decreases score by 1. 
        """
        
        #Convert user positions (ignoring spaces) to actual indexes in the sentence
        actual_pos1, actual_pos2 = -1, -1
        visible_index = 0  #Index in the sentence ignoring spaces
        
        for i, char in enumerate(self.current_sentence):
            if char != ' ':
                if visible_index == pos1:
                    actual_pos1 = i
                if visible_index == pos2:
                    actual_pos2 = i
                visible_index += 1

        #Check if either position did not find a match or trying to swap the same position
        if actual_pos1 == -1 or actual_pos2 == -1 or actual_pos1 == actual_pos2:
            return False
        
        words = self.current_sentence.split()
        word_boundaries = [(word[0], word[-1]) for word in words]
        for start, end in word_boundaries:
            if (self.current_sentence[actual_pos1] == start and self.current_sentence[actual_pos2] == end) or (self.current_sentence[actual_pos2] == start and self.current_sentence[actual_pos1] == end):
                print("Invalid swap: Cannot swap the first letter with the last letter of a word.")
                return False
        
        #Perform the swap using the actual positions
        sentence_as_list = list(self.current_sentence)
        sentence_as_list[actual_pos1], sentence_as_list[actual_pos2] = sentence_as_list[actual_pos2], sentence_as_list[actual_pos1]
        self.current_sentence = ''.join(sentence_as_list)
        self.score -= 1  #Decrease score by 1 for each swap
        return True


    def check_victory(self):
        """
        Purpose: Checks if the current state of the scrambled sentence matches the original unscrambled sentence.
        Returns: True if the player has successfully unscrambled the sentence, False otherwise. 
        """
        
        return self.original_sentence == self.current_sentence

    def get_current_sentence(self):
        """
        Purpose: Retrieves the current state of the scrambled sentence.
        Returns: The current scrambled sentence as a string.
        """
        
        return self.current_sentence

    def get_score(self):
        """
        Purpose: Retrieves the current score of the player.
        Returns: The current score as an integer.  
        """
        
        return self.score
