import json

dict_coduri_produse = {'cod':''}

with open('coduri_ean.json','w') as f:
    json.dump(dict_coduri_produse,f)
