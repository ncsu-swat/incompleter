#Source: https://stackoverflow.com/questions/26830872/attributeerror-function-object-has-no-attribute-upper
import sys
import os.path
from tkinter import *

def encode():
    array = []
    temp_array = []
    i = 0
    m = message.get
    m = m.upper()
    array.append(m)
    o = offset.get()
    array.append(o)
    length = len(array[0])
    while length > i:
        temp = array[0][i]
        if temp == " ":
            temp_array.append(temp)
            i = i + 1
        elif temp == ".":
            temp_array.append(temp)
            i = i + 1
        elif (ord(temp) + o) <= 90 and (ord(temp) + o) >= 65:
            #print("Easy option")
            temp = ord(temp)
            temp = temp + o
            temp = chr(temp)
            temp_array.append(temp)
            i = i + 1
        else:
            #print("Hard option")
            temp = ord(temp)
            temp = temp + o
            temp = (temp % 90) + 64
            temp = chr(temp)
            temp_array.append(temp)
            i = i + 1
    i = i - 1
    temp = temp_array[i]
    while i > 0:
        i = i - 1
        temp = temp_array[i] + temp 
    array.append(temp)
    word = (array[2])
    print(word)
    my_file = open("messages.txt", "a") #Open the file messages or if it does not exist create it
    for item in array:              #Get all items in array
        my_file.write(str(item))    #Write them to file
        my_file.write("\n")         #New line
    my_file.close()                 #Close the file


gui = Tk()

gui.title("Caesar Cypher Encoder")

Button(gui, text="Encode", command=encode).grid(row = 3, column = 0)
Label(gui, text = "Message").grid(row = 1, column =0)
Label(gui, text = "Offset").grid(row = 1, column =1)
message = Entry(gui)
message.grid(row=2, column=0)
offset = Scale(gui, from_=1, to=25, orient=HORIZONTAL)
offset.grid(row=2, column=1)

mainloop( )