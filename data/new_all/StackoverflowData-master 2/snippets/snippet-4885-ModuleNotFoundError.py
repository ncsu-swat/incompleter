#Source: https://stackoverflow.com/questions/42714591/typeerror-unsupported-operand-types-for-int-and-str-when-making-grid
import tkinter
import math
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk



GridSizeSetByUser = '8x8'
choicesRows = ['8', '10', '12', '14']
v = choicesRows[0]
choicesColumns = ['8', '10', '12', '14']
v2 = choicesColumns[0]

GridRows = 9
GridColumns = 9


def getRows():
    global GridRows
    GridRows = GridRowSpinbox.get()
    print(GridRows)

def getColumns():
    global GridColumns
    GridColumns = GridColumnSpinbox.get()
    print(GridColumns)

def Treasure_Hunt_Window():
    THunt = tk.Tk()
    THunt.title("Treasure Hunt")
    THuntInstructions = "Find the treasure hidden deep in the sand!Use ye arrow keys to move around,\n\n then press Space to search that spot! Keep searching until ye find it!"
    board = GameBoard(THunt)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    THunt.mainloop()

def Settings_Window():
    Settings = tk.Tk()
    Settings.title("Settings")
    SettingsWelcome = tk.Label(Settings, text='Settings Menu', width=50, fg="magenta")
    SettingsGridSize = tk.Label(Settings, text='Grid Size:', width =50, fg="magenta")
    global mystring
    mystring = StringVar()
    global mystring2
    mystring2 = StringVar()
    global GridRowSpinbox
    GridRowSpinbox = Spinbox(Settings, values=choicesRows, textvariable=mystring, width=50, state="readonly", fg="magenta")
    SaveRowSize = tk.Button(Settings, text='Save row size for grid', width=50, fg="magenta", command = getRows)
    global GridColumnSpinbox
    GridColumnSpinbox = Spinbox(Settings, values=choicesColumns, textvariable=mystring2, state="readonly", width=50, fg="magenta")
    SaveColumnSize = tk.Button(Settings, text='Save column size for grid', width=50, fg="magenta", command = getColumns)
    SettingsBandits = tk.Label(Settings, text='Amount of Bandits:', width =50, fg="magenta")
    BanditAmount = tk.Entry(Settings, width = 50, fg="magenta")
    SettingsBandits = tk.Label(Settings, text='Amount of Treasure Chests (up to 64)', width =50, fg="magenta")
    SettingsWelcome.pack(fill=X)
    SettingsGridSize.pack(fill=X)
    GridRowSpinbox.pack(fill=X)
    SaveRowSize.pack(fill=X)
    GridColumnSpinbox.pack(fill=X)
    SaveColumnSize.pack(fill=X)
    SettingsBandits.pack(fill=X)
    BanditAmount.pack(fill=X)



def main():
    root = tk.Tk()
    root.title("Menu")
    WelcomeButton = tk.Label(root, text='Welcome to the menu!', width=50, height=2, fg="magenta")
    WelcomeButton.pack(fill=X)
    StartButton = tk.Button(root, text='Start treasure hunting!', width=50, fg="magenta", command = Treasure_Hunt_Window)
    StartButton.pack(fill=X)
    SettingsButton = tk.Button(root, text='''Change the settings of the treasure hunting game.
This includes the grid size.''', width=50, fg="magenta", command = Settings_Window)
    SettingsButton.pack(fill=X)
    QuitButton = tk.Button(root, text='Exit the program', width=50, fg="magenta", command = root.destroy)# display message in a child window.
    QuitButton.pack(fill=X)
    root.mainloop()

def teststuff():
    print(GridRows)
    print(GridColumns)

class GameBoard(tk.Frame):
    def __init__(self, parent, size=48, color1="white", color2="black"):
        '''size is the size of a square, in pixels'''

        self.rows = GridRows
        self.columns = GridColumns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = GridColumns * size
        canvas_height = GridRows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="green")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.canvas.bind("<Configure>", self.refresh)


    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece") 
        self.canvas.tag_lower("square")

main()