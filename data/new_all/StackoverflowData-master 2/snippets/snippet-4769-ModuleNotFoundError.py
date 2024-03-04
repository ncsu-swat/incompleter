#Source: https://stackoverflow.com/questions/49158720/updatedtk-root-not-callable-multiple-problems-attributeerror-nonetype-obj
import tkinter as tk

Large_font= ("arial", 30)

class Myapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Payment")
        #root.withdraw()
        self.geometry("1280x1024")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Homepage, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Homepage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Homepage(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        Frame.__init__(self, parent, **kwargs)
        self.configure(background='grey')
        f1 = tk.Frame(self, width=1200, height=100, bd=3, bg="grey", relief="raise")
        f1.pack(side="top")
        lblInfo = tk.Label(f1, text="MY APP", font=Large_font, bg="grey", fg="white")
        lblInfo.pack(side="top")

#=========SUM UP==========
        f3 = tk.Frame(self, width=400, height=800, bd=3, bg="grey", relief="raise")
        f3.pack(side="right")

        def uiPrint():
            print("")
            print(clickcount)
            blankLine()

        self.click = tk.IntVar()
        self.click.set("6");

        def blankLine():
            for i in range(0):
                print("")

        def buttonCommand():
            global clickcount
            global click
            global mult
            clickcount += 2 * (mult)
            self.click.set(str(clickcount));  # Update score
            uiPrint()

        def buttonCommand1():
            global clickcount
            global click
            global mult
            clickcount -= 1 * (mult)
            self.click.set(str(clickcount));
            uiPrint()

        l = tk.Label(f3, textvariable=click)  # Score
        l.pack()
        plusButton = tk.Button(f3, command = buttonCommand, text="+")
        minusButton = tk.Button(f3, command = buttonCommand1, text="-")
        plusButton.pack(padx=10, pady=10)
        minusButton.pack(padx=10, pady=10)
        btn1 = tk.Button(f3, padx=20, pady=20, bd=8, fg="white", bg="green", font=('arial', 30, 'bold'),
                  text="NEXT")
        btn1.pack(padx=10, pady=10)


clickcount = (6)
mult = 1
dcp1 = 0

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='grey')
        f1 = tk.Frame(self, width=600, height=100, bd=3, bg="grey", relief="raise")
        f1.pack()


app = Myapp()
app.mainloop()