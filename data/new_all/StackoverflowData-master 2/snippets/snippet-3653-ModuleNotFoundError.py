#Source: https://stackoverflow.com/questions/70628464/importerror-or-attributeerror-while-using-tkinter
#testUI.py

from tkinter import *
from test2 import nameit


root = Tk()
root.title('Scott Window')
root.geometry('500x350')

greet = nameit('John')

mylabel = Label(root, text=greet)
mylabel.pack(pady=20)


root.mainloop()