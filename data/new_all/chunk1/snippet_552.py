# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56791883/typeerror-can-only-concatenate-str-not-set-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import visa
    _l_(397055)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(397057)

except ImportError:
    pass


rm = _c_(397060, _a_(397059, _n_(397058, "visa", lambda: visa), "ResourceManager"))
_l_(397061)
_c_(397066, _n_(397062, "print", lambda: print), _c_(397065, _a_(397064, _n_(397063, "rm", lambda: rm), "list_resources")))
_l_(397067)
inst = _c_(397070, _a_(397069, _n_(397068, "rm", lambda: rm), "open_resource"), 'TCPIP::192.168.100.200::INSTR')
_l_(397071)

#This one would work, after i bind the function to the button,
#i just press it and it passes the preset value. 
#All i want to do is pass a value through the Entry widget, 
#instead of having a set one.
#freq = str(250000) 
#def freqset_smb100a():
    #inst.write("SOUR:FREQ:CW " + freq)

_c_(397074, _a_(397073, _n_(397072, "inst", lambda: inst), "write"), "OUTP ON")
_l_(397075)

def freqset_smb100a():
    _l_(397085)

    _c_(397083, _a_(397077, _n_(397076, "inst", lambda: inst), "write"), f"SOUR:FREQ:CW " + {_c_(397082, _n_(397078, "str", lambda: str), _c_(397081, _a_(397080, _n_(397079, "input_var", lambda: input_var), "get")))})
    _l_(397084)



HEIGHT = 400
_l_(397086)
WIDTH = 600
_l_(397087)

root = _c_(397090, _a_(397089, _n_(397088, "tk", lambda: tk), "Tk"))
_l_(397091)

input_var = _c_(397094, _a_(397093, _n_(397092, "tk", lambda: tk), "StringVar"))
_l_(397095)

canvas = _c_(397101, _a_(397097, _n_(397096, "tk", lambda: tk), "Canvas"), _n_(397098, "root", lambda: root), height=_n_(397099, "HEIGHT", lambda: HEIGHT), width=_n_(397100, "WIDTH", lambda: WIDTH))
_l_(397102)
_c_(397105, _a_(397104, _n_(397103, "canvas", lambda: canvas), "pack"))
_l_(397106)

frame = _c_(397110, _a_(397108, _n_(397107, "tk", lambda: tk), "Frame"), _n_(397109, "root", lambda: root), bg='#80c1ff', bd=5)
_l_(397111)
_c_(397114, _a_(397113, _n_(397112, "frame", lambda: frame), "place"), relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
_l_(397115)

button = _c_(397120, _a_(397117, _n_(397116, "tk", lambda: tk), "Button"), _n_(397118, "frame", lambda: frame), text="Set Freq", font=40, command=_n_(397119, "freqset_smb100a", lambda: freqset_smb100a))
_l_(397121)
_c_(397124, _a_(397123, _n_(397122, "button", lambda: button), "place"), relx=0.7, relheight=1, relwidth=0.3)
_l_(397125)

entry = _c_(397133, _a_(397127, _n_(397126, "tk", lambda: tk), "Entry"), _n_(397128, "frame", lambda: frame), font=15, textvariable=_c_(397132, _n_(397129, "str", lambda: str), _a_(397131, _n_(397130, "input_var", lambda: input_var), "get")))
_l_(397134)
_c_(397137, _a_(397136, _n_(397135, "entry", lambda: entry), "place"), relx=0.35, relheight=1, relwidth=0.3)
_l_(397138)


_c_(397141, _a_(397140, _n_(397139, "root", lambda: root), "mainloop"))
_l_(397142)