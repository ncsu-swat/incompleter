#Source: https://stackoverflow.com/questions/59615257/i-want-to-make-a-gui-but-i-get-this-error-self-frame-gridrow-0-column-0-stic
import tkinter as tk

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainWindow, Game, Difficulty):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainWindow(tk.Tk):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcom to TIC TAC TOE", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame(Game))
        button1.pack()

        button2 = tk.Button(self, text="Diffeculty",
                            command=lambda: controller.show_frame(Difficulty))
        button2.pack()

        button3 = tk.Button(self, text="Quit", command=self.Quit)
        button3.pack()

        label1 = tk.Label(self, text="Made by VindictaOG")
        label1.pack()

    def Quit(self):
            exit()


class Game(tk.Tk):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = tk.Button(self, text="New Game")
        button1.pack()

        button2= tk.Button(self, text="Back to homescreen",
                           command=lambda: controller.show_frame(MainWindow))
        button2.pack()


class Difficulty(tk.Tk):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = tk.Button(self, text="1V1", command=lambda: controller.show_frame(MainWindow))
        button1.pack()

        button2 = tk.Button(self, text="Back to homescreen",
                            command=lambda: controller.show_frame(Game))
        button2.pack()

gui = SeaofBTCapp() 
gui.mainloop()