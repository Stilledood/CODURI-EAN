import pandas as pd
import json

with open('coduri_ean.json','r') as f:
    data = json.loads(f.read())
final_data = {'cod_ean':data.keys(),'denumire produs': data.values()}
pd_data = pd.DataFrame.from_dict(final_data)
final_ean = pd.ExcelWriter('coduri_ean.xlsx')
pd_data.to_excel(final_ean)
final_ean.close()