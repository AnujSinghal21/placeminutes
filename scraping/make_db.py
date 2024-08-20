import sqlite3

DB_PATH = 'data/data.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

profile_types = [
    'Core',
    'Software',
    'Finance',
    'Quant',
    'Analytics & Data Science',
    'Consulting',    
]

cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS openings (
        id INTEGER PRIMARY KEY,
        company_name TEXT NOT NULL,
        profile_type TEXT CHECK(profile_type IN {tuple(profile_types)}),
        profile TEXT,
        role TEXT,
        location TEXT,
        ctc REAL,
        eligibility TEXT,
        cp_cutoff REAL,
        salary_breakup TEXT,
        jd_extracted TEXT,
        performa_url TEXT,
        key_skills TEXT
    )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        roll INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        company_name TEXT,
        profile TEXT,
        gender CHAR CHECK(gender IN ('M', 'F')),
        opening_id INTEGER,
        cpi REAL,
        branch TEXT,
        home_state TEXT,
        blood_group TEXT CHECK(blood_group IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
        FOREIGN KEY (opening_id) REFERENCES openings(id)
    )
    """
)
conn.commit()

conn.close()

"""
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiYWFzX2RldmljZV9pZCI6IjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMCIsImJhYXNfZG9tYWluX2lkIjoiNjU4MTM5YTUxMzczOWI1NzZkMDg5NzRlIiwiZXhwIjoxNzI0MTU0NDI2LCJpYXQiOjE3MjQxNTI2MjYsImlzcyI6IjY2YzQ3YjMyMWY1ZjM3ZGE1NGUxZjZhZSIsImp0aSI6IjY2YzQ3YjMyMWY1ZjM3ZGE1NGUxZjZiMCIsInN0aXRjaF9kZXZJZCI6IjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMCIsInN0aXRjaF9kb21haW5JZCI6IjY1ODEzOWE1MTM3MzliNTc2ZDA4OTc0ZSIsInN1YiI6IjY2YzBmMGNmOGZkM2Q4NDE1OWQ4YWVkZSIsInR5cCI6ImFjY2VzcyJ9.PVTD6bl9daUW2W7GbxSDJlwceXGSxW3-5NT0OUrziOM",


"""