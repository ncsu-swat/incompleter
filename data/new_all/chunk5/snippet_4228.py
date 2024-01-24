# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61191223/attributeerror-tkinter-tkapp-object-has-no-attribute-name-while-usi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter
    _l_(658462)

except ImportError:
    pass
try:
    import os
    _l_(658464)

except ImportError:
    pass
try:
    import time
    _l_(658466)

except ImportError:
    pass
#control rod percentages
cr1 = 100
_l_(658467)

p = '%'
_l_(658468)

#grid pieces
c1 = 'CTRL ROD 01 '
_l_(658469)
ins = ' INSERTED'
_l_(658470)

grid1 = ' _________________________ '
_l_(658471)
grid2 = '|'
_l_(658472)
grid3 = '|_________________________|'
_l_(658473)
def panel():
    _l_(658491)

    _c_(658476, _n_(658474, "print", lambda: print), _n_(658475, "grid1", lambda: grid1))
    _l_(658477)
    _c_(658480, _n_(658478, "print", lambda: print), _n_(658479, "grid3", lambda: grid3))
    _l_(658481)
    _c_(658485, _a_(658483, _n_(658482, "win", lambda: win), "after_idle"), _n_(658484, "panel", lambda: panel))
    _l_(658486)
    _c_(658489, _a_(658488, _n_(658487, "os", lambda: os), "system"), 'cls')
    _l_(658490)

win = _c_(658494, _a_(658493, _n_(658492, "tkinter", lambda: tkinter), "Tk"), className=' N.M.S. ')
_l_(658495)
w = _c_(658500, _a_(658497, _n_(658496, "tkinter", lambda: tkinter), "Button"), _n_(658498, "win", lambda: win), activeforeground="black", activebackground="red", bg="grey", fg="black", command=_n_(658499, "panel", lambda: panel), text="START", height=1, width=10)
_l_(658501)
_c_(658504, _a_(658503, _n_(658502, "w", lambda: w), "pack"))
_l_(658505)
_c_(658508, _a_(658507, _n_(658506, "win", lambda: win), "mainloop"))
_l_(658509)