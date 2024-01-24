#Source: https://stackoverflow.com/questions/65215221/attributeerror-str-object-has-no-attribute-set-tkinter
import tkinter as tk
from tkinter import font as tkFont
from tkinter import StringVar, Entry, Button
from tkinter.ttk import *
import math
root = tk.Tk()
root.title("Simple Calculator")
mathValue = ""
def pressBtn(number):
    global mathValue
    mathValue+=str(number)
    mathValue.set(mathValue)
def mainCalc():
    mathValue = StringVar()
    fontBtn = tkFont.Font(family="Helvetica",size=15,weight='bold')
    inputMath = Label(root,textvariable=mathValue,relief='sunken')
    inputMath.config(text="Enter Your Calculation...", width=50)
    inputMath.grid(columnspan=4,ipadx=100,ipady=15) 
    btn1 = tk.Button(root,text='1',height=0,width=5,font=fontBtn,command=lambda:pressBtn(1))
    btn1.grid(row=1,column=0)
    btn2 = tk.Button(root,text='2',height=0,width=5,font=fontBtn,command=lambda:pressBtn(2))
    btn2.grid(row=1,column=1)
mainCalc()
root.mainloop()