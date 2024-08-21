import pandas as pd
import numpy as np

companies=pd.read_csv('cleaned_data.csv')
#companies.reset_index()
students=pd.read_csv('studentwise_stats.csv')
#students.reset_index()

student_ctcs=[]
student_company_map=[]
for i in range(len(students)):
    possible_companies=companies[companies['name']==students['Company Name'][i]]
    possible_companies=possible_companies.reset_index()
    if(len(possible_companies)==1):
        student_ctcs.append(possible_companies['ctc'][0])
        student_company_map.append(possible_companies['id'][0])
    else:
        found=False

        #print(possible_companies.head())

        for j in range(len(possible_companies)):
            if(possible_companies['role'][j]==students['Profile'][i]):
                student_ctcs.append(possible_companies['ctc'][j])
                student_company_map.append(possible_companies['id'][j])
                found=True
                break
        
        if not found:
            if(students['Profile'][i]=="PIO-PPO"):
                student_ctcs.append(0)
                student_company_map.append(-1) 
            elif(len(possible_companies)==0):
                student_ctcs.append(1200000)
                student_company_map.append(-1) 
                print("Anomaly found for company: "+str(students['Company Name'][i]))
            else:
                net_sum=0
                count=0
                for j in range(len(possible_companies)):
                    net_sum+=float(possible_companies['ctc'][j])
                    count+=1
                student_ctcs.append(net_sum/count)
                student_company_map.append(possible_companies['id'][0])


students['ctc']=student_ctcs
students['companyID']=student_company_map

students.to_csv('joined_data.csv',index=False)
           