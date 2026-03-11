import sqlite3

DB_NAME = "school.db"
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

cur.execute("PRAGMA foreign_keys = ON;")
print("Connected to database and foreign keys enabled.")

def save():
    conn.commit()
    print("Saved to database.")

# Drop child tables first
cur.execute("DROP TABLE IF EXISTS Attendance;")
# WAS NEEDED because Attendance references Student

cur.execute("DROP TABLE IF EXISTS StudentSubject;")
# WAS NEEDED because StudentSubject references Student

cur.execute("DROP TABLE IF EXISTS Subject;")
# Drop this before rebuilding, to keep the database clean

cur.execute("DROP TABLE IF EXISTS Student;")
# Student must be dropped after child tables

save()

# Create Student table
cur.execute("""
    CREATE TABLE Student (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        year_group INTEGER NOT NULL
    );
""")
save()
print("Student table created.")

students = [
    (1, "Aoife", "Murphy", 5),
    (2, "Cian", "O'Brien", 5),
    (3, "Niamh", "Kelly", 6),
    (4, "Dara", "Byrne", 6)
]

cur.executemany("""
    INSERT INTO Student(student_id, first_name, last_name, year_group)
    VALUES (?, ?, ?, ?);
""", students)
save()
print("Students inserted.")

cur.execute("SELECT * FROM Student;")
print("All students:")
for row in cur.fetchall():
    print(row)

cur.execute("SELECT first_name, last_name FROM Student;")
print("Names only:")
for row in cur.fetchall():
    print(row)

conn.close()
print("Database connection closed.")