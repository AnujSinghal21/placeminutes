import pandas as pd
import json
import sqlite3

class student:
    def __init__(self, name = "", roll_no = 0, cpi = 0.0, branch = "", state = "", company = None, profile = None, gender = "M", blood_group = "O+"):
        self.name = name
        self.roll_no = roll_no
        self.cpi = cpi
        self.branch = branch
        self.state = state
        self.company = company
        self.profile = profile
        self.gender = gender
        self.blood_group = blood_group
    
    def save(self, cursor):
        cursor.execute(
            """
            INSERT INTO students (roll, name, company_name, profile, gender, cpi, branch, home_state, blood_group)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (self.roll_no, self.name, self.company, self.profile, self.gender, self.cpi, self.branch, self.state, self.blood_group)
        )



stats_data = json.load(open('data/stats_data.json'))
students_data = json.load(open('data/students_data.json'))
students_data = students_data['documents']
cpi_data = pd.read_excel('data/cpi.xlsx')

students = {}

def name_case(fullname):
    parts = [name.capitalize() for name in fullname.split(' ')]
    name = ''
    for part in parts:
        if len(part) != 0:
            name += part + ' '
    return name.strip()

for cpi_data in cpi_data.iterrows():
    roll_no = int(cpi_data[1]['Roll Number'])
    spi_cols = ['2020-21 1', '2020-21 2', '2021-22 1', '2021-22 2', '2022-23 1', '2022-23 2']
    spis = [float(cpi_data[1][col]) for col in spi_cols]
    total = 0.0
    count = 0
    for spi in spis:
        if not pd.isna(spi):
            total += spi
            count += 1
    if count == 0:
        cpi = 0.0
    else:
        cpi = total / count
    students[roll_no] = student(roll_no=roll_no, name = name_case(cpi_data[1]['Name']),cpi=cpi)

for stat in stats_data:
    roll_no = int(stat['Roll No.'])
    if roll_no in students:
        students[roll_no].company = stat['Company Name']
        students[roll_no].profile = stat['Profile']
        students[roll_no].branch = stat['Branch']
    else:
        students[roll_no] = student(roll_no=roll_no, name = name_case(stat['Name']),company=stat['Company Name'], profile=stat['Profile'], branch=stat['Branch'])

for student_data in students_data:
    try:
        roll_no = int(student_data['i'])
    except:
        continue

    if roll_no in students:
        students[roll_no].state = student_data['a'].split(',')[-1].strip().upper()
        if student_data['b'] not in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']:
            students[roll_no].blood_group = 'O+'
        else:
            students[roll_no].blood_group = student_data['b']


conn = sqlite3.connect('data/data.db')
cursor = conn.cursor()
for student in students.values():
    student.save(cursor)

conn.commit()
conn.close()