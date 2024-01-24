#Source: https://stackoverflow.com/questions/55066875/typeerror-register-user-missing-1-required-positional-argument-self
def register_user(self):

    username_info = self.username.get()
    password_info = self.password.get()

    file = open(r"C:\Users\ashita.gadagotti\Desktop\username_info.txt", "w+")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(self, text="Registration Success.Please log in with the new credentials.", fg="green", font=("calibri", 11),command = lambda: master.switch_frame(login_page)).pack()

def login_verify(self):
    username1 = self.username_entry1.get()
    password1 = self.password_entry1.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    logindetails = os.listdir(r"C:\Users\ashita.gadagotti\Desktop\username_info.txt")
    if username1 == logindetails:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                master.switch_frame(SearchPage)
            else:
                tm.showerror("Login error","password has not been recognized")
    else:
        tm.showerror("Login error","User not found!")

class searchpage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="SearchPage").grid(row = 0)
        tk.Entry().grid(row = 1)
        tk.Button(self, text="Search")

if __name__ == "__main__":
    app = SampleApp()
    app.title("Equiniti Search Engine")
    app.geometry('1280x720')
    app.mainloop()