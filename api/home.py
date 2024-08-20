import sqlite3
import json
import pandas as pd

DB_PATH = '../data.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def get_company_list():
    df=pd.DataFrame(cursor.execute("SELECT * from openings"))
    df.columns=['id','name','profile','role','industry','location','ctc','eligibility','cpi','ctc desc','description','link','skills']
    required_data=[]
    json_data=[]

    for i in range(len(df)):
        curr={}
        for key in df.columns:
            curr[key]=df[key][i]
        json_data.append(curr)
    
    return json_data

print(get_company_list()[0])