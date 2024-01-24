#Source: https://stackoverflow.com/questions/57642965/calling-listbox-in-python-3-got-an-attribute-error
from tkinter import *  
import tkinter as gui
from random import randint

#code open the first window

print("Listbox setup...", end="")
ls = Tk()
lsbox = ListBox(ls, bg="yellow", fg="orange", selectbackground="grey")
lsbox.pack()
print("OK!")