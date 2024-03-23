#Source: https://stackoverflow.com/questions/72591020/i-am-trying-to-create-a-password-generator-and-i-keep-getting-this-error-typee
import random
from tkinter import *
from typing import Tuple

root = Tk()

input_box = Entry(root, width=22, borderwidth=2, bg="#000000")
input_box.grid(row=0, column=0, columnspan=2)
input_box.insert(0, 'Enter the password length:', )
random_password = ()

def password_generator():
    character_list = ("""QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm
    1234567890`~!@#$%^&*()_+[]\{}|;':",./<>?""")
    num_of_runs = 1
    random_password = ()
    password_length = int(input_box.get())
    while num_of_runs <= int(password_length):
        random_password += character_list[random.randint(0, 91)]
        num_of_runs += 1
    Label(random_password).grid(row=2, column=0)


my_button = Button(root, text="Click here for your password", 
               command=password_generator, fg="#000000", bg="white", )
my_button.grid(row=1, column=0, columnspan=2)

root.mainloop()