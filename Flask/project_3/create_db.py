# this is sqlite



# install => pip install flask-sqlite3, by default it install if not then run this
# sqlite3 --version 
# or
# pip install flask flask-sqlalchemy

import sqlite3

conn = sqlite3.connect('site.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL     
)
''')

conn.commit()
conn.close()

# run this file, directly