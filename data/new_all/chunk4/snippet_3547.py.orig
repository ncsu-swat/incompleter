#Source: https://stackoverflow.com/questions/72387864/python-typeerror-bad-operand-type-for-unary-str
import time
import math

a = ""
b = ""
c = ""


def clicked():
    global a
    a = int(entry_a.get())
    global b
    a = int(entry_b.get())
    global c
    c = int(entry_a.get())
    result1 = str((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    result2 = str((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    result = "x1 = " + result1 + ", x2 = " + result2
    text4.config(text=result)


root = tkinter.Tk()
root.title("Univariate quadratic equation Calculator")
root.geometry("350x450")
text1 = tkinter.Label(root, text="a=")
text1.grid(row=0, column=0)
text2 = tkinter.Label(root, text="b=")
text2.grid(row=0, column=2)
text3 = tkinter.Label(root, text="c=")
text3.grid(row=0, column=4)
text4 = tkinter.Label(root, text="Nothing")
text4.grid(row=1, column=0)
entry_a = tkinter.Entry(root, width=5)
entry_a.grid(row=0, column=1)
entry_b = tkinter.Entry(root, width=5)
entry_b.grid(row=0, column=3)
entry_c = tkinter.Entry(root, width=5)
entry_c.grid(row=0, column=5)
btn = tkinter.Button(root, text="Confirm", command=clicked)
btn.grid(row=0, column=6)
root.mainloop()