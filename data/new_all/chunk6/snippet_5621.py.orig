#Source: https://stackoverflow.com/questions/61810309/threading-error-nameerror-name-datelabelstringvar-is-not-defined
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from numerize import numerize
import pygame
import os
import random
from datetime import datetime
import threading
import time

wholedate = datetime.date(datetime.now())
date = wholedate.strftime("%d")
month = wholedate.strftime("%m")
year = wholedate.strftime("%Y")

def advancetime():
    global date
    global month
    global year
    threading.Timer(5.0, advancetime).start()
    if month == "09" or month == "04" or month == "06" or month == "11":
        date = int(date) + 1
        if date > 30:
            date = 1
            month = int(month) + 1
            if month > 12:
                month = 1
                year = int(year) + 1
        fixdate()
        fixmonth()
        datelabelstringvar.set(str(date) + "/" + str(month) + "/" + str(year))
        return
    if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
        date = int(date) + 1
        if date > 31:
            date = 1
            month = int(month) + 1
            if month > 12:
                month = 1
                year = int(year) + 1
        fixdate()
        fixmonth()
        datelabelstringvar.set(str(date) + "/" + str(month) + "/" + str(year))
        return
    if month == "02":
        date = int(date) + 1
        if date > 31:
            date = 1
            month = int(month) + 1
            if month > 12:
                month = 1
                year = int(year) + 1
        fixdate()
        fixmonth()
        datelabelstringvar.set(str(date) + "/" + str(month) + "/" + str(year))

def calendarOnClose():
    root.deiconify()
    calendarwindow.destroy()

def calendar():
    global datelabelstringvar
    global calendarwindow
    root.withdraw()
    calendarwindow = Toplevel()
    calendarwindow.title("Calendar")
    calendarwindow.geometry("400x350+300+100")
    calendarwindow.protocol("WM_DELETE_WINDOW", calendarOnClose)
    datelabelstringvar = StringVar()
    datelabelstringvar.set(str(date) + "/" + str(month) + "/" + str(year))
    datelabel = Label(calendarwindow, textvariable=datelabelstringvar).grid(row="0", column="0")
    Button(calendarwindow, text="Advance Time", command=advancetime).grid(row="1", column="0")
    totalfruitclickerstringvar = StringVar()
    totalfruitclickerstringvar.set("Fruit Clicked: " + str(totalfruitclicked))
    Label(calendarwindow, textvariable=totalfruitclickerstringvar).grid(row="2", column="0")

root = Tk()
root.title("Fruit Clicker")
root.geometry("400x350+300+100")

calendarbutton = Button(root, text="Calendar", fg="White", bg="Black", width="11", command=calendar)
calendarbutton.grid(row="8", column="0")

advancetime()

root.mainloop()