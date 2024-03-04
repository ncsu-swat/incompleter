#Source: https://stackoverflow.com/questions/73675698/typeerror-not-supported-between-instances-of-int-and-entry
import random
from cgitb import grey
from decimal import DefaultContext
from operator import le
from tkinter import *
from turtle import color, width


window = Tk()
window.title("IDK")
window.configure(bg='grey')
window.geometry("500x500")
window.geometry()


label_title=Label(window, width=6, text="Lenght:", font=(30), bg='#0000FF')
label_title.place(x=0,y=120) 
len_Entry= Entry(window, bd =5)
len_Entry.place(x=120,y=120)

def yeso():
    DefaultLabel = Label(window, text="Default: Yes", font=50)
    DefaultLabel.place(x=290,y=200)
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    Symbols = "[]{}#()*;._-"
    ans = upper_case + lower_case + num + Symbols
    lenght = str(len_Entry)
    password = "".join(random.sample(ans , len_Entry))
    print(password)


def noo():
    DefaultLabel = Label(window, text="Default: No  ", font=50)
    DefaultLabel.place(x=290,y=200)
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    ans2 = upper_case + lower_case + num
    lenght = len_Entry
    password = "".join(random.sample(ans2 , lenght))
    print(password)

Symboletxt = Label(window,width=8, text="Symboles:", font=(30), bg='#0000FF')
Symboletxt.place(x=0,y=200)
my_button = Button(window, text="Yes", bg='#00FF00',command=yeso)
my_button.place(x=120, y=200)
my2_button = Button(window, text="No", bg='#ff0000',command=noo)
my2_button.place(x=180, y=200)



window.mainloop()