#Source: https://stackoverflow.com/questions/48519145/nameerror-name-root-is-not-defined-in-python-3
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import LabelFrame, Label, Tk#, Canvas
from tkinter.ttk import Notebook
import tkinter.messagebox
import time
import os


import warnings
warnings.filterwarnings('ignore')

class GUIDesign():
    def __init__(self,root):
        self.initUI(root) 

    def initUI(self,root):
        print ("hello")

    LabelFrameFG="purple"
    LabelFrameBG="SNOW"

    note = Notebook(root)
    tab1 = Frame(note)
    tab6 = Frame(note)

def main():
    root = Tk()
    root.resizable(0,0)
    root.state('zoomed')
    GUI=GUIDesign(root)
    root.mainloop()

if __name__ == '__main__':
    main()