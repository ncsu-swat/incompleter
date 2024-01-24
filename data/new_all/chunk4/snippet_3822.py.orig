#Source: https://stackoverflow.com/questions/67111305/attributeerror-str-object-has-no-attribute-add
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


class CollegeApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (IndividPage, NewPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(IndividPage)
        self.lift()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class IndividPage(ttk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.userEntry()

    def userEntry(self):
        headingTest = Label(self, text="Enter your UserName:", font="Arial 20")
        headingTest.grid(row=0, column=0, pady=5, padx=5)

        self.usernameEnter = Entry(self, width=40)
        self.usernameEnter.grid(row=0, column=1, padx=5, pady=5)

        self.IndivName = StringVar(self)
        self.IndivName.set(Individuals)

        confirmBtn = Button(self, text="Confirm User", font="Arial 16",
                            command=self.confirm)

        confirmBtn.config(height=4, width=12)
        confirmBtn.grid(row=2, column=2, sticky=E, padx=45, pady=360)

    def confirm(self):
        if self.add_to_team():
            self.controller.show_frame(NewPage)

    def add_to_team(self):
        user = self.usernameEnter.get()
        if len(user) == 0:
            messagebox.showwarning(title='No user', message='Please enter a username!')
            return
        if self.usernameEnter.get():
            self.controller.show_frame(NewPage)

        Individuals = self.IndivName.get()

        if user in Individuals:
            messagebox.showwarning(title='In team', message=f'{user} is already a member of {Individuals}!')
        if len(Individuals) > 20:
            resp = messagebox.askyesno(title='Individuals List is full',
                                       message=f'There are no more spaces in {Individuals}!\nDo you want to join the '
                                               f'team?')
            print(resp)
            if resp:
                self.controller.show_frame(NewPage)
            else:
                return

        Individuals.add(user)
        print(Individuals)


class NewPage(ttk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.userEntry()

    def userEntry(self):
        textlbl = Label(self, text="New Page", font="Arial 20")
        textlbl.grid(row=0, column=0, pady=5, padx=5)


if __name__ == '__main__':
    Individuals = set()
    app = CollegeApp()
    app.geometry("800x500")
    app.title('Points Counter')
    app.mainloop()