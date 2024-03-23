#Source: https://stackoverflow.com/questions/72585255/os-rename-error-the-system-cannot-move-the-file-to-a-different-disk
from tkinter import *
import tkinter.filedialog
import os
import pathlib

window=Tk()
window.title('Hello Python')
window.geometry("300x200+10+10")
window.resizable(False, False)
window.configure(bg='white')

brackets = False

def rename():
    fileNumber = 1
    folderPath = tkinter.filedialog.askdirectory(parent=window, initialdir='Documents', title='Please select a folder')
    for filename in os.listdir(folderPath):
        fileExt = pathlib.Path(filename).suffix
        filePath = folderPath + '/' + filename
        if (fileExt != '.py') :
            if (brackets):
                os.rename(filePath, str(fileNumber) + ')' + fileExt)
            else:
                os.rename(filePath, str(fileNumber) + fileExt)
            fileNumber += 1

lbl=Label(window, text="Welcome to rename it!", fg='black', bg='white', font=("Helvetica", 20))
lbl.place(relx = 0.5, y = 25, anchor=CENTER)

btn=Button(window, text="Rename", fg='blue', command=rename)
btn.place(x=80, y=100)

window.mainloop()