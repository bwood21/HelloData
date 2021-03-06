"""Database to store people"""

import sqlite3

DB = sqlite3.connect(":memory:")
DB.execute("""CREATE TABLE IF NOT EXISTS PEOPLE(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            color TEXT
            )
            """)

PEOPLE = [
    ("Abe", "Blue"),
    ("John Purdue", "Black and Gold"),
    ("Daniel", "Blue"),
    ("Aaron", "Green"),
    ("Brandon", "Orange"),
]

DB.executemany("""
INSERT INTO PEOPLE(name, color)
VALUES(?, ?)
""", PEOPLE)

#print('\n'.join(DB.iterdump())) #quick n dirty : do not use

for person, color in DB.execute("SELECT name, color FROM people"):
    print(person + ", " + color)

person = DB.execute("SELECT name FROM people WHERE color='Blue'").fetchone()
print(person)

DB.execute("CREATE TABLE IF NOT EXISTS classes (id INTEGER PRIMARY KEY, person INTEGER NOT NULL, class_name TEXT, FOREIGN KEY (person) REFERENCES people(id))")

classes = [("John Purdue", ["SOC 100", "CS 407"])]
