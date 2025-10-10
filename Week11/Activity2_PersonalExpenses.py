#WeeK11-Activity2- Develop a program using Object-Oriented Programming (OOP)  and Unit-testing to create a simple Personal Expense Tracker.
# The system should include at least two main functionalities:
# Add Expense : Allow the user to add a new expense with a description and an amount.
# Calculate Total Expense :  Compute and display the total amount of all recorded expenses.

import unittest 

class expense:
    def __init__(self):
        self.expense = []
        

    def add_expense(self, description, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.expense.append({"description": description, "amount": amount})
        return True

    def calculate_total_expense(self):
        total = sum(expense["amount"] for expense in self.expense)
        return total

    def show_expense(self):
        for exp in self.expense:
            print(f"{exp['description']}: ${exp['amount']}")
            

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = expense()

    def test_add_expense(self):
        # Add valid expense
        result = self.tracker.add_expense("Lunch", 15.50)
        self.assertTrue(result)
        self.assertEqual(len(self.tracker.expense), 1)
        self.assertEqual(self.tracker.expense[0]["description"], "Lunch")
        self.assertEqual(self.tracker.expense[0]["amount"], 15.50)

        # Add invalid expense
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Invalid", -10)

    def test_calculate_total_expense(self):
        self.tracker.add_expense("Lunch", 15.50)
        self.tracker.add_expense("Transport", 10.00)
        self.tracker.add_expense("Snacks", 4.50)
        total = self.tracker.calculate_total_expense()
        self.assertEqual(total, 30.00)

if __name__ == '__main__':
    unittest.main()

            
            



