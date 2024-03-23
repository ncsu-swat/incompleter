#Source: https://stackoverflow.com/questions/42405289/typeerror-overlaps-missing-3-required-positional-arguments-y1-x2-and
from tkinter import *
import tkinter.messagebox
root = Tk()

coords = 1447, 474
canvas = Canvas(root, width=1480, height=960)
frame = Frame(root, width=209, height=960)

def cords(event):
    print(event.x, event.y)

def click(event):
   canvas_id = canvas.create_line(event.x, event.y, coords)
   canvas.after(100,canvas.delete,canvas_id)

line = click

obj1=canvas.create_rectangle(605,482,247,157)
obj2=canvas.create_rectangle(802,720,270,640)

objoverlap2=canvas.find_overlapping(802,720,1082, 473)

canvas.bind('<Button-1>',line)
photo = PhotoImage(file='76.gif')
label = Label(frame, image=photo)
label.config(image=photo)
label.pack()

frame.pack(side='right')
canvas.pack(side='left')

while True:
    canvas.find_overlapping(605,156,247,482)!=line
    root.mainloop()