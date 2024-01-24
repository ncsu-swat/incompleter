#Source: https://stackoverflow.com/questions/65269660/getting-attributeerror-trying-to-access-math-sqrtx-in-tkinter-app
from tkinter import *
import math

root = Tk()
root.title("More Complex Calculator")

entry_1 = Entry(root, width = 50, borderwidth = 5)
entry_1.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def button_click(number):
    current = entry_1.get()
    entry_1.delete(0, END)
    entry_1.insert(0,str(current) + str(number))

def button_add():
    first_number = entry_1.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry_1.delete(0, END)

def button_sub():
    first_number = entry_1.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry_1.delete(0, END)

def button_mult():
    first_number = entry_1.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry_1.delete(0, END)

def button_div():
    first_number = entry_1.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry_1.delete(0, END)

def button_square():
    first_number = entry_1.get()
    global f_num
    global math
    math = "square"
    f_num = int(first_number)

def button_root():
    first_number = entry_1.get()
    global f_num
    global math
    math = "root"
    f_num = int(first_number)

def button_enter():
    second_number = entry_1.get()
    entry_1.delete(0, END)
    if math == "addition":
        entry_1.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        entry_1.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        entry_1.insert(0, f_num * int(second_number))
    elif math == "division":
        entry_1.insert(0, f_num / int(second_number))
    elif math == "square":
        entry_1.insert(0, f_num**2)
    elif math ==  "root":
        entry_1.insert(0, math.sqrt(f_num))

def button_clear():
    entry_1.delete(0, END)

button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_pi = Button(root, text = "π", padx = 39, pady = 20, command = lambda: button_click(math.pi))
button_e = Button(root, text = "e", padx = 40, pady = 20, command = lambda: button_click(math.e))

button_add = Button(root, text = "+", padx = 39, pady = 20, command = button_add)
button_enter = Button(root, text = "=", padx = 39, pady = 20, command = button_enter)
button_clear = Button(root, text = "C", padx = 39, pady = 20, command = button_clear)

button_sub = Button(root, text = "-", padx = 41, pady = 20, command = button_sub)
button_mult = Button(root, text = "x", padx = 40, pady = 20, command = button_mult)
button_div = Button(root, text = "÷", padx = 40, pady = 20, command = button_div)

button_square = Button(root, text = "x²", padx = 38, pady = 20, command = button_square)
button_sqroot = Button(root, text = "√x", padx = 36, pady = 20, command = button_root)

button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)

button_0.grid(row = 5, column = 1)
button_square.grid(row = 1, column = 2)
button_sqroot.grid(row = 1, column = 3)

button_add.grid(row = 2, column = 3)
button_enter.grid(row = 5, column = 2)
button_clear.grid(row = 5, column = 0)

button_pi.grid(row = 1, column = 0)
button_e.grid(row = 1, column = 1)

button_sub.grid(row = 3, column = 3)
button_mult.grid(row = 4, column = 3)
button_div.grid(row = 5, column = 3)

root.mainloop()