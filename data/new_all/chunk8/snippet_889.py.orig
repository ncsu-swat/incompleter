#Source: https://stackoverflow.com/questions/52546212/typeerror-start-missing-1-required-positional-argument-self
import tkinter as tk
from tkinter import PhotoImage
import time

class TimeCheck():
    def __init__(self, parent=None, **kw):        
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0              

    def trianglemove(move_x, move_y):
        canvas.move (triangle3, move_x, move_y)

    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                  

    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1
            print ("RECORD")
            #for recordcounter in range(768):
            trianglemove(1, 0)

    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)    

root = tk.Tk()
root.geometry("960x600")

timechecker = TimeCheck(root)

recordbutton = PhotoImage(file="images/recordbutton.gif")
beatbutton = PhotoImage(file="images/beatbutton.gif")
stopbutton = PhotoImage(file="images/stopbutton.gif")

label_toptitle = tk.Label(root, text="Program Name", font=(None, 40),)
label_toptitle.grid(row=0, columnspan=3)

description = "To create rhythm, press the red record button. While recording, use the clicked note button to\n create a series of rectangle notes on screen. They can be held to extend the rectangles. \n\n Once you are done, press the red stop button to stop recording"

pixel = PhotoImage(width=1, height=1)
label_desc = tk.Label(root, image=pixel, compound="center", width=900, font=(None, 14),
                                          padx=20, pady=10, text=description)

label_desc.grid(row=1, columnspan=3)

canvas = tk.Canvas(width=960, height=300, bg='white')
canvas.grid(row=2, column=0, columnspan=3)

for linecounter in range(49):
        newtextbit = linecounter + 1
        if (newtextbit + 3) % 4 == 0 and newtextbit != 49:
                #print ('x is divisible by 3')
                canvas.create_text((linecounter * 16 + 80), 90,
                                           fill="darkblue",
                                           font="Times 10 bold",
                                           text=newtextbit)
        if (newtextbit + 3) % 4 == 0:
                canvas.create_line(((linecounter * 16 + 80)), 40, ((linecounter * 16 + 80)), 70,
                                           width=1,
                                           fill="black"
                                           )
        else:
                canvas.create_line(((linecounter * 16 + 80)), 50, ((linecounter * 16 + 80)), 70,
                                           width=1,
                                           fill="black"
                                           )
canvas.create_line(73, 70, 860, 70,
                                   width=2,
                                   fill="black"
                                   )
triangle3 = canvas.create_polygon(75, 25, 86, 25, 80, 40, fill ='red')

f1 = tk.Frame(root, width=70, height=30)
f1.grid(row=3, column=0, sticky='W')

button_record = tk.Button(f1,
                                                text="Record",
                                                image=recordbutton,
                                                command=TimeCheck.Start,
                                                compound="top"
                                                )
button_beat = tk.Button(f1,
                                                text="Beat",
                                                image=beatbutton,
                                                #command=tomato,
                                                compound="top"
                                                )
button_playstop = tk.Button(f1,
                                                text="Stop",
                                                image=stopbutton,
                                                #command=potato,
                                                compound="top"
                                                )

button_record.pack(side='left', padx=140)
button_beat.pack(side='left', padx=55)
button_playstop.pack(side='left', padx=140)

root.mainloop()