import pandas as pd



databse2 = pd.read_excel('stocuri_final.xlsx')
database_link = pd.read_excel('produse_link.xlsx')
new_database2 = database_link.merge(databse2,how='inner', left_on = 'Denumire',right_on='name')
final_link = pd.ExcelWriter('linkuri.xlsx')
new_database2.to_excel(final_link)
final_link.close()