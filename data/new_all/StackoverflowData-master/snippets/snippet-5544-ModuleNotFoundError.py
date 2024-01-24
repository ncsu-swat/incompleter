#Source: https://stackoverflow.com/questions/63971808/attributeerror-int-object-has-no-attribute-after
from tkinter import *
timer = 60
def startGame(event):
    if timer == 60:
        countdown()
def countdown():
    global timer
    if timer > 0:
        timer -= 1
        timeLabel.config(text='Time left:' + str(timer))
        timer.after(1000, countdown())
window = Tk()
timeLabel = Label(window, text='time = 60 sec')
entryBox = Entry(window)
timeLabel.pack()
entryBox.pack()
window.bind('<Return>', startGame)
entryBox.pack
entryBox.focus_set()
window.mainloop()