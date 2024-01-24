# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68951032/python-typeerror-label-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image, ImageTk
    _l_(341916)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(341918)

except ImportError:
    pass
try:
    from tkinter import Label
    _l_(341920)

except ImportError:
    pass

def open_window():
    _l_(341950)

    menu = _c_(341923, _n_(341921, "Toplevel", lambda: Toplevel), _n_(341922, "root", lambda: root))
    _l_(341924)
    _c_(341927, _a_(341926, _n_(341925, "menu", lambda: menu), "geometry"), "800x800")
    _l_(341928)
    _c_(341931, _a_(341930, _n_(341929, "menu", lambda: menu), "title"), "my game's menu")
    _l_(341932)
    _c_(341935, _a_(341934, _n_(341933, "menu", lambda: menu), "resizable"), False, False)
    _l_(341936)
    _c_(341939, _a_(341938, _n_(341937, "menu", lambda: menu), "geometry"), "800x800")
    _l_(341940)
    lbl = _a_(341944, _c_(341943, _n_(341941, "Label", lambda: Label), _n_(341942, "menu", lambda: menu), text ="Hello!"), "pack")
    _l_(341945)

    _c_(341948, _a_(341947, _n_(341946, "menu", lambda: menu), "mainloop"))
    _l_(341949)


root = _c_(341952, _n_(341951, "Tk", lambda: Tk))
_l_(341953)
_c_(341956, _a_(341955, _n_(341954, "root", lambda: root), "geometry"), "400x300")
_l_(341957)
Label = _c_(341960, _n_(341958, "Label", lambda: Label), _n_(341959, "root", lambda: root), text="Are you ready?")
_l_(341961)
_c_(341964, _a_(341963, _n_(341962, "Label", lambda: Label), "pack"))
_l_(341965)


_c_(341968, _a_(341967, _n_(341966, "root", lambda: root), "title"), "quick question")
_l_(341969)


btn = _c_(341973, _n_(341970, "Button", lambda: Button), _n_(341971, "root", lambda: root), text="Yes", command= _n_(341972, "open_window", lambda: open_window))
_l_(341974)
_c_(341977, _a_(341976, _n_(341975, "btn", lambda: btn), "pack"), padx=20, pady = 20)
_l_(341978)
_c_(341981, _a_(341980, _n_(341979, "root", lambda: root), "mainloop"))
_l_(341982)