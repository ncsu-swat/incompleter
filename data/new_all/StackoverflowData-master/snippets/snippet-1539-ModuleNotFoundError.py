#Source: https://stackoverflow.com/questions/38399601/attributeerror-type-object-class-has-no-attribute-stringvar
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class ManyPagesApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        # This loop adds the pages into the frame
        for F in (Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Page1)

    # This function raises the page to the "top" level of the frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Creates what shows in start page
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = ttk.Button(self, text="Go to Page 2", command=lambda: controller.show_frame(Page2))
        button1.pack()

        button2 = ttk.Button(self, text="THIS BUTTON CHANGES LABEL ON PAGE 1",
                         command=lambda: self.labelChanger('This label was changed by using button 2'))
        button2.pack()

        label = ttk.Label(self, text='This is Page 1', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.labelVariable1 = tk.StringVar()
        self.labelVariable1.set('This label will be changed')
        label = tk.Label(self, textvariable= self.labelVariable1)
        label.pack()

    def labelChanger(self, text):
        self.labelVariable1.set(text)

class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        objectofpage1 = Page1

        button1 = ttk.Button(self, text="Goes to page 1", command=lambda: controller.show_frame(Page1))
        button1.pack()

        button2 = ttk.Button(self, text="Changes Label 2 in page 1",
                         command=lambda: objectofpage1.labelChanger(objectofpage1, 'You have changed the label in page 1'))
        button2.pack()

        label = ttk.Label(self, text='This is page 2', font=LARGE_FONT)
        label.pack(pady=10, padx=10)



# Runs everything
if __name__ == "__main__":
    app = ManyPagesApp()
    app.mainloop()