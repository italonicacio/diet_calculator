
import tkinter as tk
from view.home import Home
from view.view_food import ViewFood

class App(tk.Tk):
    useful_frames = (Home, ViewFood)

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Diet Calculator")
        self.geometry('1200x600')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        
        config = {
            'bg': '#FFFFFF'
        }
        
        self.configure(**config)
        self.frames = {}
        count = 0
        for F in self.useful_frames:
            count += 1
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
       
        self.show_frame(ViewFood)
    

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == '__main__':
    app = App()
    app.mainloop()

