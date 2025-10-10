# class Student:
#     def __init__(self, name, age):
#         self.name = name       # public
#         self._age = age        # protected
#         self.__grade = 'T'     # private

#     # Getter for grade (already there)
#     def get_grade(self):
#         return self.__grade
    
#     # New method using the private attribute
#     def promote_student(self):
#         if self.__grade == 'A':
#             return f"{self.name} is an excellent student!"
#         elif self.__grade == 'Z':
#             return f"{self.name} is a good student."
#         else:
#             return f"{self.name} needs improvement."
        
#     def updated_info(self):
#         self.__grade = "A+"   # change grade to A+
#         return f"{self.name}'s grade will be upgraded to {self.__grade}"


# # New class demonstrating public and protected
# class GraduateStudent(Student):
#     def __init__(self, name, age, thesis_topic):
#         super().__init__(name, age)   # inherit from Student
#         self.thesis_topic = thesis_topic

#     def display_info(self):
#         # Access public attribute directly
#         info = f"Name: {self.name}, "
        
#         # Access protected attribute (allowed but discouraged)
#         info += f"Age: {self._age}, "
        
#         # Can't directly access __grade (private), must use getter
#         info += f"Grade: {self.get_grade()}, "
        
#         info += f"Thesis Topic: {self.thesis_topic}"
#         return info


# # Example usage
# s = Student('Bibek', 1222222222)
# print(s.name)           # accessible (public)
# print(s._age)          #  accessible but discouraged (protected)
# print(s.__grade())   #  correct way (private)
# print(s.promote_student()) # uses private attribute inside class

# print(s.updated_info())     # updates grade to A+
# # print(s.get_grade())   

# g = GraduateStudent('Bibek', 22, "Artificial Intelligence")
# print(g.display_info()) 

class employee:
    def __init__(self, name, age, salary):
        self.name = name       # public​
        self._age = age        # protected​
        self.__salary = salary  # private​

    def get_salary(self):
        return self.__salary
    
    def increase_salary(self, amount):
        self.__salary += amount

class Student:
    def __init__(self, name, age):
        self.name = name       # public​
        self._age = age        # protected​
        self.__grade = 'A'     # private​

    def get_grade(self):
        return self.__grade
    
    def reduce_grade(self):
        self.__grade = 'B'

    def Update_grade(self):
        self.__grade = 'A+'

def main():
    s = Student('Ali', 20)
    print(s.name)         # accessible​
    print(s._age)         # discouraged​
    print(s.get_grade())  # correct way​

    print("Reducing grade...")
    s.reduce_grade()
    print(s.get_grade())  # correct way​

    print("Increasing grade...")
    s.Update_grade()
    print(s.get_grade())  # correct way​

    print("")
    e = employee('John', 30, 50000)
    print(e.name)          # accessible​
    e.name = 'Doe'  # allowed​
    print (e.name)

    print(e.get_salary())          # accessible​
    e.__salary = 60000  # won't change the actual salary​
    print(e.get_salary()) 
    e.increase_salary(10000)
    print(e.get_salary())


if __name__ == "__main__":
    main()