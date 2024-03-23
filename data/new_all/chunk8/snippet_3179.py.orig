#Source: https://stackoverflow.com/questions/22268627/typeerror-when-developing-tkinter-notepad-like-application-in-python-3
from tkinter import *
top=Tk()
top.title('Mypad')
def save(self,s):
    self.s=filedialog.asksaveasfilename(defaultextension='.txt')
    c=open(self.s,'w')
    w=c.write(str(e.get('1.0','end')))
def close():
    top.destroy()
menubar=Menu(top)
file=Menu(menubar,tearoff=0)
vet=file.add_command(label='Save',command=save)
file.add_separator()
file.add_command(label='Exit',command=close)
menubar.add_cascade(label='File',menu=file)
e=Text()
e.pack(ipady=30)
top.config(menu=menubar)
top.mainloop()