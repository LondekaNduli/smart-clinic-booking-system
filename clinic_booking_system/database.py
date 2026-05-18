import sqlite3

# Connect database
conn = sqlite3.connect("clinic.db", check_same_thread=False)
cursor = conn.cursor()

# Create Doctors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialty TEXT
)
""")

# Create Patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

# Create Appointments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    doctor_name TEXT,
    date TEXT,
    time TEXT,
    status TEXT
)
""")

conn.commit()