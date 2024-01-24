#Source: https://stackoverflow.com/questions/64010698/typeerror-edit-undo-takes-1-positional-argument-but-2-were-given
from tkinter import *

class UI:
   def __init__(self):
      self.root = Tk()
      self.text= Text(self.root)
      self.text.pack()
      self.text.bind("<Return>", self.entry.edit_undo)
      self.text.mainloop()

UI()