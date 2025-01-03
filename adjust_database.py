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


del_products('18743937')
#change_name("29954944","SPOT LINIAR LED PE SINA 9650A 32,4W 120CM 3000K - TITAN MAGNETIC")


