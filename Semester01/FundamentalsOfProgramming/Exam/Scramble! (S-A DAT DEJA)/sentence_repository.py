import random

class SentenceRepository:
    """
    Purpose: Initializes the SentenceRepository instance by loading sentences from the specified file.
    Parameters: filename: A string representing the path to the file containing sentences.
    Effect: Calls load_sentences() to populate the sentences list with valid sentences from the file. 
    """
    
    def __init__(self, filename):
        self.filename = filename
        self.sentences = self.load_sentences()

    def load_sentences(self):
        """
        Purpose: Loads sentences from the file specified at initialization, ensuring they meet the game's criteria.
        Returns: A list of valid sentences loaded from the file.
        Effects: Populates the sentences attribute with the loaded sentences.
        """
        
        sentences = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    sentence = line.strip()
                    if self.validate_sentence(sentence):
                        sentences.append(sentence)
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")
        return sentences

    def validate_sentence(self, sentence):
        """
        Purpose: Validates a single sentence to ensure it meets specific criteria (e.g., length, word criteria).
        Parameters: sentence: A string representing the sentence to be validated.
        Returns: True if the sentence meets the validation criteria, False otherwise.
        """
        
        if not sentence:
            return False
        words = sentence.split()
        if not all(len(word) >= 2 for word in words):  #Each word must have at least 2 letters
            return False
        return True

    def get_random_sentence(self):
        """ 
        Purpose: Selects and returns a random sentence from the loaded sentences.
        Returns: A string representing a randomly chosen sentence from the repository.
        """

        if not self.sentences:
            return "No sentences available."
        return random.choice(self.sentences)
