#Source: https://stackoverflow.com/questions/35787215/nameerror-name-menu-is-not-defined
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.parent.title("xcal file.ics")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.createMenuBar()


    def centerWindow(self):

        w = 500
        h = 500

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def createMenuBar(self):
        menubar = Menu(Frame) #ERROR
        menubar.add_command(label="Hello!", command=hello)
        Frame.config(menu=menubar)

def main():

    root = Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()