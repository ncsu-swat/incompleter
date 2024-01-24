#Source: https://stackoverflow.com/questions/61191223/attributeerror-tkinter-tkapp-object-has-no-attribute-name-while-usi
import tkinter
import os
import time
#control rod percentages
cr1 = 100

p = '%'

#grid pieces
c1 = 'CTRL ROD 01 '
ins = ' INSERTED'

grid1 = ' _________________________ '
grid2 = '|'
grid3 = '|_________________________|'
def panel():
    print(grid1)
    print(grid3)
    win.after_idle(panel)
    os.system('cls')

win = tkinter.Tk(className=' N.M.S. ')
w = tkinter.Button(win, activeforeground="black", activebackground="red", bg="grey", fg="black", command=panel, text="START", height=1, width=10)
w.pack()
win.mainloop()