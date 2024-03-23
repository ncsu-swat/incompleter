#Source: https://stackoverflow.com/questions/65484647/why-have-i-a-nameerror-when-i-transform-a-local-variable-in-global-variable
from tkinter import *
from tkinter import colorchooser

window = Tk()
window.geometry("500x500")

def chooseColor() :
    global colorCode
    global colorName

    colorCode = colorchooser.askcolor(title="Choose color")
    colorName = colorCode[1]
    window.configure(bg=colorName)

title = Label(window, text="Voyons ce que réserve Tkinter", font="none 25", fg=colorName)
title.pack()

but = Button(window, text="Please click :D", command=chooseColor)
but.pack()

window.mainloop()