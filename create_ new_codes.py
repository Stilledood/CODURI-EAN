import json
import pandas as pd
import random


database = {}
with open('coduri_ean.json','r') as f:
    database = json.loads(f.read())




def create_code(product_name, product_suffix):
    flag = True
    while flag:
        product_code = product_suffix + str(random.randint(1000000,9999999))
        if product_code not in database:
            database[product_code] = product_name
            flag = False


    with open('coduri_ean.json','w') as f:
        json.dump(database,f)



create_code('PLAFONIERA MODO DIA 80CM AURIU','1')

