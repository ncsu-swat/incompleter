#Source: https://stackoverflow.com/questions/68196436/attributeerror-event-object-has-no-attribute-x-win-error
from tkinter import *
import tkinter as tk
import time
root = Tk()
x = 0
y = 0
def move_window(event):
    # global x, y
    print(x, y)
    root.geometry('+{0}+{1}'.format(event.x_root - x, event.y_root - y))

root.overrideredirect(True) # turns off title bar, geometry
root.geometry('400x200+200+200') # set new geometry

# make a frame for the title bar
title_bar = Frame(root, bg='white', relief='raised', bd=2)

# put a close button on the title bar
close_button = Button(title_bar, text='X', command=root.destroy)

# a canvas for the main area of the window
window = Canvas(root, bg='black')

# pack the widgets
title_bar.pack(expand=1, fill=X)
close_button.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)

# bind title bar motion to the move window function
def setxy(event):
    global x,y
    x=event.x_root - root.winfo_x()
    y=event.y_root - root.winfo_y()
    # print(x,y)
    return x,y;
title_bar.bind('<1>',setxy)

title_bar.bind('<B1-Motion>', move_window)

root.mainloop()