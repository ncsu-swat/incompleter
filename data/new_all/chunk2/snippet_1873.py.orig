#Source: https://stackoverflow.com/questions/28795573/error-attributeerror-application-object-has-no-attribute-message
from tkinter import ttk
from tkinter import *
import math

root = Tk()

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.title = StringVar()
        self.title.set('Operator Aid: Depressurisation Rate')#~~~TITLE
        self.titleField = Label(self, textvariable = self.title)
        self.titleField.grid(row = 0, column = 0, columnspan = 4, stick = 'nsew')

        self.pressure = Label(self, text = 'Pressure/ Bar')#~~~PRESSURE HEADING
        self.pressure.grid(row = 1, column = 0, columnspan = 2, stick = 'nsew')

        self.time = Label(self, text = 'Time/ Minutes')#~~~TIME HEADING
        self.time.grid(row = 1, column = 2, columnspan = 2, stick = 'nsew')

        self.est_tLabel = Label(self, text = 'Estimated Time at 2 Bar: ')
        self.est_tLabel.grid(row = 7, column = 0, stick = 'e')

        self.est_cLabel = Label(self, text = 'Estimated Category: ')
        self.est_cLabel.grid(row = 8, column = 0, stick = 'e')

        #~~~PRESSURE ENTRY~~~
        self.p1Entry = StringVar()
        self.p1Entry.set('')
        self.p1Entry = Entry(self, textvariable = self.p1Entry)
        self.p1Entry.grid(row = 2, column = 0, stick = 'nsew')

        self.p2Entry = StringVar()
        self.p2Entry.set('')
        self.p2Entry = Entry(self, textvariable = self.p2Entry)
        self.p2Entry.grid(row = 3, column = 0, stick = 'nsew')

        self.p3Entry = StringVar()
        self.p3Entry.set('')
        self.p3Entry = Entry(self, textvariable = self.p3Entry)
        self.p3Entry.grid(row = 4, column = 0, stick = 'nsew')

        self.p4Entry = StringVar()
        self.p4Entry.set('')
        self.p4Entry = Entry(self, textvariable = self.p4Entry)
        self.p4Entry.grid(row = 5, column = 0, stick = 'nsew')

        self.p5Entry = StringVar()
        self.p5Entry.set('')
        self.p5Entry = Entry(self, textvariable = self.p5Entry)
        self.p5Entry.grid(row = 6, column = 0, stick = 'nsew')

        #~~~TIME ENTRY~~~
        self.t1Entry = StringVar()
        self.t1Entry.set('')
        self.t1Entry = Entry(self, textvariable = self.t1Entry)
        self.t1Entry.grid(row = 2, column = 2, stick = 'nsew')

        self.t2Entry = StringVar()
        self.t2Entry.set('')
        self.t2Entry = Entry(self, textvariable = self.t2Entry)
        self.t2Entry.grid(row = 3, column = 2, stick = 'nsew')

        self.t3Entry = StringVar()
        self.t3Entry.set('')
        self.t3Entry = Entry(self, textvariable = self.t3Entry)
        self.t3Entry.grid(row = 4, column = 2, stick = 'nsew')

        self.t4Entry = StringVar()
        self.t4Entry.set('')
        self.t4Entry = Entry(self, textvariable = self.t4Entry)
        self.t4Entry.grid(row = 5, column = 2, stick = 'nsew')

        self.t5Entry = StringVar()
        self.t5Entry.set('')
        self.t5Entry = Entry(self, textvariable = self.t5Entry)
        self.t5Entry.grid(row = 6, column = 2, stick = 'nsew')

        #~~~ESTIMATED PRESSURE AND CATEGORY ENTRY~~~

        self.est_tEntry = StringVar()
        self.est_tEntry.set('')
        self.est_tEntry = Entry(self, textvariable = self.est_tEntry)
        self.est_tEntry.grid(row = 7, column = 1, stick = 'nsew')

        self.est_cEntry = StringVar()
        self.est_cEntry.set('')
        self.est_cEntry = Entry(self, textvariable = self.est_cEntry)
        self.est_cEntry.grid(row = 8, column = 1, stick = 'nsew')

        #~~~PRESSURE BUTTONS~~~
        self.p1Button = Button(self, text = 'ENTER', command = self.submitp1)
        self.p1Button.grid(row = 2, column = 1, stick = 'nsew')

        self.p2Button = Button(self, text = 'ENTER', command = self.submitp2)
        self.p2Button.grid(row = 3, column = 1, stick = 'nsew')

        self.p3Button = Button(self, text = 'ENTER', command = self.submitp3)
        self.p3Button.grid(row = 4, column = 1, stick = 'nsew')

        self.p4Button = Button(self, text = 'ENTER', command = self.submitp4)
        self.p4Button.grid(row = 5, column = 1, stick = 'nsew')

        self.p5Button = Button(self, text = 'ENTER', command = self.submitp5)
        self.p5Button.grid(row = 6, column = 1, stick = 'nsew')

        #~~~TIME BUTTONS~~~
        self.t1Button = Button(self, text = 'ENTER', command = self.submitt1)
        self.t1Button.grid(row = 2, column = 3, stick = 'nsew')

        self.t2Button = Button(self, text = 'ENTER', command = self.submitt2)
        self.t2Button.grid(row = 3, column = 3, stick = 'nsew')

        self.t3Button = Button(self, text = 'ENTER', command = self.submitt3)
        self.t3Button.grid(row = 4, column = 3, stick = 'nsew')

        self.t4Button = Button(self, text = 'ENTER', command = self.submitt4)
        self.t4Button.grid(row = 5, column = 3, stick = 'nsew')

        self.t5Button = Button(self, text = 'ENTER', command = self.submitt5)
        self.t5Button.grid(row = 6, column = 3, stick = 'nsew')

    def submitp1(self):
        words = self.p1Entry.get()
        try:
            p1 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.p1Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_1(p1)))


    def submitp2(self):
        words = self.p2Entry.get()
        try:
            p2 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.p2Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_1(p2)))

    def submitp3(self):
        words = self.p3Entry.get()
        try:
            p3 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.p3Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_2(p3)))

    def submitp4(self):
        words = self.p4Entry.get()
        try:
            p4 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.p4Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_3(p4)))

    def submitp5(self):
        words = self.p5Entry.get()
        try:
            p5 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.p5Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_4(p5)))

    def submitt1(self):
        words = self.t1Entry.get()
        try:
            t1 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.t1Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_1(t1)))

    def submitt2(self):
        words = self.t2Entry.get()
        try:
            t2 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.t2Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_1(t2)))

    def submitt3(self):
        words = self.t3Entry.get()
        try:
            t3 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.t3Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_2(t3)))

    def submitt4(self):
        words = self.t4Entry.get()
        try:
            t4 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.t4Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_3(t4)))

    def submitt5(self):
        words = self.t5Entry.get()
        try:
            t5 = float(words)
        except (ValueError, TypeError):
            self.change_message('ERROR')
            self.t5Entry(0, END)
            return
        self.change_message('clear')
        self.est_tEntry.delete(0, END)
        self.est_tEntry.insert(0, '%.2f' % (self.Calc_4(t5)))

    def change_message(self, status):
        messages = {'error': 'I don\'t understand your input.', 'clear': ''}
        self.message.set(messages[status])
        return

