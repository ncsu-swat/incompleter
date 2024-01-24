#Source: https://stackoverflow.com/questions/44871876/scope-error-nameerror-name-date-is-not-defined
import tkinter as tk
from datetime import datetime, timedelta

class Application(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        master.title("Trade Finance")
        master.minsize(width=250, height=200)
        master.maxsize(width=250, height=200)
        self.date = None


        #Input of expiry date
        label = tk.LabelFrame(master, text = "Input", bd = 2, font='none 8 italic')
        label.pack()
        tk.Label(label, text="Expiry Date (YYYY-MM-DD)",font = 'none 10').pack()

        self.userinput1 = tk.StringVar()
        tk.Entry(label,textvariable = self.userinput1).pack()

        #Input of non-renewal days
        tk.Label(label, text="Non-Renewal Days",font = 'none 10').pack()

        self.userinput2 = tk.StringVar()
        tk.Entry(label, textvariable = self.userinput2).pack()

        #output results
        label_1 = tk.LabelFrame(master, text = "Output", bd = 2, font='none 8 italic')
        label_1.pack()
        tk.Label(label_1,text= 'Review Date',font= 'none 10').pack()
        button = tk.Button(label_1, text="Calculate", fg ='white', bg = 'black',font= 'none 10 bold',command=self.result).pack()
        tk.Entry(label_1, textvariable = self.result).pack()


    def expiry(self):
        while True:
            date = self.userinput1.get()
            try:
                return datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print('Please follow the date format')


    def notice_days(self):
        ndays = self.userinput2.get()
        return timedelta(days=ndays)

    def result(self):
        result = datetime.date(date - days)
        return result

if __name__=='__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()