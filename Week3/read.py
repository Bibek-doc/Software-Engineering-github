

class Read:
    def __init__(self, path):
        self.path = path

    def write(self, data):
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(data)
    
    def read(self): 
        with open(self.path, "r", encoding="utf-8") as file: 
            content = file.read()
            return content

def main():
    file_manipulation = Read("demo.txt.txt")
    
    # Print the content of the file before manipulation
    print(f"Content of the file before manipulation: {file_manipulation.read()}")
    
    # Write to the file
    file_manipulation.write("Hello, You missed it!")
    print("Data written to file successfully!")
    
    # Read from the file
    content = file_manipulation.read()
    print(f"Content read from file: {content}")

if __name__ == "__main__":
    main()