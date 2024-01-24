#Source: https://stackoverflow.com/questions/43744736/python3-class-function-definition-confusion-about-nameerror
from tkinter import * 

WINDOW_HEIGHT = 300
WINDOW_WIDTH = 325

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def num_but_gen(self, disp, xloc=0, yloc=0, wid=0, hei=0):
        self.Button(text='{}'.format(disp),height=hei, width=wid)
        self.place(x=xloc, y=yloc)

    def init_window(self):
        self.master.title('Calculator')
        self.pack(fill=BOTH, expand=1)
        Button1 = num_but_gen('1', xloc=0, yloc=200, wid=40, hei=40)


root = Tk()
app = Window(root)
root.geometry("{}x{}".format(WINDOW_WIDTH,WINDOW_HEIGHT))
root.mainloop()