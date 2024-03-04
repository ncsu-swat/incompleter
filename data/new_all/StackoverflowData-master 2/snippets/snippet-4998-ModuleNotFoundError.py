#Source: https://stackoverflow.com/questions/25577228/how-can-i-fix-this-error-typeerror-unsupported-operand-types-for-str-an
import sys
from tkinter import *
def mhello():
    text1 = total
    mlabel1 = Label(text=text1, fg ="red")
    mlabel1.pack()
    return
dog = Tk()
input0 = StringVar()
input1 = StringVar()
input2 = StringVar()
dog.geometry('450x450')
dog.title("Tip Calculator")
mlabel = Label(text='This is a Simple Tip Calculator', fg ="red")
mlabel.pack()
mentry = Entry(dog, textvariable=input0)
mentry.pack()
mentry0 = Entry(dog, textvariable=input1)
mentry0.pack()
mentry1 = Entry(dog, textvariable=input2)
mentry1.pack()
meal = input0.get()
tax = input1.get()
tip = input2.get()
tip = tip / 100
tax = tax / 100
meal = meal + meal * tax
total = meal + meal * tip
mbutton = Button(text='Calculate',command = mhello)
mbutton.pack()

dog.mainloop()