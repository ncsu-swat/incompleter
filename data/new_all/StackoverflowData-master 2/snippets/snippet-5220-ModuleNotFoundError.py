#Source: https://stackoverflow.com/questions/57154707/dont-understand-why-im-getting-a-nameerror-in-my-class-definition
from tkinter import ttk
from tkinter import *
import sqlite3

class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Products inventory")

    frame = LabelFrame(self.wind, text  = 'Register a new product')
    frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

    Label(frame, text = 'Name: ').grid(row = 1, column = 0)
    self.name = Entry(frame)
    self.name.grid(row = 1, column = 1)

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()