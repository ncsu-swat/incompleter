#Source: https://stackoverflow.com/questions/66539234/typeerror-init-missing-1-required-positional-argument-parent
from tkinter import *
import tkinter.ttk as ttk


class CollegeApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (StartPage, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.startMenu()

    def startMenu(self):
        heading = Label(self, text="College Tournament Points\n Count Software",
                        font=('Arial', 25))
        heading.grid(row=0, column=0, columnspan=2, padx=240, pady=40)

        start_Btn = Button(self, text="Start", font="Arial 16", width=8,
                           command=lambda: self.controller.show_frame(PageTwo))
        start_Btn.grid(row=1, column=0, padx=30)

        exit_Btn = Button(self, text="EXIT", font="Arial 16", width=8,
                          command=exitButton)
        exit_Btn.grid(row=1, column=1, padx=30)

        def starting_Program():
            pass

class exitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self[Button] = parent.destroy
        self.pack(BOTTOM)


class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        ttk.Label(self, text='This is page two').grid(padx=(20, 20), pady=(20, 20))
        button1 = ttk.Button(self, text='Previous Page',
                             command=lambda: self.controller.show_frame(StartPage))
        button1.grid()


if __name__ == '__main__':
    app = CollegeApp()
    app.geometry("800x500")
    app.title('Points Counter')
    app.mainloop()