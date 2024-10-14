import sqlite3

def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    
    # Correct SQL query to create the employee table
    cur.execute('''CREATE TABLE IF NOT EXISTS employee (
                    eid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    gender TEXT,
                    contact TEXT,
                    dob TEXT,
                    doj TEXT,
                    pass TEXT,
                    utype TEXT,
                    address TEXT,
                    salary TEXT
                )''')
    
    con.commit()
    con.close()

create_db()
