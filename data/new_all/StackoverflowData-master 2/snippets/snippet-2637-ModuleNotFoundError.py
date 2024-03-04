#Source: https://stackoverflow.com/questions/68196436/attributeerror-event-object-has-no-attribute-x-win-error
import os 
import tkinter as tk
from tkinter import *
from tkinter import font

win = tk.Tk()
win.overrideredirect(1)





# def realcenter( o, w, h ) ->'o(w,h) centered on screen':
#     x = o.winfo_screenwidth( ) - w
#     y = o.winfo_screenheight( ) - h
#     o.geometry( f'{w}x{h}+{int( x/2 )}+{int( y/2 )}' )

# def restore( ev ):
#     win.overrideredirect( 0 )

# def unrestore( ev ):
#     win.overrideredirect( 1 )

# win.geometry( '500x525' )
# realcenter( win, 500, 525)

# win.update_idletasks()

# win.overrideredirect( 1 )

# win.bind( '<F1>', restore )
# win.bind( '<F2>', unrestore )

font1 = font.Font(family = 'Helvetica', size = 15)
font3 = font.Font(family = 'Helvetica', size = 8, weight = 'bold')
font2 = font.Font(family = 'Helvetica', size = 20, weight = 'bold')

def aaa(colora, colorb, colorc, colord, colore, colorf):
    Dark = Theme('#18181F','#0C0C0F',"#505063",'#D1DDFF','#D12319',"#D1665F")
    Ecrire('',Light)

def aaaa(colora, colorb, colorc, colord, colore, colorf):
    Light = Theme('#F1EDF5','#D1D2E8',"#EDD5EB",'#323133','#6F2EB0',"#C47ED6")
    Ecrire('',Dark)

def strl(list):
    
        list ="".join(list)
        return list



# menubar = Menu(win)
# win.config(menu=menubar)
# menufichier = Menu(menubar,tearoff=0)
# menubar.add_cascade(label="Theme", menu=menufichier) 
# menufichier.add_command(label=" Dark mode",font = font3,command =lambda: aaa('#18181F','#0C0C0F',"#505063",'#D1DDFF','#D12319',"#D1665F"))
# menufichier.add_command(label=" Light mode",font = font3,command =lambda: aaaa('#F1EDF5','#D1D2E8',"#EDD5EB",'#323133','#6F2EB0',"#C47ED6"))
 
pixel = tk.PhotoImage(width=1, height=1)

a =95
b =95

theme = 0
t = 0

ecrit = []
nombre_de_multdiv = 0
nombre_de_sous_add = 0

def Del(self):
    global ecrit
    del ecrit[-1]
    affichage = strl(ecrit)
    self.label1['text'] = affichage
    self.label1.place(anchor = 'e', x = 450, y = 75)

def Del_all(self):
    global ecrit
    del ecrit[:]
    affichage = strl(ecrit)
    self.label1['text'] = affichage
    self.label1.place(anchor = 'e', x = 450, y = 75)

def Ecrire(symbole,self):

    ecrit.append(symbole)
    affichage = strl(ecrit)
    self.label1['text'] = affichage
    self.label1.place(anchor = 'e', x = 450, y = 75)


def Ecrire_Resulat(valeur,self):
    valeur = strl(valeur)
    self.label1['text'] = valeur

