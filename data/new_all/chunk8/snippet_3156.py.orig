#Source: https://stackoverflow.com/questions/36661245/what-does-this-attributeerror-means-int-object-has-no-attribute-items
from tkinter import *
root=Tk()
root.geometry("512x512")

rows = 8
columns = 8
color1 = "#b35821" #Flery Orange
color2 = "#efcb9d" #New Tan
dim_square = 64

canvas=Canvas(root, width=512, height=512)
canvas.pack()

photo=PhotoImage(file="blackk.gif")

def draw_chessboard():
    color = color2
    for r in range(rows):
        color = color1 if color == color2 else color2
        for c in range(columns):
            x1 = (c * dim_square)
            y1 = ((7-r) * dim_square)
            x2 = x1 + dim_square
            y2 = y1 + dim_square
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="area")
            color = color1 if color == color2 else color2

def draw_pieces():
    canvas.create_image=Canvas(30,30, image=photo, anchor=CENTER, state=NORMAL)

draw_chessboard()
draw_pieces()

root.mainloop()