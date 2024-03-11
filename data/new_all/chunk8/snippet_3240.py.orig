#Source: https://stackoverflow.com/questions/76879501/tkinter-super-init-produces-attributeerror-while-tk-entry-init-do
import tkinter as tk
import tkinter.filedialog as f

class DirEntry(tk.Entry):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(self, parent, *args, **kwargs)


class GUI:

    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry('500x200')

        self.input_dir_string = tk.StringVar()

        self.input_frame = tk.LabelFrame(self.main_window,
                                         text='Input Directory')

        self.input_dir = DirEntry(self.input_frame,
                                  textvariable=self.input_dir_string,
                                  width=40)

        self.button = tk.Button(self.input_frame,
                                text='Choose',
                                command=self.ask_dir)

        self.input_frame.pack()
        self.input_dir.pack(side='left')
        self.button.pack(side='left')

        tk.mainloop()

    def ask_dir(self):
        self.input_dir_string.set(fd.askdirectory())


if __name__ == '__main__':
    gui = GUI()