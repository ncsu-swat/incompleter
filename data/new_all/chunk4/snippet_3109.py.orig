#Source: https://stackoverflow.com/questions/45231518/tkinter-listbox-error-attributeerror-int-object-has-no-attribute-tk
from tkinter import *

def ListWindow():
    Listwindow = Tk()           
    Listwindow.title("Welcome")
    Listwindow.geometry("400x130")

    lbl_welcome = Label(Listwindow,text="Welcome to A list box!")
    lbl_welcome.grid(row=0,column=0,columnspan=10)

    myList = Listbox(Listwindow)
    myList.grid(row=1,column=0,columnspan=10)

    WidgetNames = ['Button', 'Canvas']
    for widget in WidgetNames:
        Listbox.insert(0, widget)
    myList.grid(row=0,column=0,columnspan=10)

def main():
    ListWindow()

if __name__ == "__main__":
    main()