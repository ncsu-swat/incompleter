#Source: https://stackoverflow.com/questions/54144305/type-error-missing-required-positional-arguments-with-multiple-py-files
from tkinter import *
import curses
import Bauklotz_class

x1 = 10   #initialise coordinates
y1 = 10
x2 = 20
y2 = 20

root = Tk() #create window
root.wm_title("Raspberry Pi GUI") #window title
root.config(background = "#FFFFFF") #background color

#The whole left frame and widgets involved
leftFrame = Frame(root, width=200, height = 400)
leftFrame.grid(row=0, column = 0, padx = 10, pady = 3)
leftLabel1 = Label(leftFrame, text = "Platzhalter Text")
leftLabel1.grid(row = 0, column = 0, padx = 10, pady = 3)
leftLabel2 = Label(leftFrame, text = "Dies ist ein Text\nmit mehreren Zeilen")
leftLabel2.grid(row = 1, column = 0, padx = 10, pady = 3)


#the whole right frame and widgets involved
rightFrame = Frame(root, width=400, height = 400)
rightFrame.grid(row = 0, column = 1, padx = 10, pady = 3)
E1 = Entry(rightFrame, width = 50)
E1.grid(row = 0, column = 0, padx = 10, pady = 60)

#The two functions for the 2 buttons created
def callback1():
    test = Bauklotz_class.Baustein(20, 30, 40, 50, "red")
    test.show_new_object()

def callback2():
    print(1+1)

buttonFrame = Frame(rightFrame)
buttonFrame.grid(row = 1, column = 0, padx = 10, pady = 60)
B1 = Button(buttonFrame, text = "Button1", bg = "#FF0000", width = 15, command = callback1)
B1.grid(row = 0, column = 0, padx = 10, pady = 60)
B2 = Button(buttonFrame, text = "Button2", bg ="#FFFF00", width = 15, command = callback2)
B2.grid(row = 0, column = 1, padx = 10, pady = 60)

Slider = Scale(rightFrame, from_ = 0, to = 100, resolution = 0.1, orient = HORIZONTAL, length = 400)
Slider.grid(row = 2, column = 0, padx = 10, pady = 3)

Display = Canvas(rightFrame, width = 300, height = 300)
Display.configure(background = 'black')
Display.grid(row = 1, column = 3, padx = 10, pady = 3)

quadrat = Display.create_rectangle(20, 30, 40, 50, fill = "blue")
Display.coords(quadrat, x1, y1, x2, y2)


#following functions are for coordination of the square
#also you can find here the exceptions so that the object
#cant break out of the display widget

def down(event):
    global x1, y1, x2, y2
    if x2 == 290 or y2 == 300:
        pass
    else:
        y1 += 10
        y2 += 10
        Display.coords(quadrat, x1, y1, x2, y2)
        leftLabel1.config(text = "x1: " + str(x1) + ", x2:" + str(x2) + ", y1:" + str(y1) + ", y2:" + str(y2), width = "40" , )
def up(event):
    global x1, y1, x2, y2
    if x2 == 0 or y2 == 10:
        pass
    else:
        y1 -= 10
        y2 -= 10
        Display.coords(quadrat, x1, y1, x2, y2)
        leftLabel1.config(text = "x1: " + str(x1) + ", x2:" + str(x2) + ", y1:" + str(y1) + ", y2:" + str(y2), width = "40" , )
def left(event):
    global x1, y1, x2, y2
    if x1 == 0 or y1 == 10:
        pass
    else:
        x1 -= 10
        x2 -= 10
        Display.coords(quadrat, x1, y1, x2, y2)
        leftLabel1.config(text = "x1: " + str(x1) + ", x2:" + str(x2) + ", y1:" + str(y1) + ", y2:" + str(y2), width = "40" , )
def right(event):
    global x1, y1, x2, y2
    if x1 == 290 or y1 == 300:
        pass
    else:
        x1 += 10
        x2 += 10
        Display.coords(quadrat, x1, y1, x2, y2)
        leftLabel1.config(text = "x1: " + str(x1) + ", x2:" + str(x2) + ", y1:" + str(y1) + ", y2:" + str(y2), width = "40" , )    
root.bind('<a>', left)
root.bind('<w>', up)
root.bind('<s>', down)
root.bind('<d>', right)


root.mainloop()