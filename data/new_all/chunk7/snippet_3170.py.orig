#Source: https://stackoverflow.com/questions/29923129/why-am-i-getting-typeerror-init-missing-1-required-positional-argument
#Imports#
import sys
sys.path.append("F:\A2\Computing\Comp 4\Python34\Lib\site-packages")

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#Main Code#


class GUIImage(tk.Tk):
    def __init__(self, master, *pargs):
        tk.Tk.__init__(self, master, *pargs)

        self.image = Image.open("F:\A2\Computing\Comp 4\Code\main.jpg")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.frames={}

        for F in(mainMenuGUI,addUserGUI,delUserGUI,visitorGUI,prechkGUI,userManual):
            frame = F(container, self)
            self.frames[Frames] = frame
            frame.grid(row=0,column=0,sticky="nsew")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)


class mainMenuGUI(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init(self,parent)
        mainMenuGUI = GUIImage(App)
        mainMenuGUI.pack(fill=BOTH, expand=YES)
        MMText = Label(self, text ="Main Menu",bg ="#FD7F17", font = ("Arial Black",18)).place(relx=.40, rely=.05)
        MMButton1= Button(self, text = "Add User", fg = "white",bg = "dark grey", command = lambda:controller.show_frame(addUserGUI),height = "1", width ="10", font = ("Arial Black",14)).place(relx =.38 , rely=.14)
        MMButton2= Button(self, text = "Delete User", fg = "white",bg = "dark grey", command = lambda:controller.show_frame(delUserGUI),height = "1", width ="10", font = ("Arial Black",14)).place(relx =.38 , rely=.28)
        MMButton3= Button(self, text = "Add Visitor", fg = "white",bg = "dark grey", command = lambda:controller.show_frame(VisitorGUI),height = "1", width ="10", font = ("Arial Black",14)).place(relx =.38 , rely=.42)
        MMButton4= Button(self, text = "Premises Check", fg = "white",bg = "dark grey", command =   lambda:controller.show_frame(prechkGUI) ,height = "1", width ="14", font = ("Arial Black",14)).place(relx =.32 , rely=.56)
        MMButton5= Button(self, text = "Vehicle Check", fg = "white",bg = "dark grey", command = "navVehChe",height = "1", width ="14", font = ("Arial Black",14)).place(relx =.32 , rely=.70)
        MMButton6= Button(self, text = "User Manual", fg = "white",bg = "dark grey", command =  lambda:controller.show_frame(userManual),height = "1", width ="10", font = ("Arial Black",14)).place(relx =.38 , rely=.84)

App = GUIImage()
App.mainloop()