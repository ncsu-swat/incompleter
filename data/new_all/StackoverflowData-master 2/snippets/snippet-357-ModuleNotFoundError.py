#Source: https://stackoverflow.com/questions/50948727/typeerror-button-click-missing-1-required-positional-argument-self
from tkinter import *
import tkinter
from client import*

root = tkinter.Tk()
class view():    
    root.geometry("250x300")
    F1 =Frame()
    L = Listbox(F1)
    L.grid(row=0, column =0) 

    L.pack()

    F = open("users.txt","r")
    M = F.read()
    cont = M.split()

    for each in cont:
        ind = each.find("#") + 1
        L.insert(ind+1 ,each[ind:])
        break

    F.close()

    F1.pack()

    # strng_ind = -1
def button_click(self):
        self.form.destroy()
        Chatclient().design()

button = Button(root, text="Create Group Chat", command= button_click)

button.pack()
root.mainloop()