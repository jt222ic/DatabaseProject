import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY,
    title TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos2 (
    id INTEGER PRIMARY KEY,
    title TEXT
)
""")

#cursor.execute("""
#UPDATE todos SET title='Laga mat' WHERE id=1
#""")

cursor.execute("""
INSERT INTO todos2 (title) 
VALUES ('Test 4')
""")

cursor.execute("SELECT * FROM todos2")
print(cursor.fetchall())

conn.commit()

conn.close()




