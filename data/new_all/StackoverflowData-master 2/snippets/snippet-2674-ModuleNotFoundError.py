#Source: https://stackoverflow.com/questions/67120601/attributeerror-demo1-object-has-no-attribute-textbox
from tkinter import ttk
import tkinter as tk
from tkinter import *


def fun1(self,name):
    result="check"
    Demo2.data(result)
    
def cal(master):
     master = Demo2(master)

class Demo1:
    
    def __init__(self, master):
        self.master = master

        button=tk.Button(self.master, text="check",anchor="w",command=lambda :fun1(self,"abc") )
        button.grid(row=0,column=1)
        button.config(command=lambda button=button: [cal(self.master),fun1(self,"abc")])
            
        
class Demo2:
    def __init__(self, master):
        self.master = master

        self.textbox=tk.Text(self.master,font=('Calibri',12))
        self.textbox.grid(row=0,column=1)
        

    def data(self,data):
        self.textbox.insert('end',data)


                            
def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()        
 

 