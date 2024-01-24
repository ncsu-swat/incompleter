#Source: https://stackoverflow.com/questions/62111479/typeerror-can-only-concatenate-str-not-int-to-str-what-does-it-mean
from tkinter import*
import random
from tkinter import messagebox
window=Tk()
window.title("Random Tools")
window.configure(background="light green")
textvaria = IntVar()
textvaria2 = IntVar()

label0 = Label(window, text = "Min", bg ="light green")
label0.grid(row=1, column=0)

spinboxmin = Spinbox(window, from_=1, to=9999, increment=1, textvariable=textvaria)
spinboxmin.grid(row=2, column=0)
a = spinboxmin.get()

label1 = Label(window, text="Max", bg="light green")
label1.grid(row=3, column=0)

spinboxmax = Spinbox(window, from_=1, to=9999, increment=1, textvariable=textvaria2)
spinboxmax.grid(row = 4, column =0)
b = spinboxmax.get()

def submit2():
    if a <= b:
        answertext.delete('1.0', END)
    else:
        messagebox.showerror("Error", "Max must be greater than min!")

submit = Button(text="Submit", command=submit2)
submit.grid(row=4, column=2)

n = random.randint(a, b+1)

answertext = Text(text=n)
answertext.grid(row=5, column=0)


window.mainloop()