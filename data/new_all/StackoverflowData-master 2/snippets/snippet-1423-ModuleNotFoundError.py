#Source: https://stackoverflow.com/questions/60395009/typeerror-argument-should-be-integer-or-none-not-str-error-while-making-sign
import tkinter
from tkinter import messagebox
from tkinter import StringVar


class panel:
    def ask(self):
        ask = tkinter.Tk()
        ask.title("Input")
        ask.geometry("300x100")

        def y():
            ask.destroy()
            self.login()
        def n():
            ask.destroy()
            self.signup()


        stat = tkinter.Label(ask , text = "Are You An Existing User?")
        stat.grid(row = 0 , column = 0)
        yes = tkinter.Button(ask, text = "Yes" , bg = "Blue" , fg = "Black" , command = y, bd = 5 )
        yes.grid(row = 1 , column = 1)
        no = tkinter.Button(ask, text = "No" , bg = "Blue", fg = "Black" , command = n, bd = 5)
        no.grid(row = 1 , column = 2)

        ask.mainloop()

    def signup(self):
        window = tkinter.Tk()
        window.title("Registration Form")
        window.geometry("300x300")

        var = StringVar()

        def callback():
            file = open("information.txt", "a")
            file.write("\r")
            file.write("Data: ")
            file.write(firstname1.get())
            file.write(" ")
            file.write(lastname1.get())
            file.write("\n")
            file.write(firstname1.get())
            file.write("\n")
            file.write(lastname1.get())
            file.write("\n")
            file.write(email1.get())
            file.write("\n")
            file.write(password1.get())
            file.write("\n")
            file.write(var.get())
            file.write("\r")
            file.close()
            messagebox.showinfo("Signup", "You have Successfully Signed Up")
            self.login()

        firstname = tkinter.Label(window, text= "First Name", bg = "Black",fg = "White")
        firstname.grid(row= 0, column= 0)
        firstname1= tkinter.Entry(window,bd= 5)
        firstname1.grid(row= 0 , column = 1)
        lastname = tkinter.Label(window, text = "Last Name", bg = "Black", fg = "White")
        lastname.grid(row = 1, column = 0)
        lastname1= tkinter.Entry(window, bd = 5)
        lastname1.grid(row = 1, column = 1)

        email = tkinter.Label(window, text = "Email", bg = "Black", fg = "White")
        email.grid(row = 2, column = 0)
        email1 = tkinter.Entry(window, bd = 5)
        email1.grid(row = 2 , column = 1)

        password = tkinter.Label(window, text = "Password" , bg = "Black", fg = "White")
        password.grid(row = 3 , column = 0)
        password1= tkinter.Entry(window, bd = 5)
        password1.grid(row = 3 , column = 1)

        gender= tkinter.Label(window, text = "Gender", bg = "Black", fg = "White")
        gender.grid(row = 4 , column = 0)
        male = tkinter.Radiobutton(window,text= "Male" , value = "Male", variable = var )
        male.grid(row = 4 , column = 1 , sticky = "nsew")
        female = tkinter.Radiobutton(window,text= "Female" , value= "Female" , variable = var)
        female.grid(row = 4, column = 2 , sticky = "nsew")



        button = tkinter.Button(window, text = "Submit" ,command = callback , bg = "Blue", fg = "White" , height = 2, width = 14)
        button.grid(row = 5  , column = 1 , rowspan= 315)



        window.mainloop()

    def login(self):
        signin = tkinter.Tk()
        signin.title("Sign In")
        signin.geometry("300x300")

        def callback():
            file = open("information.txt" , "r")
            e = file.read(x1.get())
            print(e)
            p = file.read(y1.get())
            print(p)
            if e in file and p in file:
                messagebox.showinfo("SignIn Notification", "You are Successfully Signed In")
            else:
                messagebox.showerror("Error", "Email or Password is Incorrect")
            file.close()


        x = tkinter.Label(signin, text = "Email", bg = "Black", fg = "White" )
        x.grid(row =  0 , column = 0)
        x1 = StringVar(tkinter.Entry(signin, bd = 5).grid(row = 0 , column = 1))
        y = tkinter.Label(signin, text = "Password", bg = "Black", fg = "White")
        y.grid(row = 1 , column = 0)
        y1 = StringVar(tkinter.Entry(signin, bd = 5).grid(row = 1 , column = 1))


        login = tkinter.Button(signin, text = "Sign In" , bd = 5, bg = "Blue" , fg = "Black", height = 2 , width = 10, command = callback )
        login.grid(row  = 2 , column = 1, rowspan = 2)

        signin.mainloop()


def main():
    p  = panel()
    p.ask()
main()