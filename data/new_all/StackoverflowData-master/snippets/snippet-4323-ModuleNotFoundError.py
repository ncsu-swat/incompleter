#Source: https://stackoverflow.com/questions/59695216/receiving-a-python-typeerror-expected-str-bytes-or-os-pathlike-object-not-str
import os
import shutil
from tkinter import filedialog
from tkinter import *

def browse_button_1():
    global filePath
    filePath = filedialog.askopenfilename()

def browse_button_2():
    global folder_path
    folderPath = filedialog.askdirectory()

def browse_button_3():
    global destination
    destination = filedialog.askdirectory()

def browse_button_4():
    global run
    run = runScript()

root = Tk()

def runScript():

    filesToFind = []
    with open(filePath.get(), "r") as fh:
        for row in fh:
            filesToFind.append(row.strip())

    for filename in os.listdir(folderPath.get()):
        if filename in filesToFind:
            filename = os.path.join(folderPath.get(), filename)
            shutil.copy(filename, destination.get())

filePath = StringVar()
lbl1 = Label(master=root,textvariable=filePath)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse Text File", command=browse_button_1)
button2.grid(row=0, column=3)


folderPath = StringVar()
lbl1 = Label(master=root,textvariable=folderPath)
lbl1.grid(row=0, column=1)
button3 = Button(text="Browse Source Folder", command=browse_button_2)
button3.grid(row=0, column=6)


destination = StringVar()
lbl1 = Label(master=root,textvariable=destination)
lbl1.grid(row=0, column=1)
button4 = Button(text="Browse Destination Folder", command=browse_button_3)
button4.grid(row=0, column=9)


run = StringVar()
lbl1 = Label(master=root,textvariable=run)
lbl1.grid(row=0, column=1)
button5 = Button(text="Run Script", command=runScript)
button5.grid(row=0, column=12)

mainloop()