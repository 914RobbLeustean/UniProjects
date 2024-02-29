class SentenceRepository:
    """
    Purpose: Initializes the SentenceRepository instance.
    Parameters: filename: A string representing the path to the file containing the sentences.
    Behavior: Loads sentences from the specified file into memory, ensuring they meet the game's criteria (no duplicates, each word has at least 3 letters). 
    """
    
    def __init__(self, filename):
        self.filename = filename
        self.sentences = self.load_sentences()

    def add_sentence(self, sentence):
        """
        Purpose: Adds a new sentence to the repository and the backing file, if it meets the game's criteria.
        Parameters: sentence: A string representing the sentence to be added.
        Returns: True if the sentence was successfully added, False otherwise (e.g., if it doesn't meet criteria or is a duplicate) 
        """
        
        #Validate sentence length and word length
        if not sentence or not all(len(word) >= 3 for word in sentence.split()):
            print("Invalid sentence. Each word must have at least 3 letters.")
            return False
        #Check for duplicates
        if sentence in self.sentences:
            print("This sentence already exists.")
            return False
        #Add the sentence
        self.sentences.append(sentence)
        #Write new sentence in the text-file (optional)
        with open(self.filename, 'a') as file:
            file.write(f"{sentence}\n")
        return True
    
    def load_sentences(self):
        """
        Purpose: Loads and validates sentences from the file specified at initialization.
        Returns: A list of valid sentences.
        """
        
        sentences = set()
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    sentence = line.strip()
                    if sentence and all(len(word) >= 3 for word in sentence.split()):
                        sentences.add(sentence)
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")
        return list(sentences)

    def get_sentences(self):
        """
        Purpose: Provides access to the loaded sentences.
        Returns: A list of sentences currently loaded in the repository. 
        """
        
        return self.sentences
