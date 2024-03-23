#Source: https://stackoverflow.com/questions/62602353/why-im-getting-filenotfounderror-even-though-the-file-exists-in-the-directory
from tkinter import filedialog
from tkinter import *
import os
root = Tk()
root.withdraw()

folder_selected = filedialog.askdirectory()

list_files = os.listdir(folder_selected)

print(list_files)