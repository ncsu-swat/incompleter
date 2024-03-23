#Source: https://stackoverflow.com/questions/73538666/print-a-placeholder-in-bold-within-a-sentence-using-tags-attributeerror-str
from tkinter import ttk
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x200")

combobox=ttk.Combobox(root, width = 16)
combobox.place(x=15, y=10)
combobox['value'] = ["City", "Other"]


textbox = tk.Text(root,width=20,height=4)
textbox.place(x=15, y=50)

def function1():
    if combobox.get() == "City":
        city = "London" #city = diz[sel_city]["City"]
        city_start = city.upper()
        city_start.tag_config(font=("Verdana", 14, 'bold'))


    def function2():
        text =  f"{city_start} Phrase1, Phrase2, Phrase3"
                
        textbox.delete(1.0,END)     
        textbox.insert(tk.END, text) #.format(allenat_random=allenat_random, variable_random=variable_random))

    function2()


Button = Button(root, text="Print", command=function1)
Button.pack()
Button.place(x=15, y=130)
 
root.mainloop()