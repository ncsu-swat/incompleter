#Source: https://stackoverflow.com/questions/36983403/python-attribute-error-when-trying-to-access-thread-owned-variable
import tkinter as tk
import threading

class mainWindow(threading.Thread):
    def __init__(self, winWidth=500, winHeight=300):
        threading.Thread.__init__(self)
        self.winWidth = winWidth
        self.winHeight = winHeight

        # Save all drawn objects, to move or delete them later
        self.bricks = []

        self.start()                    #start thread

    def run(self):
        # parent object for all windows
        self.master = tk.Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.callback)
        self.show()

    def callback(self):
        self.master.quit()

    # Initialize everything important
    def show(self, tileSize=10):
        # create main window
        self.w = tk.Canvas(
                self.master,
                width=self.winWidth,
                height=self.winHeight,
                background="white")

        self.w.pack()

        # draw brick
        color = "gray49"
        posX = 200
        posY = 100
        self.bricks.append(self.w.create_rectangle(posX, posY, posX+20, posY+20, fill=color))
        tk.mainloop()

    def move_brick(self, x,y):
        self.w.move(self.brick, x, y)


mainWindow = mainWindow()
mainWindow.move_brick(100,100)