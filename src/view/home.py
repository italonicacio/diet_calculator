import tkinter as tk
from PIL import ImageTk, Image
from view.view_food import ViewFood

from tkinter import ttk


LARGEFONT = ("Verdana", 35)

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=300, height=300, bg='#ffffff')

        self.place(anchor='center', relx=0.5, rely=0.5)
        img = Image.open('assets/logo.png')
        img = img.resize((300, 300))
        self.logo = ImageTk.PhotoImage(img)
        
        self.canvas = tk.Canvas(self, bg='#FFFFFF', width=300, height=300, highlightthickness=0)
        self.canvas.grid()
        self.canvas.create_image(150, 150, image=self.logo)
        
        self.food = tk.Button(self, text='Food', command=lambda : controller.show_frame(ViewFood))
        self.food.grid(row=0, column=4, padx=10, pady=10)

        self.Meal = tk.Button(self, text='Meal', command=lambda : controller.show_frame(tk.Frame)) 
        self.Meal.grid(row=1, column=1, padx=10, pady=10)

    


