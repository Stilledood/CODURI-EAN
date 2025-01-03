import json

import pandas as pd

database = pd.read_excel('produse-arn.xlsx')
print(database.head())
print(database.columns)
dict_produse = {}
with open('coduri_ean.json','r') as f:
    dict_produse = json.loads((f.read()))

for i,v in database.iterrows():
    dict_produse[v['Cod']] = v['Denumire']

with open('coduri_ean.json','w') as f:
    json.dump(dict_produse,f)