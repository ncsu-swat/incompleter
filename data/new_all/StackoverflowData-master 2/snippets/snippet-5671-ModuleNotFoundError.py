#Source: https://stackoverflow.com/questions/52182578/typeerror-str-object-is-not-callable-in-messgaebox-of-tkinter-in-python
#other codes

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#othercodes

root = Tk()
frame = Frame(root)

#other codes

def net_connection_error():
    #print(dir(messagebox))
    messagebox.INFO(
        "info",
        "No Connection!"
    )

#other codes

net_connection_error()

#other codes

root.mainloop()