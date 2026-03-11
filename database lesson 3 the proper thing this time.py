import sqlite3

DB_NAME = "school.db"
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

cur.execute("PRAGMA foreign_keys = ON;")
# turn on foreign key enforcement

print("Connected to database, foreign keys enabled")

# create attendance table if nonexistent
cur.execute("""
    CREATE TABLE IF NOT EXISTS Attendance (
        attendance_id INTEGER PRIMARY KEY,
        student_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('Present', 'Absent')),
        FOREIGN KEY (student_id) REFERENCES Student(student_id)
        );
""")

conn.commit() # save table to database file

print("Attendance table created (if not existing already)")


# shit gets real from here on

# create list of attendance records to insert
# format: (attendance_id, student_id, date, status)

attendance_records = [
    (1, 2, "2026-03-01", "Present"), # student_id 2 must exist in Student table
    (2, 2, "2026-03-02", "Absent"),
    (3, 3, "2026-03-01", "Present")
]

# try to insert multiple rows using executemany
try:
    cur.executemany("""
        INSERT OR IGNORE INTO Attendance(attendance_id, student_id, date, status)
        VALUES (?, ?, ?, ?);
    """, attendance_records)

    conn.commit()
    print("Attendance records inserted IT WORKED")
except sqlite3.OperationalError as OE:
    print("something went wrong.", OE)