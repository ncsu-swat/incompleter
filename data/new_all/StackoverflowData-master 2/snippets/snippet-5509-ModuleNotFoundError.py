#Source: https://stackoverflow.com/questions/64357846/nameerror-name-win-is-not-defined-with-tkinter-python
import tkinter as tk
from tkinter import *
def zui(kaj,saj):
    zun=kaj
    kaj=kaj+"=tk.Tk()"
    exec(kaj)
    saj=zun+".title('"+saj+"')"
    exec(saj)
def zabel(self,naj,iaj,oaj,baj,gaj,taj):
    spsp=self+"="+"Label("+naj+", text='"+iaj+"', bg='"+oaj+"', height="+gaj+", width="+taj+",fg='"+baj+"')"
    spsp=str(spsp)
    exec(spsp)
def zosition(qak,iak,nak):
    sspp=qak+".grid(row="+iak+", column="+nak+")"
    exec(sspp)
def zainzoop(tak):
    sft=tak+".mainloop()"
    exec(sft)
zui("win","zahid app")
zabel("label","win","hello world","white","black","4","10")
zosition("win","1","1")
zainzoop("win")