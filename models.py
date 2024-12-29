# models.py

import sqlite3

DATABASE = 'example.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  age INTEGER)''')
    conn.commit()
    conn.close()

def insert_user(name, email, age):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

def update_user(user_id, name, email, age):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?", (name, email, age, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def clear_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # List of tables to be cleared
    tables = ['users']  # Add your table names here

    # Delete all rows from each table
    for table in tables:
        cursor.execute(f"DELETE FROM {table}")

    # Commit changes and close connection
    conn.commit()
    conn.close()





