#Source: https://stackoverflow.com/questions/59564096/typeerror-in-gui-tkinter-ask-stablelvl-missing-1-required-positional-argument
import tkinter as tk
import tkinter.messagebox
#from tkinter import *
from PIL import Image, ImageTk  #To display the image of the formulas of the methods
from tkinter.filedialog import askopenfile 

root3 = tk.Tk()
root3.geometry('200x300') 
info2=tk.Label(root3,text='Enter index of last head value before initiation slug test',anchor='e')
info2.pack()

#Parameter
par = ('Index of stable level')
def ask_stableLvl(enter):
    global stableLvl
    stableLvl =  float(enter['Index of stable level'].get()) 
    print(stableLvl)
#stableLvl = int(input('Enter index of last head value before initiation slug test: '))
def fill(stableLvl):
    dic = {}
    row2 = tk.Frame(root3)
    lab2 = tk.Label(row2, width=15, text=stableLvl, anchor='w')
    ent2 = tk.Entry(row2)      
    row2.pack(side=tk.TOP,fill=tk.X,padx=2,pady=2)
    lab2.pack(side=tk.LEFT)
    ent2.pack(side=tk.RIGHT, expand=tk.YES,fill=tk.X)
    dic[stableLvl] = ent2
    return dic
#
if __name__ == '__main__':
    ent2 = fill(stableLvl)
save_button = tk.Button(root3)
save_button.configure(text='Save', command=ask_stableLvl())
save_button.pack()
root3.mainloop()