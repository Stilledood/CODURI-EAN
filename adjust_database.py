import json


def del_products( product_code):
    database = {}
    with open('coduri_ean.json','r') as f:
        database = json.loads(f.read())

    del database[product_code]

    with open('coduri_ean.json','w') as f:
        json.dump(database,f)



def change_name(product_code,name):
    with open('coduri_ean.json','r') as f:
        database = json.loads(f.read())
    database[product_code] = name

    with open('coduri_ean.json','w') as f:
        json.dump(database,f)


#del_products('54750965')
change_name("54745863","NOPTIERA AROLA")


