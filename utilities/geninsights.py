import pandas as pd
import numpy as np
import json

branches=['BT-CSE','BT-EE','BS-MTH','BS-SDS','BT-ME','BT-CHE','BT-AE','BT-CE','BT-MSE','BT-BSBE','BS-PHY','BS-CHM','BS-ES','BS-ECO']
df=pd.read_csv('./new_data.csv')

def get_num_avg(df,col):
    total=0
    count=0
    for i in range(len(df)):
        total+=float(df[col][i])
        count+=1
    
    if(count==0):
        return 0
    
    return total/count

def get_num_median(df,col):
    pos=[]
    for i in range(len(df)):
        pos.append(float(df[col][i]))
    pos.sort()
    if(len(pos)==0):
        return 0
    
    return pos[len(pos)//2]

def get_num_max(df,col):
    max_ctc=0
    for i in range(len(df)):
        max_ctc=max(max_ctc,(float(df[col][i])))
    return max_ctc

def get_num_min(df,col):
    min_ctc=10000000000
    change=False
    for i in range(len(df)):
        change=True
        min_ctc=min(min_ctc,(float(df[col][i])))
    
    if not change:
        return 0
    return min_ctc

def get_branch_stats(df):
    branch_data={}

    for branch in branches:
        curr_data={}
        target_df=df[df['Branch']==branch]
        ppos=len(target_df[target_df['Profile']=="PIO-PPO"])
        target_df=target_df[target_df['companyID']!=-1]
        target_df=target_df.reset_index()
        curr_data['averageCPI']=get_num_avg(target_df,'cpi')
        curr_data['averageCTC']=get_num_avg(target_df,'ctc')
        curr_data['medianCTC']=get_num_median(target_df,'ctc')
        curr_data['maxCTC']=get_num_max(target_df,'ctc')
        curr_data['minCTC']=get_num_min(target_df,'ctc')
        curr_data['placed']=len(target_df)
        curr_data['PPO']=ppos
        branch_data[branch]=curr_data
    
    with open('branchwise.json','w') as json_file:
        json.dump(branch_data,json_file,indent=4)
    return

def get_net_stats(df):
    net_stats={}
    target_df=df.loc[df['Branch'].isin(branches)]
    target_df=target_df.reset_index()
    bt_branches=['BT-CSE','BT-EE','BS-MTH','BT-ME','BT-CHE','BT-AE','BT-CE','BT-MSE','BT-BSBE']
    bs_branches=['BS-SDS','BS-PHY','BS-CHM','BS-ES','BS-ECO']
    net_stats["placed"]=len(target_df)
    bts=target_df.loc[target_df['Branch'].isin(bt_branches)]
    bss=target_df.loc[target_df['Branch'].isin(bs_branches)]
    net_stats['placedBT']=len(bts)
    net_stats['placedBS']=len(bss)
    net_stats["maxCTC"]=get_num_max(target_df,'ctc')
    net_stats["minCTC"]=get_num_min(target_df,'ctc')
    net_stats["averageCTC"]=get_num_avg(target_df,'ctc')
    net_stats["medianCTC"]=get_num_median(target_df,'ctc')
    net_stats["PPO"]=len(target_df[target_df['Profile']=="PIO-PPO"])

    with open('cummulative.json','w') as json_file:
        json.dump(net_stats,json_file,indent=4)
    
    return

def get_bracket_stats(df):
    net_stats={}
    target_df=df.loc[df['Branch'].isin(branches)]
    target_df=target_df.reset_index()
    bt_branches=['BT-CSE','BT-EE','BS-MTH','BT-ME','BT-CHE','BT-AE','BT-CE','BT-MSE','BT-BSBE']
    bs_branches=['BS-SDS','BS-PHY','BS-CHM','BS-ES','BS-ECO']
    net_stats["placed"]=len(target_df)
    bts=target_df.loc[target_df['Branch'].isin(bt_branches)]
    bss=target_df.loc[target_df['Branch'].isin(bs_branches)]
    net_stats['placedBT']=len(bts)
    net_stats['placedBS']=len(bss)
    net_stats["maxCTC"]=get_num_max(target_df,'ctc')
    net_stats["minCTC"]=get_num_min(target_df,'ctc')
    net_stats["averageCTC"]=get_num_avg(target_df,'ctc')
    net_stats["medianCTC"]=get_num_median(target_df,'ctc')
    net_stats["PPO"]=len(target_df[target_df['Profile']=="PIO-PPO"])
    
    return net_stats

def get_by_bracket(df):
    brackets=[4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5]

    bracket_data={}

    for bracket in brackets:
        target_df=df[df['cpi']>bracket]
        target_df=target_df[target_df['cpi']<=(bracket+0.5)]
        bracket_data[bracket]=get_bracket_stats(target_df)
    
    with open('bracket_wise.json','w') as json_file:
        json.dump(bracket_data,json_file,indent=4)
    
    return



