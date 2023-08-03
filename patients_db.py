import sqlite3

conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

# Create a table for patient details
cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    dob TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phnumber TEXT NOT NULL,
                    id_number TEXT NOT NULL,
                    address TEXT NOT NULL,
                    county TEXT NOT NULL,
                    sub_county TEXT NOT NULL,
                    gender TEXT NOT NULL,
                    marital_status TEXT NOT NULL,
                    next_of_kin_name TEXT NOT NULL,
                    next_of_kin_dob TEXT NOT NULL,
                    next_of_kin_id_number TEXT NOT NULL,
                    next_of_kin_gender TEXT NOT NULL,
                    next_of_kin_relationship TEXT NOT NULL,
                    next_of_kin_phnumber TEXT NOT NULL
                )''')

conn.commit()
conn.close()
