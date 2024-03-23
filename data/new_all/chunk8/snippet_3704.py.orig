#Source: https://stackoverflow.com/questions/69578986/attributeerror-function-object-has-no-attribute-set-tkinter
from tkinter import *
w = Tk()
w.geometry("250x250")
w.title("OptionMenu Testing")
def DoNothing():
    pass
options = ["Option1", "Option2", "Option3"]
DropdownMenuVar = StringVar()
DropdownMenuVar.set("Option1")
DropdownMenu = OptionMenu(w, DoNothing, *options)
DropdownMenu.place(x=175, y=200)