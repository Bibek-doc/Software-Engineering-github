class StringManipulator:
    def __init__(self):
        self.sentence = ("")

    def get_sentence(self): 
        self.sentence = input("Can you plaese enter the text")

    def count_words(self):
        if not self.sentence:
            return 0
        
        words = self.sentence.split()
        return len(words)
    
    def display_result(self):
        word_count = self.count_words()
        print(f"The Number of the word in the sentence: {word_count}")

#if__name__ == "__main__"
    
#analyzer = SentenceAnalyzer()





    

