# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64760434/attribute-error-function-error-has-no-attribute-play-on-tkinter-and-pygame
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter
    _l_(571850)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(571852)

except ImportError:
    pass
try:
    import pygame
    _l_(571854)

except ImportError:
    pass
try:
    import random
    _l_(571856)

except ImportError:
    pass

def son1 ():
    _l_(571872)

    _c_(571860, _a_(571859, _a_(571858, _n_(571857, "pygame", lambda: pygame), "mixer"), "init"))
    _l_(571861)
    global son1
    _l_(571862)
    son1 = _c_(571866, _a_(571865, _a_(571864, _n_(571863, "pygame", lambda: pygame), "mixer"), "Sound"), "Gun_Cocking.wav")
    _l_(571867)
    _c_(571870, _a_(571869, _n_(571868, "son1", lambda: son1), "play"))
    _l_(571871)
def son2 ():
    _l_(571888)

    _c_(571876, _a_(571875, _a_(571874, _n_(571873, "pygame", lambda: pygame), "mixer"), "init"))
    _l_(571877)
    global son2
    _l_(571878)
    son2 = _c_(571882, _a_(571881, _a_(571880, _n_(571879, "pygame", lambda: pygame), "mixer"), "Sound"), "Gunshot.wav")
    _l_(571883)
    _c_(571886, _a_(571885, _n_(571884, "son2", lambda: son2), "play"))
    _l_(571887)
def gachette():
    _l_(571916)

    global son1, son2
    _l_(571889)
    r=_c_(571892, _a_(571891, _n_(571890, "random", lambda: random), "randint"), 1,6)
    _l_(571893)
    if _n_(571894, "r", lambda: r)==1:
        _l_(571915)

        _c_(571897, _a_(571896, _n_(571895, "label1", lambda: label1), "configure"), text="BAM! T'as tiré hahahaha, t'es ded!",font=("Comic Sans Ms",18),foreground="red")
        _l_(571898)
        _c_(571901, _a_(571900, _n_(571899, "son2", lambda: son2), "play"))
        _l_(571902)
        _c_(571905, _a_(571904, _n_(571903, "bouton01", lambda: bouton01), "destroy"))
        _l_(571906)
    else:
        _c_(571909, _a_(571908, _n_(571907, "label1", lambda: label1), "configure"), text="Clic! T'as survécu, tu continues hahaha" )
        _l_(571910)
        _c_(571913, _a_(571912, _n_(571911, "son1", lambda: son1), "play"))
        _l_(571914)

fenetre=_c_(571919, _a_(571918, _n_(571917, "tkinter", lambda: tkinter), "Tk"))
_l_(571920)
_c_(571923, _a_(571922, _n_(571921, "fenetre", lambda: fenetre), "title"), "La roulette russe")
_l_(571924)
_c_(571927, _a_(571926, _n_(571925, "fenetre", lambda: fenetre), "geometry"), "600x600")
_l_(571928)
_c_(571931, _a_(571930, _n_(571929, "fenetre", lambda: fenetre), "configure"), background="black")
_l_(571932)
espace_dessin=_c_(571936, _a_(571934, _n_(571933, "tkinter", lambda: tkinter), "Canvas"), _n_(571935, "fenetre", lambda: fenetre),background="black", height=600, width=600)
_l_(571937)
_c_(571940, _a_(571939, _n_(571938, "espace_dessin", lambda: espace_dessin), "pack"))
_l_(571941)
label0=_c_(571945, _a_(571943, _n_(571942, "tkinter", lambda: tkinter), "Label"), _n_(571944, "fenetre", lambda: fenetre),text="JEU DE LA ROULETTE RUSSE",font=("Arial",20),foreground="black")
_l_(571946)
_c_(571949, _a_(571948, _n_(571947, "label0", lambda: label0), "configure"), background="white")
_l_(571950)
_c_(571953, _a_(571952, _n_(571951, "label0", lambda: label0), "pack"))
_l_(571954)
_c_(571957, _a_(571956, _n_(571955, "label0", lambda: label0), "place"), x=115,y=20)
_l_(571958)

label1=_c_(571962, _a_(571960, _n_(571959, "tkinter", lambda: tkinter), "Label"), _n_(571961, "fenetre", lambda: fenetre), text="T'es toujours vivant, félicitations...!", font=("Comic Sans Ms",18),foreground="green")
_l_(571963)
_c_(571966, _a_(571965, _n_(571964, "label1", lambda: label1), "configure"), background="black")
_l_(571967)
_c_(571970, _a_(571969, _n_(571968, "label1", lambda: label1), "pack"))
_l_(571971)
_c_(571974, _a_(571973, _n_(571972, "label1", lambda: label1), "place"), x=110,y=200)
_l_(571975)

label2=_c_(571979, _a_(571977, _n_(571976, "tkinter", lambda: tkinter), "Label"), _n_(571978, "fenetre", lambda: fenetre), text="Tu poses le bout du canon sur ta tempe et ...", font=("Arial",18),foreground="grey")
_l_(571980)
_c_(571983, _a_(571982, _n_(571981, "label2", lambda: label2), "configure"), background="black")
_l_(571984)
_c_(571987, _a_(571986, _n_(571985, "label2", lambda: label2), "pack"))
_l_(571988)
_c_(571991, _a_(571990, _n_(571989, "label2", lambda: label2), "place"), x=70,y=300)
_l_(571992)

bouton01=_c_(571997, _a_(571994, _n_(571993, "tkinter", lambda: tkinter), "Button"), _n_(571995, "fenetre", lambda: fenetre),text="Tirer",command=_n_(571996, "gachette", lambda: gachette),font=("Arial",16),relief="groove")
_l_(571998)
_c_(572001, _a_(572000, _n_(571999, "bouton01", lambda: bouton01), "pack"))
_l_(572002)
_c_(572005, _a_(572004, _n_(572003, "bouton01", lambda: bouton01), "place"), x=260,y=350)
_l_(572006)


_c_(572009, _a_(572008, _n_(572007, "fenetre", lambda: fenetre), "mainloop"))
_l_(572010)