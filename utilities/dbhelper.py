import sqlite3
import pandas as pd
import json

DB_PATH = '../data.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def get_json_files():
    df=pd.DataFrame(cursor.execute("SELECT * from openings"))
    df.columns=['id','name','profile','role','industry','location','ctc','eligibility','cpi','ctc desc','description','link','skills']
    json_data=[]

    for i in range(len(df)):
        curr={}
        for key in df.columns:
            curr[key]=df[key][i]
        json_data.append(curr)
    
    with open('../companies.json','w') as json_file:
        json.dump(json_data,json_file)
    
    return

get_json_files()