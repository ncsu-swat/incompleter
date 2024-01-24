#Source: https://stackoverflow.com/questions/50222747/attributeerror-application-object-has-no-attribute-tk
import tkinter as tk

class Application(tk.Frame):    

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack

        self.PRINT = tk.Button(frame, text = 'Print', fg = 'Red', command = self.Print())
        self.PRINT.pack(side = 'left')    

        self.QUIT = tk.Button(frame, text = 'Quit', fg = 'Red', command = self.quit())
        self.QUIT.pack(side = 'left')    

    def Print(self):
        print('at least somethings working')

root = tk.Tk()

b = Application(root)    
root.mainloop()