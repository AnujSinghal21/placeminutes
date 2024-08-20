import pandas as pd
import google.generativeai as genai
import os
from bs4 import BeautifulSoup
import typing_extensions as typing
import sqlite3
import json
import time

class Details(typing.TypedDict):
  package_details: str
  ctc: int
  location: str
  description: str
  profile: str
  profile_type: str
  skills: str

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Using `response_mime_type` with `response_schema` requires a Gemini 1.5 Pro model
model = genai.GenerativeModel('gemini-1.5-flash',
                              # Set the `response_mime_type` to output JSON
                              # Pass the schema object to the `response_schema` field
                              generation_config={"response_mime_type": "application/json",
                                                 "response_schema": Details})

conn = sqlite3.connect('data/data.db')
cursor = conn.cursor()

def is_id_present(id):
    cursor.execute(
        f"""
        SELECT * FROM openings WHERE id = ?
        """,
        (id,)
    )
    return cursor.fetchone() is not None

prompt = "Extract the information about the package details (summarized in one line), with CTC (don't forget to convert LPA to integer and currency to INR, carefully look at all the data given), location as city/country (if not found both, give unknown/unknown ), job profile, job profile type (from the set of {'Core', 'Software','Finance','Quant','Analytics & Data Science','Consulting'} based on mainly the profile but can also look at the JD, research roles are generally core), a list of skills (keywords only, technical related, precisely specified, comma seperated) that will be helpful (choose top 4-5), and a 2-3 line description of job from the following Job description (that is relevant for those applying for the job, can remove company's background etc.)"
def store_opening_data(id, performa_data, opening_data):
    profile = performa_data['profile']
    role = performa_data['role']
    location = performa_data['tentative_job_location']
    jd = performa_data['job_description']
    eligibility = performa_data['eligibility']
    cost_to_company = performa_data['cost_to_company']
    package_details = performa_data['package_details']
    bond_details = performa_data['bond_details']
    soup = BeautifulSoup(jd, 'lxml')
    jd = soup.get_text(separator='\n')
    performa_url = f"https://spo-backend.vercel.app/details/2024/{id}"
    query_text = f"Cost to company: {cost_to_company}\nPackage details: {package_details}\nrole: {role}\nprofile: {profile}\nlocation: {location}\nBond details: {bond_details}\nDescription: {jd}\n"
    query = f"{prompt}\n[[{query_text}]]"
    try:            
        response = model.generate_content(query)
        response = json.loads(response.text)
    except Exception as e:
        print("Quota exceeded, waiting for 60 seconds")
        time.sleep(60)  
        print("Resuming")      
        response = model.generate_content(query)
        response = json.loads(response.text)
    if response['profile_type'] not in ['Core', 'Software', 'Finance', 'Quant', 'Analytics & Data Science', 'Consulting']:
        response['profile_type'] = 'Core'
    try:
        cursor.execute(
            f"""
            INSERT INTO openings (id, company_name, profile_type, profile, role, location, ctc, eligibility, cp_cutoff, salary_breakup, jd_extracted, performa_url, key_skills)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (id, opening_data['company_name'], response['profile_type'], profile, role, response['location'], response['ctc'], eligibility, opening_data['cpi_cutoff'], response['package_details'], response['description'], performa_url, response['skills'])
        )
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True

def store_student_data():
    return True

