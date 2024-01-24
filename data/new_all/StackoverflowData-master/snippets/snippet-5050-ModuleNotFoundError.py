#Source: https://stackoverflow.com/questions/20597786/typeerror-unsupported-operand-types-for-type-and-float
from tkinter import *

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Solution in liters:').grid(row=0, column=0)
        self.vol = DoubleVar
        Entry(frame, textvariable=self.vol).grid(row=0, column=1)
        Label(frame, text='Growth Stage (1-5):').grid(row=1, column=0)
        self.stage = IntVar
        Entry(frame, textvariable=self.stage).grid(row=1, column=1)
        self.fgTotal = DoubleVar
        self.fmTotal = DoubleVar
        self.fbTotal = DoubleVar
        Label(frame, textvariable=self.fgTotal).grid(row=2, column=0)
        Label(frame, textvariable=self.fmTotal).grid(row=2, column=2)
        Label(frame, textvariable=self.fbTotal).grid(row=2, column=3)
        button = Button(frame, text='Calculate', command=self.calculate)
        button.grid(row=3, column=1, sticky=(W, E))

    def calculate(self):
        if self.stage == 1:
             #Seedlings
            fgML,fmML,fbML = 0.33,0.33,0.33
        elif self.stage == 2:
            #Mild Veg
            fgML,fmML,fbML = 1.32,1.32,1.32
        elif self.stage == 3:
            #Aggresive Veg
            fgML,fmML,fbML = 3.96,2.64,1.32
        elif self.stage == 4:
            #Tranistion to Bloom
            fgML,fmML,fbML = 2.64,2.64,2.64
        else:
            #Blooming and Ripening
            fgML,fmML,fbML = 1.32,2.64,3.96
        fgTotal = self.vol * fgML
        fmTotal = self.vol * fmML
        fbTotal = self.vol * fbML


root = Tk()
root.wm_title('Solution Mixer')
app = App(root)
root.mainloop()