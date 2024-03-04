#Source: https://stackoverflow.com/questions/48104288/typeerror-initial-value-must-be-str-or-none-not-bytes
# -*- coding : utf-8 -*-
import tkinter as tk
import requests
from PIL import Image
from io import StringIO


class Window:
    def __init__(self, master):
        self.master = master
        self.url = tk.Entry()
        self.url.get()
        self.url.grid(row=0, column=1)
        self.button = tk.Button(text="Download", command=self.get_url)
        self.button.grid(row=0, column=0)
        self.label = tk.Label(text="Name")
        self.label.grid(row=1, column=0)
        self.path = tk.Entry()
        self.path.grid(row=1, column=1)

    def get_url(self):
        self.r = requests.get(self.url.get())
        self.i = Image.open(StringIO(self.r.content))
        self.i.save(self.path.get())


def main():
    root = tk.Tk()
    w = Window(root)
    root.mainloop()


if __name__ == "__main__":
    main()