#Source: https://stackoverflow.com/questions/66970261/attributeerror-str-object-has-no-attribute-configure
from tkinter import *

root = Tk()
root.resizable(width=False, height=False)

b1 = Button(root, text = '', width = 10, height = 5, command = lambda: main(1))
b1.grid(row = 0, column = 1)
b2 = Button(root, text = '', width = 10, height = 5, command = lambda: main(2))
b2.grid(row = 0, column = 2)
b3 = Button(root, text = '', width = 10, height = 5, command = lambda: main(3))
b3.grid(row = 0, column = 3)
b4 = Button(root, text = '', width = 10, height = 5, command = lambda: main(4))
b4.grid(row = 1, column = 1)
b5 = Button(root, text = '', width = 10, height = 5, command = lambda: main(5))
b5.grid(row = 1, column = 2)
b6 = Button(root, text = '', width = 10, height = 5, command = lambda: main(6))
b6.grid(row = 1, column = 3)

def main(num):
    something = 'b' + str(num)
    something.configure(text = 'hi')