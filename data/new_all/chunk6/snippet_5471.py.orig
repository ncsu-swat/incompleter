#Source: https://stackoverflow.com/questions/27089880/error-attribute-error-in-tcl
from tkinter import *
from tkinter import ttk
sys.path.insert(0, 'home/ashwin/')
import portscanner

class App:
    def __init__(self, master):

        master.option_add('*tearOff', False)
        master.resizable(False,False)

        self.nb = ttk.Notebook(master)
        self.nb.pack()
        self.nb.config(width=720,height=480)

        self.zipframe = ttk.Frame(self.nb)
        self.scanframe = ttk.Frame(self.nb)
        self.botframe = ttk.Frame(self.nb)

        self.mb = Menu(master)
        master.config(menu = self.mb)
        file = Menu(self.mb)
        info = Menu(self.mb)

        self.mb.add_cascade(menu = file, label = 'Tools')
        self.mb.add_cascade(menu = info, label = 'Help')

        file.add_command(label='Zip Cracker', command = self.zipframe_create)
        file.add_command(label='Port Scanner', command = self.scanframe_create)
        file.add_command(label='Bot net', command =self.botframe_create)
        info.add_command(label='Usage', command=(lambda:print('Usage')))
        info.add_command(label='About', command=(lambda:print('About')))

    def zipframe_create(self):

        self.nb.add(self.zipframe,text='Zip')
        self.zipframe.config(height=480,width=720)
        zlabel1 = ttk.Label(self.zipframe, text='Select the zip file').grid(row=0,column=0, padx=5, pady=10)
        zlabel2 = ttk.Label(self.zipframe, text='Select the dictionary file').grid(row=2,column=0, padx=5)
        ztext1 = ttk.Entry(self.zipframe, width = 50).grid(row=0,column=1,padx=5,pady=10)
        ztext2 = ttk.Entry(self.zipframe, width = 50).grid(row=2,column=1,padx=5)
        zoutput = Text(self.zipframe, width=80, height=20).grid(row=3,column=0,columnspan = 3,padx=5,pady=10)
        zb1 = ttk.Button(self.zipframe, text='Crack', width=10).grid(row=0,column=2,padx=5,pady=10)


    def scanframe_create(self):

        self.nb.add(self.scanframe,text='Scan')
        self.scanframe.config(height=480,width=720)
        slabel1 = ttk.Label(self.scanframe, text='IP address').grid(row=0,column=0, padx=5, pady=10)
        sin_put = ttk.Entry(self.scanframe, width = 50).grid(row=0,column=1,padx=5,pady=10)
        soutput = Text(self.scanframe, width=80, height=20).grid(row=3,column=0,columnspan = 3,padx=5,pady=10)
        sb1 = ttk.Button(self.scanframe, text='Scan', width=6,command= print('Content: {}'.format(sin_put.get()))).grid(row=0,column=2,padx=5,pady=10)

    def botframe_create(self):

        self.nb.add(self.botframe,text='Bot')
        self.botframe.config(height=480,width=720)
        blabel1 = ttk.Label(self.botframe, text='IP address').grid(row=0,column=0, padx=5, pady=10)
        blabel2 = ttk.Label(self.botframe, text='Username').grid(row=1,column=0, padx=2)
        blabel3 = ttk.Label(self.botframe, text='password').grid(row=2,column=0, padx=2)
        btext1 = ttk.Entry(self.botframe, width = 30).grid(row=0,column=1,padx=5,pady=10)
        btext2 = ttk.Entry(self.botframe, width = 30).grid(row=1,column=1)
        btext2 = ttk.Entry(self.botframe, width = 30).grid(row=2,column=1)
        boutput = Text(self.botframe, width=80, height=20).grid(row=3,column=0,columnspan = 3,padx=5,pady=10)
        bb1 = ttk.Button(self.botframe, text='Connect', width=8).grid(row=2,column=2,padx=5,pady=10)


def main():            

    root = Tk()
    feedback = App(root)
    root.mainloop()

if __name__ == "__main__": main()