#Source: https://stackoverflow.com/questions/27515882/csv-reader-close-raises-an-attributeerror
from tkinter import *
import csv
import os
login = "bakerg"

def upgradetoadmin():
    global masterpassword
    masterpassword = []
    def one():
        masterpassword.append("1")
        arraycheck()
    def two():
        masterpassword.append("2")
        arraycheck()
    def three():
        masterpassword.append("3")
        arraycheck()
    def four():
        masterpassword.append("4")
        arraycheck()
    def five():
        masterpassword.append("5")
        arraycheck()
    def six():
        masterpassword.append("6")
        arraycheck()
    def seven():
        masterpassword.append("7")
        arraycheck()
    def eight():
        masterpassword.append("8")
        arraycheck()
    def nine():
        masterpassword.append("9")
        arraycheck()
    def zero():
        masterpassword.append("0")
        arraycheck()
    def clear():
        global masterpassword
        masterpassword = []
    def arraycheck():
        global masterpassword
        if len(masterpassword) == 4:
            if masterpassword == ['2','5','8','0']:
                print("Success")
                r = csv.reader(open('Student Data.csv'))
                lines = [l for l in r]
                print(lines)
                i = 0
                for item in lines:
                    if item[0] == login:
                        print(item)
                        print("YAY")
                        item[4] = "ADMIN"
                        print(item)
                        os.remove('Student Data.csv')
                        writer = csv.writer(open('Student Data.csv', 'w'))
                        writer.writerows(lines)

                print(login + " is now an admin")
            else:
                print("Invalid Code")
            masterpassword = []

    keypadwindow = Tk()
    keypadwindow.iconbitmap("hXYTZdJy.ico")
    keypadwindow.title("ADMIN UPGRADER")
    Button(keypadwindow, text="1", height = 4, width = 10, command = one).grid(column = 0, row = 0)
    Button(keypadwindow, text="2", height = 4, width = 10, command = two).grid(column = 1, row = 0)
    Button(keypadwindow, text="3", height = 4, width = 10, command = three).grid(column = 2, row = 0)
    Button(keypadwindow, text="4", height = 4, width = 10, command = four).grid(column = 0, row = 1)
    Button(keypadwindow, text="5", height = 4, width = 10, command = five).grid(column = 1, row = 1)
    Button(keypadwindow, text="6", height = 4, width = 10, command = six).grid(column = 2, row = 1)
    Button(keypadwindow, text="7", height = 4, width = 10, command = seven).grid(column = 0, row = 2)
    Button(keypadwindow, text="8", height = 4, width = 10, command = eight).grid(column = 1, row = 2)
    Button(keypadwindow, text="9", height = 4, width = 10, command = nine).grid(column = 2, row = 2)
    Button(keypadwindow, text="0", height = 4, width = 10, command = zero).grid(column = 1, row = 3)
    Button(keypadwindow, text="CLEAR", height = 4, width = 10, command = clear).grid(column = 2, row = 3)
    keypadwindow.mainloop()

upgradetoadmin()