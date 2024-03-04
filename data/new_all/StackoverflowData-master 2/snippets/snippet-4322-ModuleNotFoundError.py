#Source: https://stackoverflow.com/questions/59695216/receiving-a-python-typeerror-expected-str-bytes-or-os-pathlike-object-not-str
import os
import shutil
from tkinter import filedialog
from tkinter import *

def browse_button():
    filePath = filedialog.askopenfilename()
    
def browse_button():
    global folder_path
    folderPath = filedialog.askdirectory()

def browse_button():
    global destination
    destination = filedialog.askdirectory()

root = Tk()

filePath = StringVar()
lbl1 = Label(master=root,textvariable=filePath)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse Text File", command=browse_button)
button2.grid(row=0, column=3)


folderPath = StringVar()
lbl1 = Label(master=root,textvariable=folderPath)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse Source Folder", command=browse_button)
button2.grid(row=0, column=6)


destination = StringVar()
lbl1 = Label(master=root,textvariable=destination)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse Destination Folder", command=browse_button)
button2.grid(row=0, column=9)
 
filesToFind = []
with open(filePath, "r") as fh:
    for row in fh:
        filesToFind.append(row.strip())


for filename in os.listdir(folderPath):
    if filename in filesToFind:
        filename = os.path.join(folderPath, filename)
        shutil.copy(filename, destination)

mainloop()