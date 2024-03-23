#Source: https://stackoverflow.com/questions/57134375/attributeerror-users-arduino-object-has-no-attribute-progressbar
from tkinter import *
from tkinter import ttk
import time

class users_Arduino:

    def __init__(self,window):
        self.wind = window
        self.wind.title("System F2T - Cadastro Arduino")

        menubar = Menu(window)
        arduino = Menu(menubar,tearoff=0)
        menubar.add_cascade(label = "Arduino",menu=arduino)
        arduino.add_command(label = "Conectar/Inserir dados-BD", command=self.getSerialData)
        window.config(menu = menubar)

    def bar(): 
        progress['value'] = 20
        root.update_idletasks() 
        time.sleep(1) 

        progress['value'] = 40
        root.update_idletasks() 
        time.sleep(1) 

        progress['value'] = 50
        root.update_idletasks() 
        time.sleep(1) 

        progress['value'] = 60
        root.update_idletasks() 
        time.sleep(1) 

        progress['value'] = 80
        root.update_idletasks() 
        time.sleep(1) 
        progress['value'] = 100   

    def getSerialData(self):
        self.progresso = Toplevel()
        self.progresso.title("System F2T - Progress")
        self.progresso.geometry("290x200")
        #self.progresso["bg"] = "#000"
        progress = self.Progressbar(self.progresso,orient = HORIZONTAL, length = 100, mode = 'determinate').pack(pady = 10) 
        Button(self.progresso, text = 'Start', command = self.bar).pack(pady = 10) 

if __name__ == '__main__':
    window = Tk()
    window['bg'] = "#000"
    users_Arduino(window)
    window.mainloop()