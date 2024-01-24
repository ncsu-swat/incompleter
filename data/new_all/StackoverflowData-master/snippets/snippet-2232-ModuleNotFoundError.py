#Source: https://stackoverflow.com/questions/56453398/attributeerror-stringvar-object-has-no-attribute-tk
from tkinter import *
from tkinter import ttk
import tkinter as tk

class loginUser:
    def __init__(self, window, master=None):   
        self.wind = window
        self.wind.title("System F2T")

        #Definicoes de fonte p/ o layout de login
        self.fonteTitulo = ("Arial","10","bold")
        self.fontePadrao = ("Arial", "10")

        self.var = tk.StringVar()
        self.var2 = tk.StringVar()

        self.userLabel = Label(text="Digite seu usuário:", font=self.fontePadrao,bg="#000",fg="#FFF").place(x=27,y=60)
        self.user = Entry(textvariable=self.var, font=self.fontePadrao,bg="#FFF",fg="#000")
        self.user.place(x=140,y=60,width=110)

        self.senhaLabel = Label(text="Digite sua senha:", font=self.fontePadrao,bg="#000",fg="#FFF").place(x=29,y=90)
        self.senha = Entry(self.var2, font=self.fontePadrao,show="*",bg="#FFF",fg="#000")
        self.senha.place(x=140,y=90,width=110)

    def limiteUsuario(self,*args):
        u = self.var.get()
        if len(u) == 1 and not 65<=ord(u)<=68: # you can also use *if not u in "ABCD"*
            self.var.set("")
        elif len(u) > 1:
            if not 65<=ord(u[-1])<=68: # retirar ultimo caracter caso nao seja digito
                self.var.set(u[:-1])
            else: # aproveitar apenas os primeiros 5 chars
                self.var.set(u[:self.max_user])

    def limiteSenha(self,*args):
        s = self.var2.get()
        if len(s) > 4:
            if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
                self.var2.set(s[:-1])
            else: # aproveitar apenas os primeiros 5 chars
                self.var2.set(s[:self.max_senha])

if __name__ == "__main__":
    root = Tk()
    root['bg'] = "#000"
    loginUser(root)
    #Tamanho da janela
    root.geometry("330x200")
    root.mainloop()