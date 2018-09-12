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
    ("Abe", "Blue")
    ("John Purdue", "Black and Gold")
    ("Daniel", "Blue")
    ("Aaron", "Green")
    ("Brandon", "Orange")
]
