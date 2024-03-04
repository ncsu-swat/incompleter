#Source: https://stackoverflow.com/questions/74072555/how-can-i-use-value-of-a-combobox-in-another-external-file-to-help-cursor-excute
from tkinter import ttk
import tkinter as tk
from tkinter import *
import sqlite3

from two import *

window = tk.Tk()  
window.geometry("350x200")
style = ttk.Style(window)

combo1=ttk.Combobox(window, width = 22)
combo1['value'] =["Item 1", "Item 2", "Item 3"]
combo1.place(x=10, y=10)
combo1.set("Select")

btn = Button(window, text="Click")
btn.place(x=10, y=80)