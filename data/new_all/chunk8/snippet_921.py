# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35787215/nameerror-name-menu-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import Tk, BOTH
    _l_(388921)

except ImportError:
    pass
try:
    from tkinter.ttk import Frame, Button, Style
    _l_(388923)

except ImportError:
    pass


class Example(_n_(388924, "Frame", lambda: Frame)):
    _l_(388996)


    def __init__(self, parent):
        _l_(388952)

        _c_(388929, _a_(388926, _n_(388925, "Frame", lambda: Frame), "__init__"), _n_(388927, "self", lambda: self), _n_(388928, "parent", lambda: parent))
        _l_(388930)

        _n_(388931, "self", lambda: self).parent = _n_(388932, "parent", lambda: parent)
        _l_(388933)
        _c_(388937, _a_(388936, _a_(388935, _n_(388934, "self", lambda: self), "parent"), "title"), "xcal file.ics")
        _l_(388938)
        _c_(388942, _a_(388940, _n_(388939, "self", lambda: self), "pack"), fill=_n_(388941, "BOTH", lambda: BOTH), expand=1)
        _l_(388943)
        _c_(388946, _a_(388945, _n_(388944, "self", lambda: self), "centerWindow"))
        _l_(388947)
        _c_(388950, _a_(388949, _n_(388948, "self", lambda: self), "createMenuBar"))
        _l_(388951)


    def centerWindow(self):
        _l_(388980)


        w = 500
        _l_(388953)
        h = 500
        _l_(388954)

        sw = _c_(388958, _a_(388957, _a_(388956, _n_(388955, "self", lambda: self), "parent"), "winfo_screenwidth"))
        _l_(388959)
        sh = _c_(388963, _a_(388962, _a_(388961, _n_(388960, "self", lambda: self), "parent"), "winfo_screenheight"))
        _l_(388964)

        x = (_n_(388965, "sw", lambda: sw) - _n_(388966, "w", lambda: w))/2
        _l_(388967)
        y = (_n_(388968, "sh", lambda: sh) - _n_(388969, "h", lambda: h))/2
        _l_(388970)
        _c_(388978, _a_(388973, _a_(388972, _n_(388971, "self", lambda: self), "parent"), "geometry"), '%dx%d+%d+%d' % (_n_(388974, "w", lambda: w), _n_(388975, "h", lambda: h), _n_(388976, "x", lambda: x), _n_(388977, "y", lambda: y)))
        _l_(388979)

    def createMenuBar(self):
        _l_(388995)

        menubar = _c_(388983, _n_(388981, "Menu", lambda: Menu), _n_(388982, "Frame", lambda: Frame)) #ERROR
        _l_(388984) #ERROR
        _c_(388988, _a_(388986, _n_(388985, "menubar", lambda: menubar), "add_command"), label="Hello!", command=_n_(388987, "hello", lambda: hello))
        _l_(388989)
        _c_(388993, _a_(388991, _n_(388990, "Frame", lambda: Frame), "config"), menu=_n_(388992, "menubar", lambda: menubar))
        _l_(388994)

def main():
    _l_(389008)


    root = _c_(388998, _n_(388997, "Tk", lambda: Tk))
    _l_(388999)
    ex = _c_(389002, _n_(389000, "Example", lambda: Example), _n_(389001, "root", lambda: root))
    _l_(389003)
    _c_(389006, _a_(389005, _n_(389004, "root", lambda: root), "mainloop"))
    _l_(389007)


if _n_(389009, "__name__", lambda: __name__) == '__main__':
    _l_(389013)

    _c_(389011, _n_(389010, "main", lambda: main))
    _l_(389012)