import customtkinter
from tkinter import ttk
from tkinter import messagebox as mb



class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x400")
        self.title('Database')
        self.button = customtkinter.CTkButton(master=self,text='Search',width=20, corner_radius=5,text_color='white',hover_color='grey',font=('Helvetica',15),fg_color='red',command=self.print_txt)
        self.button.place(relx=0.65,rely=0.65)
        self.check = customtkinter.CTkCheckBox(master=self,text='I have read',)
        self.check.place(relx=0.4,rely=0.4)
        self.combo = customtkinter.CTkComboBox(master=self,values=['value 1', "Value 2"])
        self.combo.place(relx=0.3,rely=0.3)
        self.casuta = customtkinter.CTkEntry(master=self)
        self.casuta.place(relx=0.2,rely=0.2)
        self.bar = customtkinter.CTkProgressBar(master=self)
        self.bar.place(relx=0.4,rely=0.1)
        self.radio = customtkinter.CTkRadioButton(master=self)
        self.radio.place(relx=0.8,rely=0.2)
        self.segment = customtkinter.CTkSegmentedButton(master = self,values=['value 1','value 2'])
        self.segment.place(relx=0.6,rely=0.6)



    def print_txt(self):
        print(self.casuta.get(),self.combo.get())











app = MainWindow()
customtkinter.set_appearance_mode('dark')
app.mainloop()


