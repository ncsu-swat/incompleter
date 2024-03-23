#Source: https://stackoverflow.com/questions/45383859/typeerror-an-integer-is-required-got-type-str-in-tkinter
from tkinter import*
from os import open

def addData():
    dataInsert = dataEntry.get()
    itemList.insert(END, dataInsert.upper())
    dataEntry.delete(0, END)

def deleteData():
    dataSelect = itemList.curselection()
    itemList.delete(dataSelect)

def clearData():
    itemList.delete(0, END)

def printData():
    dataDirectory = filedialog.askdirectory()
    f = open('items.txt', dataDirectory, 'ab+')
    f.write(bytes('', itemList.get(), 'UTF-8'))
    f.close()

def rootExit():
    root.destroy()

root = Tk()
root.config(bg='gray79')
root.title('Inventory Recording Systems')
root.geometry('1300x800')
root.resizable(width=False, height=False)

mainLabel = Label(text='Inventory Recording Systems',
                  font=('comic sans ms', 20, 'bold'),
                  bg='gray79',
                  fg='black')

mainLabel.place(x=360, y=10)

f1 = Frame(root,
           bg='black',
           width=300,
           height=40)

f1.place(x=40, y=22)

f2 = Frame(root,
           bg='black',
           width=300,
           height=40)

f2.place(x=950, y=22)

dataLabel = Label(root,
                  text='Enter Data:',
                  font=('comic sans ms', 20, 'bold'),
                  bg='gray79')

dataLabel.place(x=10, y=130)

dataEntry = Entry(root,
                  font=('arial', 16, 'bold'))

dataEntry.place(x=250, y=142)

itemList = Listbox(root,
                    font=('arial', 15, 'bold'),
                    width=47,
                    height=16)

itemList.place(x=10, y=200)

addButton = Button(root,
                   text='Add Data',
                   font=('arial', 20, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=GROOVE,
                   width=15,
                   height=1,
                   bd=5,
                   command=addData)

addButton.place(x=865, y=215)

deleteButton = Button(root,
                   text='Delete Data',
                   font=('arial', 20, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=GROOVE,
                   width=15,
                   height=1,
                   bd=5,
                   command=deleteData)

deleteButton.place(x=865, y=345)

clearButton = Button(root,
                   text='Clear Data',
                   font=('arial', 20, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=GROOVE,
                   width=15,
                   height=1,
                   bd=5,
                   command=clearData)

clearButton.place(x=865, y=470)

printButton = Button(root,
                   text='Print Data',
                   font=('arial', 20, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=GROOVE,
                   width=15,
                   height=1,
                   bd=5,
                   command=printData)

printButton.place(x=865, y=595)

exitButton = Button(root,
                   text='Exit',
                   font=('arial', 10, 'bold'),
                   bg='gray89',
                   fg='black',
                   relief=GROOVE,
                   width=6,
                   height=1,
                   bd=5,
                   command=rootExit)

exitButton.place(x=1212, y=752)

root.mainloop()