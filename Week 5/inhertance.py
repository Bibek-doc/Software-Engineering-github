class Person:
    def __init__(self, name):
        self.set_name(name)   # use setter for validation

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name. It must be a non-empty string.")


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # calls Person’s constructor
        self.student_id = student_id
    
    def display_info(self):
        # Access parent's private __name via inherited getter
        return f"Name: {self.get_name()}, Student ID: {self.student_id}"


# Example usage
s1 = Student("Bibek", "S123")
print(s1.display_info())   # ✅ Works fine
s1.set_name("shaym bdr")        # ✅ Update name safely
print(s1.display_info())