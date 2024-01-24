#Source: https://stackoverflow.com/questions/76137381/attributeerror-window-object-has-no-attribute-tk
import tkinter as tk
from tkinter import *


class window(Toplevel):
  def __init__(self, master=None):
        self.master=master
        self.title("Add Customer Record")
        window= tk.Tk()
        window.geometry("500x400")


class MainWindow:
  def __init__(self, master=None):
    self.master = master
    self.title("Shopping Mall Management")
    self.master.geometry("500x300")
    Button(self.master, text="Add customer record", command=self.open_save_record_window).pack(pady=20)


root = window()
main_window = MainWindow(root)
root.mainloop()