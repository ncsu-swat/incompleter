#Source: https://stackoverflow.com/questions/55876187/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
import tkinter as tk

window9 = tk.Tk()
msrp = tk.IntVar()
amgpage = tk.Label(window9, text="Mercedes Benz AMG Depreciation Calculator").pack(anchor='center')

amgpage = tk.Label(window9, text="What is the MSPR of the car?: ")
amgpage.pack()

msrp = tk.Entry(window9)
msrp.pack()

msrp.focus_set()

def callback():
    value=(msrp.get())

b = tk.Button(window9, text="Save your msrp value", command=callback,fg="red")
b.pack()
amgpage = tk.Label(window9, text="What is the age of the car?: ")
amgpage.pack()

old = tk.Entry(window9)
old.pack()
old.focus_set()
def callback2():
    age=(old.get())

b = tk.Button(window9, text="Save the age of the car", command=callback2,fg="blue")
b.pack()    
amgpage = tk.Label(window9, text="")
amgpage.pack(anchor='w')
def msrpv():
    m = callback()
    p = int(m)
    a = callback2()
    n = int(a)
    a=p*(1-0.15)**n
    amgpage=tk.Label(window9,text="$"+a)
    amgpage.pack()


amgmsrp = tk.Button(window9, text="Get the current value of the car.", command=msrpv,fg="green")
amgmsrp.pack()


window9.geometry("400x400")

window9.title("Mercedes Benz AMG Depreciation Calculator")

window9.mainloop()