#Source: https://stackoverflow.com/questions/67506988/attributeerror-function-object-has-no-attribute-destroy
from tkinter import *
import os


def fechar():
    tela_principal.destroy()


def tela_clientes():
    fechar()
    exec(open('cadastro_cliente.py').read(), {'c': tela_principal})


def tela_carros():
    pass


tela_principal = Tk()
tela_principal.title('Principal')
tela_principal.geometry('400x300+250+50')

fr_logo = Frame(tela_principal, borderwidth=1, relief='solid')
fr_logo.place(x=10, y=10, width=380, height=180)

btn_cliente = Button(
    tela_principal, text='CADASTRO\nCLIENTE', command=tela_clientes)
btn_cliente.place(x=30, y=220, width=100, height=50)

btn_carros = Button(tela_principal, text='PESQUISA\nCARROS',
                    command=tela_carros)
btn_carros.place(x=150, y=220, width=100, heigh=50)

btn_sair = Button(tela_principal, text='SAIR', command=fechar)
btn_sair.place(x=270, y=220, width=100, height=50)


tela_principal.mainloop()