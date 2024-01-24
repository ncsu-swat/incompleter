#Source: https://stackoverflow.com/questions/65445879/implementing-vkeyboard-in-tkinter-window-causing-error-attributeerror-int-o
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import pygame
import cv2
import numpy as np
import os


class tkinterApp(Tk): 
      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        Tk.__init__(self, *args, **kwargs) 
          
        # creating a container 
        container = Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        # initializing frames to an empty array 
        self.frames = {}
        
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (Page1,Page2): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.update()
        self.show_frame(Page1)
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): # cont = page_name
        if cont not in self.frames:
            self.frames[cont] = cont(self.container, self)
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

   

class Page1(Frame): 
      
    def __init__(self, parent, controller): 
          
        Frame.__init__(self, parent)
        self.controller = controller
        pygame.mixer.init()
        self.bind("<<ShowFrame>>", self.myPage1)

    def myPage1(self,controller):
        super(Page1).__init__()

        canvas = Canvas(self,width=2300, height=900, bd=0, highlightthickness=0, relief='ridge')
        canvas.pack()

        canvas1 = Canvas(canvas, width=2000, height=500, bd=0, highlightthickness=0, relief='ridge')
        canvas.create_window(730,600,window=canvas1)

        self.background = PhotoImage(file="Images/background.png")
        canvas.create_image(525,425,image=self.background, tags="B")

        self.canvas_textbox = canvas.create_text(290, 250, text='SOME TEXT', anchor=NW,fill="cyan", font=('Orbitron',72))

        def highlight(item):
            # mark focused item.  note that this code recreates the
            # rectangle for each update, but that's fast enough for
            # this case.
            bbox = canvas.bbox(item)
            canvas.delete("highlight")
            if bbox:
                i = canvas.create_rectangle(
                    bbox, fill="",
                    tag="highlight"
                    )
                canvas.lower(i, item)

        def has_focus():
            return canvas.focus()

        def has_selection():
            # hack to work around bug in Tkinter 1.101 (Python 1.5.1)
            return canvas.tk.call(canvas._w, 'select', 'item')

        def set_focus(event):
            print("set_focus")
            if canvas.type(CURRENT) != "text":
                return

            highlight(CURRENT)

            # move focus to item
            canvas.focus_set() # move focus to canvas
            canvas.focus(CURRENT) # set focus to text item
            canvas.select_from(CURRENT, 0)
            canvas.select_to(CURRENT, END)


        def handle_key(event):
            print("handle_key")
            # widget-wide key dispatcher
            item = has_focus()
            if not item:
                return
            elif event.keysym == 'Return':
                canvas.delete("highlight")
                print(canvas.focus(""))

            insert = canvas.index(item, INSERT)

            if event.char >= " ":
                # printable character
                if has_selection():
                    canvas.dchars(item, SEL_FIRST, SEL_LAST)
                    canvas.select_clear()
                canvas.insert(item, "insert", event.char)
                highlight(item)

            elif event.keysym == "BackSpace":
                if has_selection():
                    canvas.dchars(item, SEL_FIRST, SEL_LAST)
                    canvas.select_clear()
                else:
                    if insert > 0:
                        canvas.dchars(item, insert-1, insert)
                highlight(item)

            # navigation
            elif event.keysym == "Home":
                canvas.icursor(item, 0)
                canvas.select_clear()
            elif event.keysym == "End":
                canvas.icursor(item, END)
                canvas.select_clear()
            elif event.keysym == "Right":
                canvas.icursor(item, insert+1)
                canvas.select_clear()
            elif event.keysym == "Left":
                canvas.icursor(item, insert-1)
                canvas.select_clear()

            else:
                pass # print event.keysym


        # standard bindings
        canvas.bind("<Double-Button-1>", set_focus)
        canvas.bind("<Key>", handle_key)

        buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'SHIFT',
            ' Space ',
        ]
        curBut = [-1,-1]
        buttonL = [[]]
        #entry = Text(Keyboard_App, width=97, height=8)
        #entry.grid(row=0, columnspan=15)

        varRow = 1
        varColumn = 0

        def leftKey(event):
            if curBut == [-1,-1]:
                curBut[:] = [0,0]
                buttonL[0][0].configure(highlightbackground='red')
            elif curBut[0] == 4:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
                curBut[:] = [0,10]
                buttonL[0][10].configure(highlightbackground='red')
            else:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
                curBut[:] = [curBut[0], (curBut[1]-1)%11]
                buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')

        def rightKey(event):
            if curBut == [-1,-1]:
                curBut[:] = [0,0]
                buttonL[0][0].configure(highlightbackground='red')
            elif curBut[0] == 4:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
                curBut[:] = [0,0]
                buttonL[0][0].configure(highlightbackground='red')
            else:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
                curBut[:] = [curBut[0], (curBut[1]+1)%11]
                buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')

        def upKey(event):
            if curBut == [-1,-1]:
                curBut[:] = [0,0]
                buttonL[0][0].configure(highlightbackground='red')
            elif curBut[0] == 0:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
                curBut[:] = [(curBut[0]-1)%5, 0]
                buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
            else:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
                curBut[:] = [(curBut[0]-1)%5, curBut[1]]
                buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')

        def downKey(event):
            if curBut == [-1,-1]:
                curBut[:] = [0,0]
                buttonL[0][0].configure(highlightbackground='red')
            elif curBut[0] == 3:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
                curBut[:] = [(curBut[0]+1)%5, 0]
                buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
            else:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
                curBut[:] = [(curBut[0]+1)%5, curBut[1]]
                buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')

        def select(value, x, y):
            if curBut != [-1,-1]:
                buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
            curBut[:] = [x,y]
            buttonL[x][y].configure(highlightbackground='red')
            if value == "<-":
                input = self.canvas_textbox.get("1.0", 'end-2c')
                self.canvas_textbox.delete("1.0", END)
                self.canvas_textbox.insert("1.0", input, END)

            elif value == " Space ":
                self.canvas_textbox.insert(END, ' ')

            elif value == "Tab":
                self.canvas_textbox.insert(END, '   ')

            else:
                self.canvas_textbox.insert(END, value)

        for button in buttons:
            if button != " Space ":
                but = Button(canvas1, text=button, width=5, bg="#000000", fg="#ffffff", highlightthickness=4, 
                               activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                               pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
                buttonL[varRow-1].append(but)
                but.grid(row=varRow, column=varColumn)

            if button == " Space ":
                but = Button(canvas1, text=button, width=60, bg="#000000", fg="#ffffff", highlightthickness=4, 
                               activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=4,
                               pady=4, bd=4, command=lambda x=button, i=varRow-1, j=varColumn: select(x, i, j))
                buttonL[varRow-1].append(but)
                but.grid(row=6, columnspan=16)

            varColumn += 1
            if varColumn > 10:
                varColumn = 0
                varRow += 1
                buttonL.append([])

        canvas1.bind('<Left>', leftKey)
        canvas1.bind('<Right>', rightKey)
        canvas1.bind('<Up>', upKey)
        canvas1.bind('<Down>', downKey)

class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.myPage2)


    def myPage2(self,controller):
        super(Page2).__init__()

        canvas = Canvas(self,width=2300, height=900, bd=0, highlightthickness=0, relief='ridge')
        canvas.pack()

        self.background = PhotoImage(file="Images/background.png")
        canvas.create_image(525,425,image=self.background, tags="B")

        canvas.create_text(140,376, fill="cyan",text="Second Frame")

app = tkinterApp()
app.title("Test")
app.mainloop() 