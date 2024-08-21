import sqlite3
import json
import pandas as pd

DB_PATH = '../data.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def get_company_data():
    
    with open('companies.json','r') as json_file:
        json_data=json.load(json_file)
    return json_data

def get_student_data():
    with open('students.json','r') as json_file:
        json_data=json.load(json_file)
    return json_data

