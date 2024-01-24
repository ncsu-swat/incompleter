#Source: https://stackoverflow.com/questions/55213354/pystray-with-tkinter-typeerror-takes-1-positional-argument-but-2-were-given
from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
class Program:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Welcome")
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.mainloop()

    def quit_window(self):
        self.icon.stop()
        self.window.destroy()

    def show_window(self):
        self.icon.stop()
        self.window.after(0, self.window.deiconify)

    def withdraw_window(self):
        self.window.withdraw()
        image = Image.open("microphone.ico")
        menu = (item('Quit', self.quit_window), item('Show', self.show_window))
        self.icon = pystray.Icon("name", image, "title", menu)
        self.icon.run()

run=Program()