#Source: https://stackoverflow.com/questions/18299930/typeerror-when-using-tkinter-python
from random import *
from tkinter import *

class match:
    def __init__(self):
        self.players = 4*[None]

    def commandos(self):
        print("show commands:")
        print("now commands for you!")

    def choice(self, choose):
        print("No choice")

class Application(Frame):

    def __init__(self, master, match):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.match = match
        self.match.commandos()

    def create_widgets(self):
        self.submit_button = Button(self, text = "Submit", command = self.button_click)
        self.submit_button.grid(row = 2, column = 0, sticky = W)

        self.entry = Entry(self)
        self.entry.grid(row = 1, column = 1, sticky = W)

    def button_click(self):        
        choose = self.entry.get()
        while choose != 'S':
            self.match.choice(choose)
            choose = input()

root = Tk()
root.title("StackQuestion")
root.geometry("250x150")
app = Application(root, match)

root.mainloop()