import sqlite3
import pandas as pd
import numpy as np
import json

DB_PATH = '../data.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def convert_to_csv():
    df=pd.DataFrame(cursor.execute("SELECT * from openings"))
    df.columns=['id','name','profile','role','industry','location','ctc','eligibility','cpi','ctc desc','description','link','skills']
    df.to_csv('cleaned_data.csv',index=False)
    return

def get_json_files():
    df=pd.DataFrame(cursor.execute("SELECT * from openings"))
    df.columns=['id','name','profile','role','industry','location','ctc','eligibility','cpi','ctc desc','description','link','skills']
    json_data=[]
    reqcols=['id','name','profile','role','location','ctc','eligibility','cpi']

    for i in range(len(df)):
        curr={}
        for key in reqcols:
            value=df[key][i]
            curr[key]=str(value)
        json_data.append(curr)
    
    with open('../companies.json','w') as json_file:
        json.dump(json_data,json_file, indent=4)
    
    return

convert_to_csv()