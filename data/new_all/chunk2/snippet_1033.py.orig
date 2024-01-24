#Source: https://stackoverflow.com/questions/52043575/attribute-error-window-has-no-object-namee
from tkinter import *


class Window:
    def __init__(self, master):
        self.master = master
        root.title("Sign Up or Login")
        root.minsize(width=300, height=300)
        root.maxsize(width=300,height=300)

        self.login_button = Button(master, text = "Login", width=18,height=4, command=self.LoginPage)
        self.signup_button = Button(master, text = "Sign Up", width=18,height=4, command=self.SignupPage)

        self.login_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.signup_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def LoginPage(self):

        root.title("Login")
        self.login_button.place_forget()
        self.signup_button.place_forget()

        self.text_username = Label(root, text = "Username : ")
        self.text_password = Label(root, text = "Password : ")

        self.usernameE = Entry(root)
        self.passwordE = Entry(root)

        self.text_username.place(relx=0.3, rely= 0.4, anchor=CENTER)
        self.text_password.place(relx=0.3, rely= 0.6, anchor=CENTER)

        self.usernameE.place(relx=0.65,rely= 0.4, anchor=CENTER)
        self.passwordE.place(relx=0.65,rely= 0.6, anchor=CENTER)

        self.submit_button_login = Button(root, text="Submit", command=self.SubmitInfo)
        self.submit_button_login.place(relx=0.7,rely=0.7)



    def SignupPage(self):

        root.title("Sign Up")
        self.login_button.place_forget()
        self.signup_button.place_forget()

        self.text_name = Label(root, text = "Name :")
        self.text_age = Label(root, text = "Age :")
        self.text_username = Label(root, text = "Username :")
        self.text_password = Label(root, text = "Password :")

        self.text_name.place(relx=0.2, rely=0.2, anchor=CENTER)
        self.text_age.place(relx=0.2,rely=0.4, anchor=CENTER)
        self.text_username.place(relx=0.2,rely=0.6,anchor=CENTER)
        self.text_password.place(relx=0.2,rely=0.8,anchor=CENTER)

        self.nameE = Entry(root)
        self.ageE = Entry(root)
        self.usernameE2 = Entry(root)
        self.passwordE2 = Entry(root)

        self.nameE.place(relx= 0.4, rely=0.2)
        self.ageE.place(relx=0.4,rely=0.4)
        self.usernameE2.place(relx=0.4,rely=0.6)
        self.passwordE2.place(relx=0.4,rely=0.8)

        self.submit_button_signup = Button(root, text="Submit", command=self.SubmitInfo)
        self.submit_button_signup.place(relx= 0.7, rely=0.9)

    def SubmitInfo(self):

        self.username_login = self.usernameE.get()
        self.password_login = self.passwordE.get()
        self.name_signup = self.nameE.get()
        self.age_signup = self.ageE.get()
        self.username_signup = self.usernameE2.get()
        self.password_signup = self.passwordE2.get()
        print(self.username_login)


root = Tk()

run = Window(root)

root.mainloop()