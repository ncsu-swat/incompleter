# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57154707/dont-understand-why-im-getting-a-nameerror-in-my-class-definition
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import ttk
    _l_(344909)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(344911)

except ImportError:
    pass
try:
    import sqlite3
    _l_(344913)

except ImportError:
    pass

class Product:
    _l_(344939)

    def __init__(self, window):
        _l_(344922)

        _n_(344914, "self", lambda: self).wind = _n_(344915, "window", lambda: window)
        _l_(344916)
        _c_(344920, _a_(344919, _a_(344918, _n_(344917, "self", lambda: self), "wind"), "title"), "Products inventory")
        _l_(344921)

    frame = _c_(344924, LabelFrame, _a_(344923, self, "wind"), text  = 'Register a new product')
    _l_(344925)
    _c_(344927, _a_(344926, frame, "grid"), row = 0, column = 0, columnspan = 3, pady = 20)
    _l_(344928)

    _c_(344931, _a_(344930, _c_(344929, Label, frame, text = 'Name: '), "grid"), row = 1, column = 0)
    _l_(344932)
    self.name = _c_(344933, Entry, frame)
    _l_(344934)
    _c_(344937, _a_(344936, _a_(344935, self, "name"), "grid"), row = 1, column = 1)
    _l_(344938)

if _n_(344940, "__name__", lambda: __name__) == '__main__':
    _l_(344952)

    window = _c_(344942, _n_(344941, "Tk", lambda: Tk))
    _l_(344943)
    application = _c_(344946, _n_(344944, "Product", lambda: Product), _n_(344945, "window", lambda: window))
    _l_(344947)
    _c_(344950, _a_(344949, _n_(344948, "window", lambda: window), "mainloop"))
    _l_(344951)