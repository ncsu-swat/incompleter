#Source: https://stackoverflow.com/questions/67339079/attributeerror-function-object-has-no-attribute-insert-while-writting-tkint
#So after clicking for ex. button with "5" fucnction has to write 5 on calc

import tkinter as tk

symbols=["7", "8", "9", "/", "\u21BA","4", "5", "6", "*", "C", "1", "2", "3", "-", "x^2", "0", "+", "\u221A"]

def window():
    root=tk.Tk()

    root.configure(bg="light gray")

    root.geometry('460x430')

    root.title("Kalkurator ONP")

    return root

def screen(root):

    screen=[tk.Label(root, width=65, anchor="w", borderwidth=2, bg='#C0CBCB') for i in range(3)]

    for i in range(len(screen)):

        #ipadx and ipady are margins
        screen[i].grid(row=i, columnspan=5, ipady=15, ipadx=1)

    return screen

def dataLabel(root, screen):
    label_for_data=tk.Entry(root, borderwidth=0, highlightcolor="white", highlightbackground="white")
    label_for_data.grid(row=len(screen), columnspan=5, ipadx=160, ipady=10)

    info=tk.Label(root, width=65, anchor="w", borderwidth=2, bg='white')
    info.grid(row=len(screen)+1, columnspan=5, ipady=15, ipadx=1)

    return label_for_data, info

def afterClickingBtn(lfd, symbol):
    def f():
        lfd.insert(tk.END, symbol)#Here is the problem
    return f

def buttons(root, screen):

    j=len(screen)+2

    button=[tk.Button(root, text=symbol, bg="light gray", borderwidth=0) for symbol in symbols]
    for i in range(len(symbols)):
        if i%5==0:
            j+=1
        button[i].grid(row=j, column=i%5, ipadx=15, ipady=10)
        button[i].configure(command=afterClickingBtn(dataLabel, button[i]["text"]))

    equal_button=tk.Button(root, text="=", bg="green", borderwidth=0)
    equal_button.grid(row=len(screen)+6, column=3, columnspan=2, ipadx=60, ipady=10)

    return button, equal_button
    

def main():
    root=window()

    sc=screen(root)

    lfd=dataLabel(root, sc)
    
    btn=buttons(root, sc)

    #End of loop
    root.mainloop()

if __name__=="__main__":
    main()