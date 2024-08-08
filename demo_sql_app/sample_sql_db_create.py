import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')
conn.commit()

# Function to add a record
def add_record(name, age):
    c.execute('INSERT INTO people (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

# Function to view records
def view_records():
    c.execute('SELECT * FROM people')
    return c.fetchall()

# Function to delete a record by ID
def delete_record(record_id):
    c.execute('DELETE FROM people WHERE id = ?', (record_id,))
    conn.commit()

# Add some records
add_record('Alice', 30)
add_record('Bob', 25)

# View records
records = view_records()
print("Records in the database:")
for record in records:
    print(record)

# Delete a record (example: delete the record with ID 1)
#delete_record(1)

# View records after deletion
records = view_records()
print("\nRecords after deletion:")
for record in records:
    print(record)

# Close the database connection
conn.close()