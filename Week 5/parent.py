class classroom:
    def __init__(self, name, address, age, ID):
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID
    
    def display_info(self):
        return f"Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.ID}"

class student(classroom):
    def __init__(self, name, address, age, ID, academic_record):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record

    def display_info(self):
        return super().display_info() + f", Academic Record: {self.academic_record}"
    
class academic(classroom):
    def __init__(self, name, address, age, ID, tax_code, salary):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.salary = salary

    def show_details(self):
        return super().show_details() + f", Tax Code: {self.tax_code}, Salary: {self.salary}"
    
class generalStaff(classroom):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def show_details(self):
        return super().show_details() + f", Tax Code: {self.tax_code}, Pay Rate: {self.pay_rate}"

student1 = student("Bibek", "City Road", 20, "B1", "A+")
academic1 = academic("Mr.Hari", "Symond Street", 45, "H2", "TX123",20000)
staff1 = generalStaff("Ganesh", "21 Grafton", 35, "G2", "TX789", 28.50)

print(student1.display_info())
print(academic1.display_info())
print(staff1.display_info())