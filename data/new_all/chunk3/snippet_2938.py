# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57642965/calling-listbox-in-python-3-got-an-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(526197)

except ImportError:
    pass
try:
    import tkinter as gui
    _l_(526199)

except ImportError:
    pass
try:
    from random import randint
    _l_(526201)

except ImportError:
    pass

#code open the first window

_c_(526203, _n_(526202, "print", lambda: print), "Listbox setup...", end="")
_l_(526204)
ls = _c_(526206, _n_(526205, "Tk", lambda: Tk))
_l_(526207)
lsbox = _c_(526210, _n_(526208, "ListBox", lambda: ListBox), _n_(526209, "ls", lambda: ls), bg="yellow", fg="orange", selectbackground="grey")
_l_(526211)
_c_(526214, _a_(526213, _n_(526212, "lsbox", lambda: lsbox), "pack"))
_l_(526215)
_c_(526217, _n_(526216, "print", lambda: print), "OK!")
_l_(526218)