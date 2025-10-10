# # to calculate the given which number is greater.


# a= 9
# b = 1

# if a > b:
#     print('a is greater')

# elif b > a:
#     print('b is greater')
# else:
#     print('they are equal')


# >> Print the number in the list

# numbers = [1,2,3,4,5,6]

# for num in numbers:
#     print(num)

#     print(numbers[2])


n = "Nabina"
b = "Bibek"

if n < b:
    print('Nabina is very good one')

elif n > b:
    print(' Bibek is very energetic one')

else:
    print('They both are good one')
 
 
#  import sqlite3
# def init_db():
#     conn = sqlite3.connect("car_rental.db")
#     c = conn.cursor()
#     # create users table if not exists
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             username TEXT PRIMARY KEY,
#             password TEXT NOT NULL,
#             role TEXT NOT NULL
#         )
#     """)
#     # insert default admin if not exists
#     c.execute("SELECT * FROM users WHERE username = ?", ("admin",))
#     if not c.fetchone():
#         c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
#                   ("admin", "admin123", "admin"))
#     conn.commit()
#     conn.close()
# def register():
#     print("\n--- User Registration ---")
#     username = input("Enter username: ")
#     conn = sqlite3.connect("car_rental.db")
#     c = conn.cursor()

#     c.execute("SELECT * FROM users WHERE username = ?", (username,))
#     if c.fetchone():
#         print("❌ Username already exists.")
#         conn.close()
#         return

#     password = input("Enter password: ")
#     c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
#               (username, password, "customer"))
#     conn.commit()
#     conn.close()
#     print(f"✅ User '{username}' registered successfully!")
# def login():
#     print("\n--- User Login ---")
#     username = input("Username: ")
#     password = input("Password: ")

#     conn = sqlite3.connect("car_rental.db")
#     c = conn.cursor()
#     c.execute("SELECT username, password, role FROM users WHERE username = ?", (username,))
#     user = c.fetchone()
#     conn.close()

#     if user and user[1] == password:
#         print(f"✅ Welcome {username} ({user[2]})!")
#         if user[2] == "admin":
#             admin_menu(username)
#         else:
#             customer_menu(username)
#     else:
#         print("❌ Invalid login.")
# def main():
#     init_db()  # make sure DB and default admin exist
#     while True:
#         print("\n=== Car Rental System ===")
#         print("1. Register\n2. Login\n3. Exit")
#         option = input("Enter choice: ")
#         if option == "1":
#             register()
#         elif option == "2":
#             login()
#         elif option == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option.")
