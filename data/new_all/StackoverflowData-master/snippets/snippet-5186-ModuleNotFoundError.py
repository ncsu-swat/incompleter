#Source: https://stackoverflow.com/questions/65181993/attributeerror-event-object-has-no-attribute-show-frame-in-tkinter
from tkinter import *
from PIL import Image, ImageTk
   
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
        for F in (StartPage, Page1): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.update()
        self.show_frame(StartPage)
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): # cont = page_name
        if cont not in self.frames:
            self.frames[cont] = cont(container, self)
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")
   
# first window frame startpage 
   
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.bind("<<ShowFrame>>", self.myStartPage)

    def printcehck(self,event):
        print("hack")

    def myStartPage(self,controller):
        super(StartPage).__init__()
        print(controller)
        canvas = Canvas(self,width=300, height=300, bd=0, highlightthickness=0, relief='ridge')
        canvas.pack()

        self.background = PhotoImage(file="background.png")
        canvas.create_image(300,300,image=self.background, tags="B")

        self.character1 = PhotoImage(file="bg-e-butd.png")
        obj1 = canvas.create_image(50,50,image=self.character1, anchor=NW)
        canvas.tag_bind(obj1, '<1>', lambda event=None : controller.show_frame(self,Page1)) #error occurs here.
           
      
# second window frame page1  
class Page1(Frame): 
      
    def __init__(self, parent, controller): 
          
        Frame.__init__(self, parent)

        canvas = Canvas(self,width=300, height=300, bd=0, highlightthickness=0, relief='ridge')
        canvas.pack()

        self.background = PhotoImage(file="background.png")
        canvas.create_image(300,300,image=self.background, tags="B")

        self.character1 = PhotoImage(file="bg-e-butd.png")
        self.after(1000, lambda: (canvas.create_image(50,50,image=self.character1, anchor=NW)))

   
# Driver Code 
app = tkinterApp()
app.title("Title")
app.mainloop() 