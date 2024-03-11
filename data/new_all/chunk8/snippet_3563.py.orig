#Source: https://stackoverflow.com/questions/72176562/getting-typeerror-insertstop-takes-0-positional-arguments-but-1-was-given-w
import time
import os
import sys
from tkinter import *

# Creates the Tkinter form named "screen"
screen = Tk()
screen.geometry("550x645")
screen.title("Test")
# Initialize frames
menuframe = Frame(screen,
                  height=60,width=600,bg="gray",pady=5)
inputframe = Frame(screen,
                   height=300,width=600,pady=5)
outputframe = Frame(screen,
                   height=290,width=600,pady=5)

# Packs the frames so they will display
menuframe.pack()
inputframe.pack()
outputframe.pack()


#==STOPBOX==#

stopbox=Text(inputframe,yscrollcommand=1,height= 10,width=20,
               padx=3,pady=3,relief=GROOVE,bg="gray79")
stopbox.place(x=345, y=90)

def insertstop():
    global stop_vanconv
    stop_vanconv=(stop_entry.get())
    stopbox.insert(END, stop_vanconv + "\n")
    stop_entry.delete("0","end")
    

stoplist_label = Label(inputframe,
                       text="Type stop locations and press" + '\n' +
                       "the Add Stop button to insert a new stop.")
stoplist_label.place(x=100, y=150)

stop_entry = Entry(inputframe,
                      textvariable = " ")
stop_entry.place(x=150, y=190)

addstopbutton = Button(inputframe,text="Add Stop",padx=20,pady=0,
                       activebackground="darkslategray4",command=insertstop)
addstopbutton.place(x=160, y=220)

stop_entry.bind('<Return>',insertstop)

screen.mainloop()