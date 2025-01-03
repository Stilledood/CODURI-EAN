import json
import random

import pandas as pd

dict_categories = {
    'Scaune':('Scaune',3),
    'Fotolii' : ('Scaune',3),
    'Mese Dining' : ('Mese',4),
    'Becuri' : ('Iluminat Decorativ',1),
    'Iluminat tehnic' : ('iluminat tehnic',2),
    'Lampi Podea' :('Iluminat Decorativ',1),
    'Plafoniere' : ('Iluminat Decorativ',1),
    'Lampi Perete' : ('Iluminat Decorativ',1),
    'Veioze' : ('Iluminat Decorativ',1),
    'corpuri pe fir': ('Iluminat Decorativ',1),
    'Iluminat decorativ': ('Iluminat Decorativ',1),
    'Mese Cafea' : ('Mese',4),
    'Mese cafea' : ('Mese',4),
    'Mese dining' : ('Mese',4),
    'Decoratiuni' : ('Decoratiuni',7),
    'Exterior' : ('Exterior',9),
    'Finisaje' :('Finisaje',8),
    'Tablouri' : ('Decoratiuni',7),
    'Office' : ('Mobilier', 5),
    'Plante Decorative' : ('Decoratiuni',7),
    'Vaze' : ('Decoratiuni',7),
    'Noptiere' : ('Mobilier', 5),
    'Canapele' : ('Mobilier', 5),
    'Paturi' : ('Mobilier', 5),
    'Saltele' : ('Mobilier', 5),
    'Console Perete' : ('Mobilier', 5),
    'Comode' : ('Mobilier', 5),
    'Flori Artificiale' : ('Decoratiuni',7),
    'Mobilier Exterior' : ('Exterior',9),
    'Masa Toaleta' : ('Mobilier', 5),
    'Mese toaleta' : ('Mobilier', 5),
    'Comode TV' : ('Mobilier', 5),
    'Office' : ('Mobilier', 5),
    'Mobilier Baie' : ('Baie',6),
    'Biblioteca' :('Mobilier', 5),
    'Candelabre' : ('Iluminat Decorativ',1),
    'Accesorii' : ('Decoratiuni',7),
    'Seturi Mobilier' : ('Mobilier', 5),
    'Dresing' : ('Mobilier', 5),
    'Statuete Decorative' : ('Decoratiuni',7),
    'Oglinzi' : ('Decoratiuni',7),
    'Suport Lumnanari' : ('Decoratiuni',7),
    'Riflaje' : ('Finisaje',8),
    'Console TV' : ('Mobilier', 5),
    'Abajur ratan/iuta' : ('Iluminat Decorativ',1),
    'Seturi Mobilier' : ('Mobilier', 5),
    'Living':('Mobilier', 5),
    'Panouri Decorative' : ('Finisaje',8),
    'Pereti verzi artificiali' : ('Decoratiuni',7),
    'Plante artificiale' : ('Decoratiuni',7),
    'Scaune copii' : ('Scaune',3),
}

data_set = pd.DataFrame(columns=['Nume Produs', 'COD EAN'])
database = pd.read_excel('stocuri_final.xlsx')

def load_products_dict():
    with open('coduri_ean.json','r') as f:
        dict_produse = json.loads(f.read())
        return dict_produse
def process_data(filename):
    dict_produse_arn = load_products_dict()
    file_data = pd.read_excel(filename)
    for i, row in file_data.iterrows():
        denumire_produs = row['name']
        categorie = row['categories']
        if isinstance(categorie,float):
            categorie = str(categorie)
            if categorie == 'nan':
                categorie = 'Paturi'

        for key in dict_categories:

            if key in categorie:
                product_suffix = random.randint(1000000,9999999)
                product_code = str(dict_categories[key][1])+str(product_suffix)
                while product_code in dict_produse_arn:
                    product_code = str(dict_categories[key][1])+str(product_suffix)
                dict_produse_arn[product_code] = denumire_produs
                datas = {'Nume Produs':denumire_produs,'COD EAN':product_code}
                data_set.loc[len(data_set)] = datas
                break

    with open('coduri_ean.json','w') as f:
        json.dump(dict_produse_arn,f)
    final_ean = pd.ExcelWriter('coduri.xlsx')
    data_set.to_excel(final_ean)
    final_ean.close()
process_data('stocuri_final.xlsx')
print(data_set.head())
