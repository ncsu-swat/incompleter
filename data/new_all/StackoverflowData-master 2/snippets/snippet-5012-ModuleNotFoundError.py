#Source: https://stackoverflow.com/questions/71583588/typeerror-menus-init-takes-1-positional-argument-but-2-were-given
from tkinter import *
from meanu_items import *


def main():
    windows = Tk()
    windows.title("NotePad")
    windows.minsize(width=60, height=80)
    windows.config()
    # Create place to write a text
    text = Text(windows)
    text.focus()
    text.grid(pady=0.5, padx=10)

    # Creating Scale
    scroll = Scrollbar(windows, orient=VERTICAL, )
    scroll.grid(row=0, column=1, sticky=NS + SE)
    text.config(yscrollcommand=scroll.set)
    scroll.config(command=text.yview)

    menu = Menus(windows)

    windows.mainloop()


if __name__ == '__main__':
    main()