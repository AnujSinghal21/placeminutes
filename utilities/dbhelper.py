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

def convert_to_json():
    net_data=[]
    df=pd.read_csv('./joined_data.csv')
    for i in range(len(df)):
        curr_data={}
        for key in df.columns:
            curr_data[key]=str(df[key][i])
        net_data.append(curr_data)
    
    with open('student_json','w') as json_file:
        json.dump(net_data,json_file,indent=4)
    
    return

def modify_csv():
    df=pd.read_csv('./joined_data.csv')
    genders=[]
    cpis=[]
    home_states=[]
    blood_groups=[]
    for i in range(len(df)):
        curr_stud_data=cursor.execute(f"select * from students where roll={df['Roll No.'][i]}").fetchall()
        if(len(curr_stud_data)==0):
            print(df['Name'][i] + ": "+str(df['Branch'][i]))
            genders.append('M/F')
            cpis.append(-1)
            home_states.append('India')
            blood_groups.append('Human Blood')
            continue
        curr_stud_data=list(curr_stud_data[0])
        genders.append(curr_stud_data[4])
        cpis.append(curr_stud_data[6])
        home_states.append(curr_stud_data[8])
        blood_groups.append(curr_stud_data[9])

    df['gender']=genders
    df['cpi']=cpis
    df['home_states']=home_states
    df['blood_groups']=blood_groups

    df.to_csv('new_data.csv',index=False)

modify_csv()
