#Source: https://stackoverflow.com/questions/63231901/tkinter-child-objects-typeerror-list-indices-must-be-integers-or-slices-not-s
import tkinter as tk
from tkinter import ttk


class DummyParent(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title('Test')
        self.children = []
        for i in range(4):
            self.children.append(DummyChild(self))
            self.children[i].grid(row=i//2, column=i%2)


class DummyChild(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.state(ttk.Label(text='Test'))


root = tk.Tk()

dP = DummyParent(master=root)
dP.mainloop()