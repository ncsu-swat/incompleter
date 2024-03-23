# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27946030/tkinter-attributeerror-object-has-no-attribute-tk
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(381631)

except ImportError:
    pass

root=_c_(381634, _a_(381633, _n_(381632, "tk", lambda: tk), "Tk"))
_l_(381635)

class Page(_a_(381637, _n_(381636, "tk", lambda: tk), "Frame")):
    _l_(381646)

    '''Enables switching between pages of a window.'''
    _l_(381638)
    def __init__(self):
        _l_(381645)

        _n_(381639, "self", lambda: self).widgets={}
        _l_(381640)
        _c_(381643, _a_(381642, _n_(381641, "self", lambda: self), "grid"), column=0,row=0)
        _l_(381644)

page=_c_(381648, _n_(381647, "Page", lambda: Page))
_l_(381649)

_c_(381652, _a_(381651, _n_(381650, "tk", lambda: tk), "mainloop"))
_l_(381653)