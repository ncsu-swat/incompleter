# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66913415/return-self-tk-callself-w-cget-key-typeerror-can-only-concatenate
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(568055)

except ImportError:
    pass

def calcular():
    _l_(568074)

    mars = (_c_(568058, _a_(568057, _n_(568056, "peso", lambda: peso), "get"))*3.7)/9.8
    _l_(568059)

  
    if "Marte" in _n_(568060, "planeta", lambda: planeta):
        _l_(568073)

        _c_(568071, _a_(568062, _n_(568061, "res", lambda: res), "set"), "Tu peso en el planeta " + _c_(568067, _n_(568063, "str", lambda: str), _c_(568066, _a_(568065, _n_(568064, "planeta", lambda: planeta), "get"))) + " es: " + _c_(568070, _n_(568068, "str", lambda: str), _n_(568069, "mars", lambda: mars)))
        _l_(568072)

ventana = _c_(568076, _n_(568075, "Tk", lambda: Tk))
_l_(568077)
#StringVar , IntVar, DoubleVar
peso = _c_(568079, _n_(568078, "IntVar", lambda: IntVar))
_l_(568080)
planeta = _c_(568082, _n_(568081, "StringVar", lambda: StringVar))
_l_(568083)
res = _c_(568085, _n_(568084, "StringVar", lambda: StringVar))
_l_(568086)
_c_(568089, _a_(568088, _n_(568087, "ventana", lambda: ventana), "geometry"), "400x300")
_l_(568090)




#Etiqueta
textoN = _c_(568093, _n_(568091, "Label", lambda: Label), _n_(568092, "ventana", lambda: ventana),text="Escribe un numero: ")
_l_(568094)
_c_(568097, _a_(568096, _n_(568095, "textoN", lambda: textoN), "place"), x=150,y=10)
_l_(568098)

#Caja de texto
pesoentry = _c_(568102, _n_(568099, "Entry", lambda: Entry), _n_(568100, "ventana", lambda: ventana),textvariable=_n_(568101, "peso", lambda: peso))
_l_(568103)
_c_(568106, _a_(568105, _n_(568104, "pesoentry", lambda: pesoentry), "place"), x=150,y=40)
_l_(568107)

planeta = _c_(568111, _n_(568108, "Entry", lambda: Entry), _n_(568109, "ventana", lambda: ventana),textvariable=_n_(568110, "planeta", lambda: planeta))
_l_(568112)
_c_(568115, _a_(568114, _n_(568113, "planeta", lambda: planeta), "place"), x=150,y=60)
_l_(568116)

#Etiqueta Resultado
textoR = _c_(568120, _n_(568117, "Label", lambda: Label), _n_(568118, "ventana", lambda: ventana),textvariable=_n_(568119, "res", lambda: res))
_l_(568121)
_c_(568124, _a_(568123, _n_(568122, "textoR", lambda: textoR), "place"), x=150,y=140)
_l_(568125)

#Boton
boton = _c_(568129, _n_(568126, "Button", lambda: Button), _n_(568127, "ventana", lambda: ventana),text="Calcular",command=_n_(568128, "calcular", lambda: calcular),bg="#006",fg="white")
_l_(568130)
_c_(568133, _a_(568132, _n_(568131, "boton", lambda: boton), "place"), x=180,y=100)
_l_(568134)
_c_(568137, _a_(568136, _n_(568135, "ventana", lambda: ventana), "mainloop"))
_l_(568138)