#~~~CALCULATIONS~~~~~~~~~~~~~~~~~
    def Calc_1(self, pressure):
        a1 = math.log(p1) - math.log(p2)
        b1 = t2 - t1
        k1 = a1/b1
        p2bar = math.log(p1) - math.log(2)
        t2bar = (p2bar / k1) + t1
        return t2bar

    def Calc_2(self, pressure):
        a2 = math.log(p2) - math.log(p3)
        b2 = t3 - t2
        k2 = a2/b2
        p2bar = math.log(p1) - math.log(2)
        t2bar = (p2bar / k2) + t1#~~~CHANGE IF YOU WANT EST. TIME FROM
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NOW RATHER THAN START
        return t2bar

    def Calc_3(self, pressure):
        a3 = math.log(p3) - math.log(p4)
        b3 = t4 - t3
        k3 = a3/b3
        p2bar = math.log(p3) - math.log(2)
        t2bar = (p2bar / k3) + t1#~~~CHANGE IF YOU WANT EST. TIME FROM
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NOW RATHER THAN START
        return t2bar

    def Calc_4(self, pressure):
        a4 = math.log(p4) - math.log(p5)
        b4 = t5 - t4
        k4 = a4/b4
        p2bar = math.log(p4) - math.log(2)
        t2bar = (p2bar / k4) + t1#~~~CHANGE IF YOU WANT EST. TIME FROM
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NOW RATHER THAN START
        return t2bar

#~~~MAIN~~~~~~~~~~~~~~~
def main():
    app = Application()
    app.master.title('Operator Aid: Depressurisation Rate')
    app.mainloop()
    return 0

if __name__ == '__main__':
        main()