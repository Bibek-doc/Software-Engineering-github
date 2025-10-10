# Week 2- Activity-6: Develop the basic HR project using OO.

class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        """To displays the employee's information."""
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Job Title: {self.job_title}")
        print("-" * 30)
    
    def display1_info(self):
        """To displays the employee's information."""
        print(f"Name: {self.name }")
        print(f"Salary: ${self.salary}")
        print(f"Job Title: {self.job_title}")
        print("-" * 30)

    def give_raise(self, amount):
        """It increases the employee's salary by the given amount."""
        self.salary += amount
        print(f"{self.name} Salary after increment ${amount}!")
        print(f"New Salary of Bibek: ${self.salary}")
        print(f"New salary of Good Man: {self.salary}")
        print("-" * 30)


def main():
    #  To create at least two Employee objects with different data
    employee1 = Employee("Bibek Jaishi", 4500.25, "Developer")
    employee2 = Employee("Good Man", 45000, "Coordinator")

    # Display each employee's details
    print("Display Employee Information:")
    employee1.display_info()
    employee2.display1_info()

    # Display updated salary
    employee1.give_raise(5000)
    employee2.give_raise(4200.39)


# It call the main function.
if __name__ == "__main__":
    main()
