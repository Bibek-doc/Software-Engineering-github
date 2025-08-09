class StringManipulator:

    def find_character(self,text, char):
        return text.find(char)

    def get_length(self,text):
        """Return the length of the string."""
        return len(text)

    def to_lowercase(self,text):
        """Return the string in uppercase."""
        return text.lower()



name = StringManipulator()

result = name.find_character("test",'t')
print("Index of 'x':", result)

length = name.get_length("hippoppatamas")
print("Length of string:", length) 

lowercase_text = name.to_lowercase("ENGLISH")
print("Lowercase string:", lowercase_text) 
