# setup vvvvv
import sqlite3 # import library so sqlite databases can be used

DB_NAME = "school.db" # store name of database file to be used

conn = sqlite3.connect(DB_NAME) #connect to db file
# creates one if nonexistent

cur = conn.cursor() # create cursor object

# reminder: cursor is used to run sql commands
#           and fetch results

print("Database connected successfully to:", DB_NAME)
# print message to show connection worked

# setup ^^^


# creates table called "Student" using an sql command
# IF NOT EXISTS prevents an error if table already exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        studentID INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        yearGroup INTEGER NOT NULL
    );
""")

conn.commit() # save changes to database file

# confirmation message
print("Student table created (if it did not already exist).")



# create list of student records
# each tuple matches columns in Student table (see lines 22-29)
students = [
    (1, "Aoife", "Murphy", 5),
    (2, "Cian", "O'Brien", 5),
    (3, "Niamh", "Kelly", 6),
    (4, "Dara", "Byrne", 6),
]

# insert multiple rows using executemany
# INSERT OR IGNORE means:
    # insert the row if primary key inexistent
    # ignore if primary key exists already (would cause errors)
cur.executemany("""
    INSERT OR IGNORE INTO Student
    VALUES (?, ?, ?, ?);
""", students)

# save changes
conn.commit()

#confirmation message
print("Students inserted (duplicates ignored)")

# query 1 - select all columns and all rows from Student
cur.execute("SELECT * FROM Student;")

# fetchall() gets all rows returned by query
rows = cur.fetchall()


# print results (nice)
print("All students:", rows)



# query 2: select only first and last names
cur.execute("SELECT firstName, lastName FROM Student;")
print("Names only:", cur.fetchall())

# query 3: filter using WHERE
cur.execute("SELECT * FROM Student WHERE yearGroup = 6;")
print("6th years:", cur.fetchall())

# query 4: sort using ORDER BY
cur.execute("SELECT * FROM Student ORDER BY lastName ASC;")
print("Sorted by last name:", cur.fetchall())
