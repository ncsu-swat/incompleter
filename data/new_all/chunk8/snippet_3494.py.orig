#Source: https://stackoverflow.com/questions/73271900/bind-all-in-tkinter-module-command-does-not-work-for-me-return-self-funcargs
from tkinter import *
from tkinter import filedialog
from tkinter import font
import tkinter 
from sys import *
import sys
from sys import argv


if len(argv) > 1:
    global filename
    filename = argv[1]
else:
    a = 0



try:
    #def find():
    def new_file():
        text.delete(0.0,END)
        global file2
        file2=filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        file2=file2.name
        global counterofnum
        counterofnum = 1
        global new
        new = 1
        global filename
        filename=file2
        data=text.get(0.0, END)
        file1=open(filename,"w")
        file1.write(data)
        file1.flush()
    def open_file():
        file1=filedialog.askopenfile(mode='r')
        data=file1.read()
        text.delete(0.0,END)
        text.insert(0.0,data) #Inserts data
    counterofnum = 0
    def save_file():
        global filename
        global counterofnum
        if counterofnum == 0:
            global file2
            file2=filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            file2=file2.name
            counterofnum = 1
        elif new == 1:
            global filename
            filename=file2
            data=text.get(0.0, END)
            file1=open(filename,"w")
            file1.write(data)
            file1.flush()
        filename=file2
        data=text.get(0.0, END)
        file1=open(filename,"w")
        file1.write(data)
        file1.flush()
    def save_as():
        file1=filedialog.asksaveasfile(mode='w')
        data=text.get(0.0,END)
        file1.write(data)
        file1.flush()

except AttributeError:
    a = 0

try:
    if filename is None:
        filename = "Untitled.txt"
except NameError:
    filename = "Untitled.txt"


gui=Tk() #tkinter object.
titled = 'Text Editor - ' + filename
gui.title(titled)
gui.geometry("1200x600")
frame = Frame(gui)
frame.pack(pady=5)
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)
text = Text(frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
text.pack() #Display the text
text_scroll.config(command = text.yview)
mymenu=Menu(tearoff=False)
list1=Menu(tearoff=False)
list2=Menu(tearoff=False)
list1.add_command(label='New File',command=new_file, accelerator='Ctrl+N') #Create menus.
list1.bind_all("<Control-n>", new_file)
list1.add_command(label='Save File',command=save_file, accelerator='Ctrl+S')
list1.bind_all("<Control-s>", save_file)
list1.add_command(label='Save File As',command=save_as, accelerator='Ctrl+Shift+S')
list1.bind_all("<Control-Shift-s>", save_as)
list1.add_command(label='Open File',command=open_file, accelerator='Ctrl+O')
list1.bind_all("<Control-o>", open_file)
list1.add_command(label='Exit',command=gui.quit, accelerator='Alt+F4')
mymenu.add_cascade(label='File', menu=list1) #Create a file option.
mymenu.add_cascade(label="Edit", menu=list2)
list2.add_command(label="Cut", \
                    accelerator="Ctrl+X", \
                    command=lambda: \
                            gui.focus_get().event_generate('<<Cut>>'))
list2.add_command(label="Copy", \
                    accelerator="Ctrl+C", \
                    command=lambda: \
                            gui.focus_get().event_generate('<<Copy>>'))
list2.add_command(label="Paste", \
                    accelerator="Ctrl+V", \
                    command=lambda: \
                            gui.focus_get().event_generate('<<Paste>>'))
list2.add_command(label="Undo", \
                    accelerator="Ctrl+Z", \
                    command=lambda: \
                            gui.focus_get().event_generate('<<Undo>>'))
list2.add_command(label="Redo", \
                    accelerator="Ctrl+Shift+X", \
                    command=lambda: \
                            gui.focus_get().event_generate('<<Redo>>'))
#list2.add_command(label="Find",command=find)
gui.config(menu=mymenu)
gui.mainloop()