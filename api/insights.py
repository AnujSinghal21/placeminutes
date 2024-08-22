import sqlite3
import json
import pandas as pd

def get_branchwise_insights():
    with open('./branchwise.json','r') as json_file:
        data=json.load(json_file)
    return data

def get_net_insights():
    with open('./cummulative.json') as json_file:
        data=json.load(json_file)
    return data

def get_bracketwise():
    with open('./bracket_wise.json','r') as json_file:
        data=json.load(json_file)
    return data

