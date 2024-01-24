#Source: https://stackoverflow.com/questions/61533489/nameerror-name-username-is-not-defined-in-python-with-tkinter-gui
#26/4/2020 28/4/2020 30/4/2020

def sign_in_clicked():
    username = username_entry.get()
    password = password_entry.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

from tkinter import *

sign_in = Tk()
sign_in.title("Sign in")

sign_in_label = Label(sign_in,text="Please Sign In!").grid(row=0, column=0, columnspan=2, sticky=W)
username_label = Label(sign_in,text="Username:").grid(row=1, column=0, sticky=W)
password_label = Label(sign_in,text="password:").grid(row=2, column=0, sticky=W)

username_entry = Entry(sign_in, width=20, bg="gray70")
username_entry.grid(row=1, column=1, sticky=W)
password_entry = Entry(sign_in, width=20, bg="gray70")
password_entry.grid(row=2, column=1, sticky=W)

sign_in_button = Button(sign_in, text="Sign In", width=25, command=sign_in_clicked).grid(row=3, column=0, columnspan=2, sticky=W)

output_text = Text(sign_in, width=23, height=6, wrap=WORD, background="DarkOrchid1")
output_text.grid(row=6, column=0, columnspan=2, sticky=W)

if username=="1" and password=="2":
    output_text.insert(END, "hi")

sign_in.mainloop()