def Calcul(self):
    global nombre_de_multdiv
    global nombre_de_sous_add

    for i in range(len(ecrit)):
        if ecrit[i]  == '/' or ecrit[i] == '*':
            nombre_de_multdiv +=1
    for i in range(len(ecrit)):
        if ecrit[i]  == '+' or ecrit[i] == '-':
            nombre_de_sous_add +=1

    for i in range(nombre_de_multdiv):

        for i in range(len(ecrit)):
            if ecrit[i] == '*' or ecrit[i] == '/':

                numero = i
                nb = i
                nbb = i

                for i in range(len(ecrit)-numero-1):

                    if ecrit[i+1 + numero] != '/' and ecrit[i+1 + numero] != '*' and ecrit[i+1 + numero] != '+' and ecrit[i+1 + numero] != '-':

                        nb +=1

                    elif ecrit[i+1+numero] == '/' or ecrit[i+1+numero] == '*' or ecrit[i+1+numero] == '+' or ecrit[i+1+numero] == '-':

                        break 

                for i in range(numero):

                    i = -i

                    if ecrit[i-1+numero] != '/' and ecrit[i-1+numero] != '*' and ecrit[i-1+numero] != '+' and ecrit[i-1+numero] != '-':

                        nbb -=1

                    elif ecrit[i-1+numero] == '/' or ecrit[i-1+numero] == '*' or ecrit[i-1+numero] == '+' or ecrit[i-1+numero] == '-':

                        break 

                nombre1 = "".join(ecrit[numero+1:nb+1])
                nombre1 = float(nombre1)
                nombre2 = "".join(ecrit[nbb:numero])
                nombre2 = float(nombre2)

                if ecrit[numero] =='*':
                    resultat = nombre1 * nombre2

                    if resultat == int(resultat):
                        resultat = int(resultat)

                    resultat = list(str(resultat))


                else:
                    resultat = nombre2 / nombre1

                    if resultat == int(resultat):
                        resultat = int(resultat)

                    resultat = list(str(resultat))

                del ecrit[nbb:nb+1]
                for i in range(len(resultat)):

                    ecrit.insert(nbb+i,resultat[i])
                    
                break

    for i in range(nombre_de_sous_add):

        for i in range(len(ecrit)):
            if ecrit[i] == '+' or ecrit[i] == '-':

                numero = i
                nb = i
                nbb = i

                for i in range(len(ecrit)-numero-1):


                    if ecrit[i+1 + numero] != '/' and ecrit[i+1 + numero] != '*' and ecrit[i+1 + numero] != '+' and ecrit[i+1 + numero] != '-':

                        nb +=1

                    elif ecrit[i+1+numero] == '/' or ecrit[i+1+numero] == '*' or ecrit[i+1+numero] == '+' or ecrit[i+1+numero] == '-':

                        break 

                for i in range(numero):

                    i = -i

                    if ecrit[i-1+numero] != '/' and ecrit[i-1+numero] != '*' and ecrit[i-1+numero] != '+' and ecrit[i-1+numero] != '-':

                        nbb -=1

                    elif ecrit[i-1+numero] == '/' or ecrit[i-1+numero] == '*' or ecrit[i-1+numero] == '+' or ecrit[i-1+numero] == '-':

                        break 

                nombre1 = "".join(ecrit[numero+1:nb+1])
                nombre1 = float(nombre1)
                nombre2 = "".join(ecrit[nbb:numero])
                nombre2 = float(nombre2)

                if ecrit[numero] =='+':
                    resultat = nombre1 + nombre2

                    if resultat == int(resultat):
                        resultat = int(resultat)

                    resultat = list(str(resultat))


                else:
                    resultat = nombre2 - nombre1

                    if resultat == int(resultat):
                        resultat = int(resultat)

                    resultat = list(str(resultat))

                del ecrit[nbb:nb+1]

                for i in range(len(resultat)):

                    ecrit.insert(nbb+i,resultat[i])

                break
    Ecrire_Resulat(ecrit,self)


