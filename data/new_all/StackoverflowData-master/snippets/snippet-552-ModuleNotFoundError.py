#Source: https://stackoverflow.com/questions/56791883/typeerror-can-only-concatenate-str-not-set-to-str
import visa
import tkinter as tk


rm = visa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('TCPIP::192.168.100.200::INSTR')

#This one would work, after i bind the function to the button,
#i just press it and it passes the preset value. 
#All i want to do is pass a value through the Entry widget, 
#instead of having a set one.
#freq = str(250000) 
#def freqset_smb100a():
    #inst.write("SOUR:FREQ:CW " + freq)

inst.write("OUTP ON")

def freqset_smb100a():
    inst.write(f"SOUR:FREQ:CW " + {str(input_var.get())})



HEIGHT = 400
WIDTH = 600

root = tk.Tk()

input_var = tk.StringVar()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Set Freq", font=40, command=freqset_smb100a)
button.place(relx=0.7, relheight=1, relwidth=0.3)

entry = tk.Entry(frame, font=15, textvariable=str(input_var.get))
entry.place(relx=0.35, relheight=1, relwidth=0.3)


root.mainloop()