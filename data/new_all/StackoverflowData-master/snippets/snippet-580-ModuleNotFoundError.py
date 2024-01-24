#Source: https://stackoverflow.com/questions/28261876/python3-askopenfilename-error
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from mtTkinter import *
import subprocess


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def OpenFile():
    file = open(askopenfilename(),'r')
    print(root.file)

def Quit():
    root.destroy()

def Test():
    print("Hello world")
    input("Press return to exit")

def Shell():
#    print("Below is the output")
    subprocess.call('./home/shanaka/bash_lerning/function1.sh',shell=True)


root = Tk()
root.title("Volatility")
root.geometry("600x400")

menubar = Menu(root)
startmenu = Menu(menubar, tearoff=0)
startmenu.add_command(label="Import", command=OpenFile)
startmenu.add_separator()
startmenu.add_command(label="Exit", command=Quit)
menubar.add_cascade(label="Start", menu=startmenu)

searchmenu = Menu(menubar, tearoff=0)

submenu = Menu(searchmenu)
submenu.add_command(label="New feed", command=Shell)
submenu.add_command(label="Bookmarks")
submenu.add_command(label="Mail")
searchmenu.add_cascade(label='Plugins', menu=submenu, underline=0)

searchmenu.add_separator()
#searchmenu.add_command(label="Plugins", command=Test)
searchmenu.add_command(label="Copy", command=donothing)
searchmenu.add_command(label="Paste", command=donothing)
searchmenu.add_command(label="Delete", command=donothing)
searchmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Search", menu=searchmenu)

reportmenu = Menu(menubar, tearoff=0)
reportmenu.add_command(label="Generate Reports", command=donothing)
menubar.add_cascade(label="Reports", menu=reportmenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()