import sqlite3

conn =sqlite3.connect("app.db")
cursor = conn.cursor()

# Create 'users' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

# Create 'orders' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product TEXT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")


# Insert sample users
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))

# Insert sample orders
cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (1, "Laptop", 1200.50))
cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (1, "Mouse", 25.00))
cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (2, "Keyboard", 45.00))

conn.commit()
conn.close()