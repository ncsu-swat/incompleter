#Source: https://stackoverflow.com/questions/57064929/typeerror-ord-expected-a-character-but-string-of-length-5-found
from tkinter import *
import tkinter as tk

class loginUser:
    def __init__(self, window, master=None):   
        self.wind = window
        self.wind.title("System F2T")

        #Definicoes de fonte p/ o layout de login
        self.fonteTitulo = ("Arial","10","bold")
        self.fontePadrao = ("Arial", "10")

        self.var = StringVar() #create the var first before you assign them
        self.var2 = StringVar()

        #Labels e campos de texto do sistema de login
        self.userLabel = Label(text="Digite seu usuário:", font=self.fontePadrao,bg="#000",fg="#FFF").place(x=27,y=60)
        self.user = Entry(textvariable=self.var, font=self.fontePadrao,bg="#FFF",fg="#000")
        self.user.place(x=140,y=60,width=110)

        self.senhaLabel = Label(text="Digite sua senha:", font=self.fontePadrao,bg="#000",fg="#FFF").place(x=29,y=90)
        self.senha = Entry(textvariable=self.var2, font=self.fontePadrao,bg="#FFF",fg="#000")
        self.senha.place(x=140,y=90,width=110)

        self.max_user = 1
        self.var.trace("w", self.limiteUsuario)
        self.max_senha = 4
        self.var2.trace("w", self.limiteSenha)

    def limiteUsuario(self,*args):
        u = self.var.get()
        if len(u) == 1 and not 65<=ord(u)<=68 and not 48<=ord(u)<=57: # you can also use *if not u in "ABCD"*
            self.var.set("")
        elif len(u) > 1:
            if not 65<=ord(u[-1])<=68: # retirar ultimo caracter caso nao seja digito
                self.var.set(u[:-1])
            else: # aproveitar apenas os primeiros 5 chars
                self.var.set(u[:self.max_user])

    def limiteSenha(self,*args):
        text = self.var2.get()
        text = ''.join(char for char in text if char in 'ABCD')
        if len(text) == 4 and not 65<=ord(text)<=68 and not 48<=ord(text)<=57: # you can also use *if not u in "ABCD"*
            self.var2.set("")
        elif len(text) > 4:
            if not 65<=ord(text[-1])<=68: # retirar ultimo caracter caso nao seja digito
                self.var2.set(text[:-1])
            else: # aproveitar apenas os primeiros 5 chars
                self.var2.set(text[:self.max_senha])
        print(self.var2.set(text))

if __name__ == "__main__":
    root = Tk()
    root['bg'] = "#000"
    loginUser(root)
    #Tamanho da janela
    root.geometry("330x200")
    root.mainloop()