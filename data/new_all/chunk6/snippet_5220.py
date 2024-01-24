# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57154707/dont-understand-why-im-getting-a-nameerror-in-my-class-definition
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import ttk
    _l_(358194)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(358196)

except ImportError:
    pass
try:
    import sqlite3
    _l_(358198)

except ImportError:
    pass

class Product:
    _l_(358224)

    def __init__(self, window):
        _l_(358207)

        _n_(358199, "self", lambda: self).wind = _n_(358200, "window", lambda: window)
        _l_(358201)
        _c_(358205, _a_(358204, _a_(358203, _n_(358202, "self", lambda: self), "wind"), "title"), "Products inventory")
        _l_(358206)

    frame = _c_(358209, LabelFrame, _a_(358208, self, "wind"), text  = 'Register a new product')
    _l_(358210)
    _c_(358212, _a_(358211, frame, "grid"), row = 0, column = 0, columnspan = 3, pady = 20)
    _l_(358213)

    _c_(358216, _a_(358215, _c_(358214, Label, frame, text = 'Name: '), "grid"), row = 1, column = 0)
    _l_(358217)
    self.name = _c_(358218, Entry, frame)
    _l_(358219)
    _c_(358222, _a_(358221, _a_(358220, self, "name"), "grid"), row = 1, column = 1)
    _l_(358223)

if _n_(358225, "__name__", lambda: __name__) == '__main__':
    _l_(358237)

    window = _c_(358227, _n_(358226, "Tk", lambda: Tk))
    _l_(358228)
    application = _c_(358231, _n_(358229, "Product", lambda: Product), _n_(358230, "window", lambda: window))
    _l_(358232)
    _c_(358235, _a_(358234, _n_(358233, "window", lambda: window), "mainloop"))
    _l_(358236)