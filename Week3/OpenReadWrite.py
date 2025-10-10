

class OpenReadWrite:

    def file_reader(self, file_path):
        with open(file_path, "r") as file:
            Content = file.read()
            print(f"list of the file is {Content} ")




#if __name__ == "__main__"
 file_path = ""C:\Users\jaish\Documents\Software Engineering\demo.txt.txt""
 file_read_writer = OpenReadWrite()