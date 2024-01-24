#Source: https://stackoverflow.com/questions/73660841/attributeerror-list-object-has-no-attribute-set-canvas
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def f(x, a, b, c):
    return a*x**2+b*x+c

xlist = np.linspace(-10, 10, num = 1000)
##print(xlist)

a = 5
b = 1
c = 4
ylist = f(xlist, a, b, c)

plt.figure(num = 0, dpi = 120)

ax = plt.plot(xlist, ylist, label = 'f(x)')
print(type(ax))

plt.title('Plotting Example')
plt.xlabel('Distance / ft')
plt.ylabel('Height / ft')
plt.legend()
plt.grid(True)
# plt.show()
# __________________________________________________________________
my_w = tk.Tk()
my_w.geometry('1000x820+50+50')
my_w.title('data view on tk graph')

wrapper1 = tk.LabelFrame(my_w)
wrapper2 = tk.LabelFrame(my_w)
wrapper1.pack(fill="both", expand="yes", padx=5, pady=5)
wrapper2.pack(fill="both", padx=5, pady=5)


canvas = tk.Canvas(wrapper1, bg="#595656", height=200)

canvas.pack(fill="both", expand=True)
# __________________________________________________________________


plot1 = FigureCanvasTkAgg(ax, canvas)
plot1.draw()
plot1.get_tk_widget().pack(fill="both", expand="yes", padx=5, pady=5)

ctrl_frame = tk.Frame(wrapper2, bg='green', height=100)
ctrl_frame.pack(fill="both")

tk.Button(ctrl_frame, text='View', width=15, command=lambda:None).place(relx=0.9, rely=0.5, anchor=tk.E)

my_w.mainloop()