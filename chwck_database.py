import pandas as pd
import json
import random


database = {}
with open('coduri_ean.json','r') as f:
    database = json.loads(f.read())

def check_name(name):
    for i,v in database.items():
        if name in v:
            print(i)
            print(v)

check_name('MODO')

