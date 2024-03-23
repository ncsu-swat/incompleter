#Source: https://stackoverflow.com/questions/77208733/import-widgets-into-a-function-from-a-class-in-another-file-nameerror-name-te
import tkinter as tk
from tkinter import ttk
from tkinter import *

from page1 import Page1

root = tk.Tk()
root.geometry('480x320')

style = ttk.Style()
style.theme_use('default') 
style.configure('TNotebook', tabposition='wn', background='white', tabmargins=0)
style.configure('TNotebook.Tab', background='white', width=10, focuscolor='yellow', borderwidth=0)
style.map('TNotebook.Tab', background=[('selected', 'yellow')])

nb = ttk.Notebook(root)
nb.place(x=0, y=70)
page1 = Page1(nb, width=492, height=905)
nb.add(page1, text='Tab 1', compound='left')

def function1(textbox1, textbox2):

    val_1 = "example 1"
    textbox1.insert(0, val_1)

    val_2 = "example 1"
    textbox2.insert(0, val_2)

button1 = Button(root, text="Button", command= function1(textbox1, textbox2))
button1.place(x=0, y=0)

root.mainloop()