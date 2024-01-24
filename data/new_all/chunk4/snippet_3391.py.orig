#Source: https://stackoverflow.com/questions/74967046/how-can-i-import-a-function-into-class-of-an-external-file-nameerror-name-cli
import tkinter as tk
from tkinter import ttk
from page1 import *

root = tk.Tk()
root.geometry('480x320')

style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook', tabposition='ws', background='white', tabmargins=0)

nb = ttk.Notebook(root)
nb.pack(fill='both', expand=1)
page1 = Page1(nb)
nb.add(page1, text='Page 1', compound='left')

datalist = []
        
def clicked(flag, func):
    if flag:
        datalist.append(func())
    else:
        datalist.remove(func())

def try_print():
    if len(datalist) > 0:
        print("ok")

button = tk.Button(root, text="Print", command= try_print())
button.place(x=60, y=100)

root.mainloop()