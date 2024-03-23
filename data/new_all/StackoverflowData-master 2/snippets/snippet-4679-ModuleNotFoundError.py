#Source: https://stackoverflow.com/questions/51704416/none-type-error-in-gui-window-execution-of-farenheit-to-deg-celcius-converter
from tkinter import *
my_window = Tk()
def converter():
    F = float(entry_input.get())
    T = (F-32)*5/9
    display_Temp["text"] = str(T) 
Label(my_window,text="Enter Temperature in Farenheit = ").grid(row=0,column=0)
display_Temp = Label(my_window).grid(row=1,column=1)
entry_input = Entry(my_window).grid(row=0,column=1)
button = Button(my_window,text="Convert to Deg Celcius",command = converter,bd=8,relief="raised").grid(row=1,column=0)
my_window.mainloop()