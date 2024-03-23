#Source: https://stackoverflow.com/questions/66913415/return-self-tk-callself-w-cget-key-typeerror-can-only-concatenate
from tkinter import *

def calcular():
    mars = (peso.get()*3.7)/9.8

  
    if "Marte" in planeta:
        res.set("Tu peso en el planeta " + str(planeta.get()) + " es: " + str(mars))
        


        

ventana = Tk()
#StringVar , IntVar, DoubleVar
peso = IntVar()
planeta = StringVar()
res = StringVar()
ventana.geometry("400x300")




#Etiqueta
textoN = Label(ventana,text="Escribe un numero: ")
textoN.place(x=150,y=10)

#Caja de texto
pesoentry = Entry(ventana,textvariable=peso)
pesoentry.place(x=150,y=40)

planeta = Entry(ventana,textvariable=planeta)
planeta.place(x=150,y=60)

#Etiqueta Resultado
textoR = Label(ventana,textvariable=res)
textoR.place(x=150,y=140)

#Boton
boton = Button(ventana,text="Calcular",command=calcular,bg="#006",fg="white")
boton.place(x=180,y=100)
ventana.mainloop()