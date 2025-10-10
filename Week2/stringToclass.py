class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)

    def get_length(self):
        return len(self.text)

    def to_lowercase(self):
        return self.text.lower()


def object():
    name = StringManipulator("CHARACTER")

    result = name.find_character('C')
    print("Index of 'x':", result)

    length = name.get_length()
    print("Length of string:", length) 

    lowercase_text = name.to_lowercase()
    print("Uppercase string:", lowercase_text) 


if __name__ == "__main__":
    object()