class Theme():

    def move_window(self,event):
        # global x, y
        print(self.x, self.y)
        win.geometry('+{0}+{1}'.format(event.x_win - self.x, event.y_win - self.y))

    def set_xy(self,event):

        self.x=event.x_win - win.winfo_x()
        self.y=event.y_win - win.winfo_y()
        # print(x,y)
        return self.x,self.y;

    def boutontheme(self,colora, colorb, colorc, colord, colore, colorf):
        self.openmenu(colora, colorb, colorc, colord, colore, colorf)
        if self.t == 0:
            Light = Theme('#F1EDF5','#D1D2E8',"#EDD5EB",'#323133','#6F2EB0',"#915ec4")
            self.t = 1
        else:
            Dark = Theme('#18181F','#0C0C0F',"#505063",'#D1DDFF','#D12319',"#D1665F")
            self.t = 0



    def openmenu(self,colora, colorb, colorc, colord, colore, colorf):
        if self.ouvert == False:
            self.b_theme.config(bg = colore)
            if self.t == 0:
                self.b_theme_dark = tk.Button(win,state=DISABLED, text = 'Dark theme',font = font3,borderwidth=0, highlightthickness=0,compound="c",image = pixel,height = 20,width = 70,activebackground =colore,bg =colora,fg = colord,command = lambda: self.boutontheme(colora, colorb, colorc, colord, colore, colorf))
                self.b_theme_light = tk.Button(win,state=NORMAL, text = 'Light theme',font = font3,borderwidth=0, highlightthickness=0,compound="c",image = pixel,height = 20,width = 70,activebackground =colore,bg =colora,fg = colord,command = lambda: self.boutontheme(colora, colorb, colorc, colord, colore, colorf))
            else:
                self.b_theme_dark = tk.Button(win,state=NORMAL, text = 'Dark theme',font = font3,borderwidth=0, highlightthickness=0,compound="c",image = pixel,height = 20,width = 70,activebackground =colore,bg =colora,fg = colord,command = lambda: self.boutontheme(colora, colorb, colorc, colord, colore, colorf))
                self.b_theme_light = tk.Button(win,state=DISABLED, text = 'Light theme',font = font3,borderwidth=0, highlightthickness=0,compound="c",image = pixel,height = 20,width = 70,activebackground =colore,bg =colora,fg = colord,command = lambda: self.boutontheme(colora, colorb, colorc, colord, colore, colorf))
            
            self.b_theme_dark.place(anchor = 'nw', x = 5, y = 25)
            self.b_theme_light.place(anchor = 'nw', x = 5, y = 45) 
            self.ouvert = True
            return;

        if self.ouvert == True:
            self.b_theme.config(bg = colorb)
            self.b_theme_dark.destroy()
            self.b_theme_light.destroy()
            self.ouvert = False 
            return;


    # def closemenu(self):
    #   self.b_theme_dark.forget()
    #   self.b_theme_light.forget()

    #   ouvert = False 


    def __init__(self,colora, colorb, colorc, colord, colore, colorf):

        
        if colora == '#18181F':
            self.t = 0
        else:
            self.t = 1

        self.ouvert = False
        self.x = 0
        self.y=0

        #creation menu

        self.canvas_menu = Canvas(win, width =500, height =25, bg = colora, borderwidth=0, highlightthickness=0)
        self.exit = Canvas(bg = colora,borderwidth=0, highlightthickness=0)
        self.exit.create_oval(0,0,20,20, fill= colore,width = 0)
        self.exit.create_text(10, 10, text="x", fill = colord, font= font3)
        self.exit.bind("<Button-1>", lambda e: win.destroy())

        #affichage menu

        self.exit.place(anchor = 'nw', x = 475, y = 2)
        self.canvas_menu.grid(row = 0,column = 0, columnspan = 5)

        #creation des canvas

        self.canvas_screen = Canvas(win, width =500, height =100, bg =colorb,borderwidth=0, highlightthickness=0)
        self.canvas_keyb_num = Canvas(win, width =300, height =400, bg =colorb,borderwidth=0, highlightthickness=0)
        self.canvas_keyb_op = Canvas(win, width =200, height =400, bg =colorb,borderwidth=0, highlightthickness=0)

        #affchage des canvas

        self.canvas_screen.grid(row = 1,column = 0, columnspan = 5)
        self.canvas_keyb_num.grid(row = 2,column = 0, columnspan = 3, rowspan = 4)
        self.canvas_keyb_op.grid(row = 2,column = 3, columnspan = 2, rowspan = 4)

        # creation des boutons

        self.b1 = Button(win, text ='1',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('1',self))
        self.b2 = Button(win, text ='2',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('2',self))
        self.b3 = Button(win, text ='3',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('3',self))
        self.b4 = Button(win, text ='4',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('4',self))
        self.b5 = Button(win, text ='5',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('5',self))
        self.b6 = Button(win, text ='6',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('6',self))
        self.b7 = Button(win, text ='7',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('7',self))
        self.b8 = Button(win, text ='8',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('8',self))
        self.b9 = Button(win, text ='9',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('9',self))
        self.b_point = Button(win, text ='.',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('.',self))
        self.b0 = Button(win, text ='0',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('0',self))
        
        self.b_plus = Button(win, text ='+',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('+',self))
        self.b_moins = Button(win, text ='-',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('-',self))
        self.b_fois = Button(win, text ='*',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('*',self))
        self.b_diviser = Button(win, text ='/',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Ecrire('/',self))
        self.b_del = Button(win, text ='DEL',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Del(self))
        self.b_del_all = Button(win, text ='CE',borderwidth=0, highlightthickness=0, bg = colora,activebackground =colorc,foreground=colord,compound="c",image = pixel,height = a,width = b ,font = font1,command=lambda: Del_all(self))
        self.b_egale = Button(win, text ='=',borderwidth=0, highlightthickness=0, bg = colore,activebackground =colorf,foreground=colord,compound="c",image = pixel,height = a,width = 295 ,font = font1,command= lambda: Calcul(self))

        #affichage des nombres

        #colone 1

        self.b7.grid(column = 0, row = 2)
        self.b4.grid(column = 0, row = 3)
        self.b1.grid(column = 0, row = 4)
        self.b_point.grid(column = 0, row = 5)

        #colone 2

        self.b8.grid(column = 1, row = 2)
        self.b5.grid(column = 1, row = 3)
        self.b2.grid(column = 1, row = 4)
        self.b0.grid(column = 1, row = 5)

        #colone 3

        self.b9.grid(column = 2, row = 2)
        self.b6.grid(column = 2, row = 3)
        self.b3.grid(column = 2, row = 4)

        #operateurs

        self.b_plus.grid(column = 3, row = 2)
        self.b_moins.grid(column = 4, row = 2)
        self.b_fois.grid(column = 3, row = 3)
        self.b_diviser.grid(column = 4, row = 3)
        self.b_del.grid(column = 3, row = 4)
        self.b_del_all.grid(column = 4, row = 4)
        self.b_egale.grid(column = 2, row = 5,columnspan = 3)

        #ecriture

        self.label1 = tk.Label(win, text = '', justify = tk.RIGHT,font = font2,bg =colorb,fg = colord)
        self.label1.place(anchor = 'e', x = 450, y = 75)
        self.b_theme = tk.Button(win, text = 'Themes',font = font3,bg =colorb,fg = colord,borderwidth=0, highlightthickness=0,compound="c",image = pixel,height = 20,width = 50,activebackground =colore,command= lambda: self.openmenu(colora, colorb, colorc, colord, colore, colorf))
        self.b_theme.place(anchor = 'nw', x = 5, y = 2)

        self.canvas_menu.bind('<1>', self.set_xy)

        # bind title bar motion to the move window function

        self.canvas_menu.bind('<B1-Motion>', self.move_window)

        # b_theme_dark.config(bg =colorb,fg = colord, activebackground =colore)
        # b_theme_light.config(bg =colorb,fg = colord, activebackground =colore)

        # menufichier.config(activebackground = colorc,bg = colora,fg = colord)


if theme == 0:
    Dark = Theme('#18181F','#0C0C0F',"#505063",'#D1DDFF','#D12319',"#D1665F")
else:
    Light = Theme('#F1EDF5','#D1D2E8',"#EDD5EB",'#323133','#6F2EB0',"#915ec4")

win.title('calculator')






#pour un future menu 

# bouton.config(state=DISABLED)
# bouton.config(state=NORMAL)

win.resizable(height=False,width=False)
win.mainloop()