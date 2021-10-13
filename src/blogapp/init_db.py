import os
import sqlite3

module_dir = os.path.dirname(os.path.abspath(__file__))
connection = sqlite3.connect(module_dir + "/database.db")

with open(module_dir + "/schema.sql") as fsql:
    connection.executescript(fsql.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (
    'First Post', 'Content for the first post'))

cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (
    'Second Post', 'Content for the second post'))

connection.commit()
connection.close()
