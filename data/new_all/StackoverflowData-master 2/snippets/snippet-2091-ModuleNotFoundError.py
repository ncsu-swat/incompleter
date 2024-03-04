#Source: https://stackoverflow.com/questions/64760434/attribute-error-function-error-has-no-attribute-play-on-tkinter-and-pygame
import tkinter
from tkinter import messagebox
import pygame
import random

def son1 ():#function that plays a sound (son1)
    pygame.mixer.init()
    global son1
    son1 = pygame.mixer.Sound("Gun_Cocking.wav")
    son1.play()
def son2 ():#function that plays a sound (son2)
    pygame.mixer.init()
    global son2
    son2 = pygame.mixer.Sound("Gunshot.wav")
    son2.play()
def gachette():#if r=1 son2 plays, if r!=1 son1plays
    global son1, son2
    r=random.randint(1,6)
    if r==1:
        label1.configure(text="BAM! T'as tiré hahahaha, t'es ded!",font=("Comic Sans Ms",18),foreground="red")
        son2.play()
        bouton01.destroy()
    else:
        label1.configure(text="Clic! T'as survécu, tu continues hahaha" )
        son1.play()

fenetre=tkinter.Tk()
fenetre.title("La roulette russe")
fenetre.geometry("600x600")
fenetre.configure(background="black")
espace_dessin=tkinter.Canvas(fenetre,background="black", height=600, width=600)
espace_dessin.pack()
label0=tkinter.Label(fenetre,text="JEU DE LA ROULETTE RUSSE",font=("Arial",20),foreground="black")
label0.configure(background="white")
label0.pack()
label0.place(x=115,y=20)

label1=tkinter.Label(fenetre, text="T'es toujours vivant, félicitations...!", font=("Comic Sans Ms",18),foreground="green")
label1.configure(background="black")
label1.pack()
label1.place(x=110,y=200)

label2=tkinter.Label(fenetre, text="Tu poses le bout du canon sur ta tempe et ...", font=("Arial",18),foreground="grey")
label2.configure(background="black")
label2.pack()
label2.place(x=70,y=300)

bouton01=tkinter.Button(fenetre,text="Tirer",command=gachette,font=("Arial",16),relief="groove")
bouton01.pack()
bouton01.place(x=260,y=350)


fenetre.mainloop()