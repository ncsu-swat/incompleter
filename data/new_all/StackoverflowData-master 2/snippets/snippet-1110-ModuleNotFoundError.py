#Source: https://stackoverflow.com/questions/45739240/nameerror-name-apply-is-not-defined
from tkinter import *

movieList = ["1 Frozen 06/15 11:35 95", "3 Frozen 06/18 11:35 95",
        "4 Frozen 06/30 11:25 95", "5 Frozen 07/02 11:45 95",
        "6 Frozen 07/05 12:30 95"]

master = Tk()

option = StringVar(master)
option.set(movieList[0]) # Set the first value to be the default option

w = apply(OptionMenu, (master, option) + tuple(movieList))
w.pack()

mainloop()