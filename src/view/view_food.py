import tkinter as tk
from home import Home

class ViewFood(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent , width=300, height=300, bg='#ffffff')
        
        OPTIONS = ['g']

        name = tk.Label(self, text='Nome')
        name.grid(row=1, column=0)
        name_field = tk.Entry(self)
        name_field.grid(row=1, column=1, ipadx=100)
        
        amount = tk.Label(self, text='Quantidade')
        amount.grid(row=2, column=0)
        amount_field = tk.Entry(self)
        amount_field.grid(row=2, column=1, ipadx=100)

        unity = tk.Label(self, text='Unidade')
        unity.grid(row=3, column=0)
        #modificar unidade para ser um select
        #onde o usuario escolhe uma unidade disponivel
        unity_field = tk.Entry(self)
        unity_field.grid(row=3, column=1, ipadx=100)

        kcal_label = tk.Label(self, text='Kcal')
        kcal_label.grid(row=4, column=0)
        kcal_field = tk.Entry(self)
        kcal_field.grid(row=4, column=1, ipadx=100)

        protein_label = tk.Label(self, text='Proteína (g)')
        protein_label.grid(row=5, column=0)
        protein_field = tk.Entry(self)
        protein_field.grid(row=5, column=1, ipadx=100)

        carbohydrate_label = tk.Label(self, text='Carboidrato (g)')
        carbohydrate_label.grid(row=6, column=0)
        carbohydrate_field = tk.Entry(self)
        carbohydrate_field.grid(row=6, column=1, ipadx=100)

        fat_label = tk.Label(self, text='Gordura (g)')
        fat_label.grid(row=7, column=0)
        fat_field = tk.Entry(self)
        fat_field.grid(row=7, column=1, ipadx=100)

        button_back = tk.Button(self, text='Voltar',
                                command= lambda : controller.show_frame(Home)
                                )