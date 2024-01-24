#Source: https://stackoverflow.com/questions/68951032/python-typeerror-label-object-is-not-callable
from PIL import Image, ImageTk
from tkinter import *
from tkinter import Label

def open_window():
    menu = Toplevel(root)
    menu.geometry("800x800")
    menu.title("my game's menu")
    menu.resizable(False, False)
    menu.geometry("800x800")
    lbl = Label(menu, text ="Hello!").pack

    menu.mainloop()


root = Tk()
root.geometry("400x300")
Label = Label(root, text="Are you ready?")
Label.pack()


root.title("quick question")


btn = Button(root, text="Yes", command= open_window)
btn.pack(padx=20, pady = 20)
root.mainloop()