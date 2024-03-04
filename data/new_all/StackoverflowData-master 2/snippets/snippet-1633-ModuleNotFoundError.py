#Source: https://stackoverflow.com/questions/68753814/attributeerror-str-object-has-no-attribute-tk-when-running-tkinter
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from spleeter.separator import Separator
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
screen_width,screen_height = window.maxsize()
window.title("Spleeter GUI Version")
w = int((screen_width-700)/2)
h = int((screen_height-400)/2)
window.geometry(f'700x400+{w}+{h}')

lbl = Label(window, text="File Path:")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

lbl2 = Label(window, text="Stems:")
lbl2.grid(column=0, row=1)

combo = Combobox(window)
combo['values'] = (2,4,5)
combo.current(0)
combo.grid(column=1, row=1)

def Separation():
    File_name=txt.get();
    stems='spleeter:'+combo.get()+'stems'
    separator = Separator(stems)
    separator.separate_to_file(File_name, 'out')
    messagebox.showinfo("Notification", "Separation Finished!")


def clicked():
    Separation()

btn = Button(window, text="Separate", command=clicked)
btn.grid(column=2, row=0)

def main():
    window.mainloop()


if __name__=='__main__':
    main()