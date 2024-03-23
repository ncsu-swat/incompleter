# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50948727/typeerror-button-click-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(418400)

except ImportError:
    pass
try:
    import tkinter
    _l_(418402)

except ImportError:
    pass
try:
    from client import*
    _l_(418404)

except ImportError:
    pass

root = _c_(418407, _a_(418406, _n_(418405, "tkinter", lambda: tkinter), "Tk"))
_l_(418408)
class view():
    _l_(418446)

    _c_(418411, _a_(418410, _n_(418409, "root", lambda: root), "geometry"), "250x300")
    _l_(418412)
    F1 =_c_(418413, Frame)
    _l_(418414)
    L = _c_(418415, Listbox, F1)
    _l_(418416)
    _c_(418418, _a_(418417, L, "grid"), row=0, column =0) 
    _l_(418419) 

    _c_(418421, _a_(418420, L, "pack"))
    _l_(418422)

    F = _c_(418424, _n_(418423, "open", lambda: open), "users.txt","r")
    _l_(418425)
    M = _c_(418427, _a_(418426, F, "read"))
    _l_(418428)
    cont = _c_(418430, _a_(418429, M, "split"))
    _l_(418431)

    for each in cont:
        _l_(418439)

        ind = _c_(418433, _a_(418432, each, "find"), "#") + 1
        _l_(418434)
        _c_(418436, _a_(418435, L, "insert"), ind+1 ,each[ind:])
        _l_(418437)
        break
        _l_(418438)

    _c_(418441, _a_(418440, F, "close"))
    _l_(418442)

    _c_(418444, _a_(418443, F1, "pack"))
    _l_(418445)
def button_click(self):
    _l_(418457)

    _c_(418450, _a_(418449, _a_(418448, _n_(418447, "self", lambda: self), "form"), "destroy"))
    _l_(418451)
    _c_(418455, _a_(418454, _c_(418453, _n_(418452, "Chatclient", lambda: Chatclient)), "design"))
    _l_(418456)

button = _c_(418461, _n_(418458, "Button", lambda: Button), _n_(418459, "root", lambda: root), text="Create Group Chat", command= _n_(418460, "button_click", lambda: button_click))
_l_(418462)

_c_(418465, _a_(418464, _n_(418463, "button", lambda: button), "pack"))
_l_(418466)
_c_(418469, _a_(418468, _n_(418467, "root", lambda: root), "mainloop"))
_l_(418470)