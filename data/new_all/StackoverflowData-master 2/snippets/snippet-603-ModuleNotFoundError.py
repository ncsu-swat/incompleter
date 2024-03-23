#Source: https://stackoverflow.com/questions/20152258/typeerror-can-only-concatenate-tuple-not-str-to-tuple-in-python
#-*- coding: cp857 -*-

from tkinter import *

###########################################################

root=Tk()

root.title("MY FILM ARCHIVE")

root.resizable(False, False)

########################################################### 


def add():
    db = open(r"C:\Users\PC\Desktop\db.txt", "a+")
    enter=input("Enter your's film: "),
    db.write(enter + "\n")
    db.close()
    db.flush()    

button=Button(text="Add Film!",command=add, font=("Flux",15, "bold"))
button.pack(expand="yes", anchor="center")

mainloop()