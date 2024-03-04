#Source: https://stackoverflow.com/questions/19104771/attribute-error-none-type-object-has-no-attribute-insert-inserting-into-a
from tkinter import *
from tkinter.ttk import *
import math, os

try:
    os.remove("temp.txt")
except OSError:
    pass

def Calculate():
    h1 = float(LongHeight.get())
    h2 = float(ShortHeight.get())
    aj = float(Width.get())
    d = float(Depth.get())

    opc = h1 - h2
    Opc_Width = opc / aj
    Radians = math.atan(opc / aj)
    Pitch = math.degrees(math.atan(opc / aj))
    Width_And_Height_Squared = (opc * opc) + (aj * aj)
    Square_Root = math.sqrt((opc * opc) + (aj * aj))
    Roof_Area = math.sqrt((opc * opc) + (aj * aj))*d

    text_file = open("temp.txt", "a")
    text_file.write("Longest Height: ")
    text_file.write(str(h1))
    text_file.write("\n")
    text_file.write("Shortest Height: ")
    text_file.write(str(h2))
    text_file.write("\n")
    text_file.write("Width: ")
    text_file.write(str(aj))
    text_file.write("\n")
    text_file.write("Depth: ")
    text_file.write(str(d))
    text_file.write("\n")
    text_file.write("Pitch: ")
    text_file.write(str(Pitch))
    text_file.write("\n")
    text_file.write("Roof Area: ")
    text_file.write(str(Roof_Area))
    text_file.write("\n")
    text_file.write("\n")
    text_file.close()

    text_file = open("temp.txt")
    contents = ""

    for i in text_file:
        contents += i

    ResultsBox.insert(END, contents)
    text_file.close()

    ShortHeight.set("")
    LongHeight.set("")
    Depth.set("")
    Width.set("")


window = Tk()
window.geometry("600x400+200+200")
window.title("Roof Pitch Calculator")
window.wm_resizable(0,0)

TitleLabel = Label(window, font = "Comic 30", foreground = "deep sky blue", text = "Roof Pitch Calculator").pack()

CalculateButton = Button(window, text = "Calculate", command = Calculate).pack(side = BOTTOM, pady = 5)
ResultsBox = Text(window, height = 13, width = 70).pack(side = BOTTOM)
ShortHeightLabel = Label(window, text = "Short Height").place(x = 190, y = 50)
LongHeightLabel = Label(window, text = "Long Height").place(x = 330, y = 50)
DepthLabel = Label(window, text = "Depth").place(x = 207, y = 100)
WidthLabel = Label(window, text = "Width").place(x = 345, y = 100)

ShortHeight = StringVar()
ShortHeightEntry = Entry(window, textvariable = ShortHeight)
ShortHeightEntry.place(x = 161, y = 71)

LongHeight = StringVar()
LongHeightEntry = Entry(window, textvariable = LongHeight)
LongHeightEntry.place(x = 300, y = 71)

Depth = StringVar()
DepthEntry = Entry(window, textvariable = Depth)
DepthEntry.place(x = 161, y = 120)

Width = StringVar()
WidthEntry = Entry(window, textvariable = Width)
WidthEntry.place(x = 300, y = 120)

window.mainloop()