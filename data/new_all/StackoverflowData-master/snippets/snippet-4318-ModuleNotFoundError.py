#Source: https://stackoverflow.com/questions/59810726/typeerror-after-cancel-takes-2-positional-arguments-but-3-were-given
from tkinter import *
from time import sleep
import os
import sys
times1 = 0
times2 = 1
def quit_():
    screen.destroy()
    sys.exit()
def run():
    global times1
    global times2
    times1 += 1
    bpm = bpm_.get()
    entry.delete(0, END)
    bpm = int(bpm)
    bpm = bpm/60
    bpm = 1/bpm
    def run_():
        global times1
        global times2
        sleep(bpm)
        os.system("afplay metronome.wav&")
        screen.after(1,run_)
        if times1 > times2:
            screen.after_cancel(1,run_)
            times1 = 0
            times2 = 1
    run_()
def main():
    global bpm_
    global entry
    bpm_ = StringVar()
    Label(screen, text="").pack()
    Label(screen, text = "enter a bpm").pack()
    entry = Entry(screen, textvariable=bpm_)
    entry.pack()
    Label(screen, text="").pack()
    Button(screen, text = "enter", command = run).pack()
    Label(screen, text="").pack()
    Button(screen, text = "quit", command = quit_).pack()
screen = Tk()
main()
screen.mainloop()