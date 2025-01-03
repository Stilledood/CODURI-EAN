import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb

import customtkinter
from customtkinter import CTk
import json


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('1920x1080')
        self.title("ARN Database")

        self.search_button = customtkinter.CTkButton(master=self,width=80,height=30, border_width=0, corner_radius=10,text = 'Cauta Produs', text_color='white',hover_color='red',command=self.display_searched_products)
        self.search_button.place(relx=0.65,rely=0.25)
        self.product_name_entry = customtkinter.CTkEntry(self,placeholder_text='Nume Produs', width=380, height=35, corner_radius=10)
        self.product_name_entry.place(relx=0.6, rely=0.25, anchor='ne')

        #Adding tree view to display all searched products
        style = ttk.Style()
        style.theme_use('clam')

        #Modify the font of the body
        style.configure("Treeview",highlightthickness=1,bd=1,font=('Helvetica',8), borderwidth=0,background='gray19',foreground="#B1B1B1",fieldbackground='gray19')

        #Modify the font of the header
        style.configure('Treeview', font=('Helvetica',9, 'bold'), background='gray29')
        style.map('Treeview',background=[('selected','green')])
        columns = ('Denumire Produs', 'Cod Produs')
        self.product_display = ttk.Treeview(self.master,show='headings',height=10, columns=columns)
        self.product_display.place(relx=0.5, rely=0.4,width=800, anchor='center')
        self.product_display.heading('Denumire Produs',text='Produse',anchor='center')
        self.product_display.column('Denumire Produs',width=70, anchor='center')
        self.product_display.heading('Cod Produs',text='Cod Produs', anchor='center')
        self.product_display.column('Cod Produs',width=70,anchor='center')
        self.product_display.bind(self.display_searched_products)


    def display_searched_products(self):
        '''Method to search for a specific product'''

        product_name = self.product_name_entry.get().upper()

        database = {}
        with open('coduri_ean.json','r') as f:
            database = json.loads(f.read())

        products = []
        for key,value in database.items():
            if product_name in value:
                products.append((value,key))

        if products:
            self.product_display.delete(*self.product_display.get_children())
            for product in products:
                self.product_display.insert('','end',values=(product[0],product[1]))






app = App()
customtkinter.set_appearance_mode("dark")
app.mainloop()