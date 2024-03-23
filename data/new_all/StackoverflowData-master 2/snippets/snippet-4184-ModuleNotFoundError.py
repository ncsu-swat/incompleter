#Source: https://stackoverflow.com/questions/61909480/filenotfounderror-errno-2-no-such-file-or-directory-but-the-file-exists
import os
import sys
import Pmw
import time
import tkinter as tk
from tkinter import *
from pathlib import Path

#Def Section
def close():
    install.destroy()

def Policy():
    f= open(Policy())
    t.insert(1.0, f.read())

#dir_location
dir="~/Scrivania/Healir/Healir/Healir_OS/bin/files/"

#file dir_location
Logo_Img = dir + 'logo.png'
Policy = dir + 'Policy.txt'

#gui
install = Tk()
install.title('Healir - Installation')
install.configure(bg='#FFF')
install.attributes("-fullscreen", True)

#logo
Logo_Canvas = Canvas(install, width=100, height=100, bg='#FFF', highlightthickness=0)
Logo_Canvas.pack()
Logo_Img = PhotoImage(file=Logo_Img)
Logo_Canvas.create_image(0, 0, anchor=NW, image=Logo_Img)

#Privacy
Privacy = Label(install, text='Privacy Policy', font='Helvetica 28 bold', fg='#000', bg='#FFF')
Privacy.config(anchor=CENTER)
Privacy.pack()

#text
text = Text(install, wrap=WORD, width=45, height= 20)
with open(Policy, 'r') as f:
    text.insert(INSERT, f.read())

install.mainloop()