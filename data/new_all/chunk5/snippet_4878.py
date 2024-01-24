# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43744736/python3-class-function-definition-confusion-about-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(655861)

except ImportError:
    pass

WINDOW_HEIGHT = 300
_l_(655862)
WINDOW_WIDTH = 325
_l_(655863)

class Window(_n_(655864, "Frame", lambda: Frame)):
    _l_(655909)


    def __init__(self, master = None):
        _l_(655878)

        _c_(655869, _a_(655866, _n_(655865, "Frame", lambda: Frame), "__init__"), _n_(655867, "self", lambda: self), _n_(655868, "master", lambda: master))
        _l_(655870)
        _n_(655871, "self", lambda: self).master = _n_(655872, "master", lambda: master)
        _l_(655873)
        _c_(655876, _a_(655875, _n_(655874, "self", lambda: self), "init_window"))
        _l_(655877)

    def num_but_gen(self, disp, xloc=0, yloc=0, wid=0, hei=0):
        _l_(655894)

        _c_(655886, _a_(655880, _n_(655879, "self", lambda: self), "Button"), text=_c_(655883, _a_(655881, '{}', "format"), _n_(655882, "disp", lambda: disp)),height=_n_(655884, "hei", lambda: hei), width=_n_(655885, "wid", lambda: wid))
        _l_(655887)
        _c_(655892, _a_(655889, _n_(655888, "self", lambda: self), "place"), x=_n_(655890, "xloc", lambda: xloc), y=_n_(655891, "yloc", lambda: yloc))
        _l_(655893)

    def init_window(self):
        _l_(655908)

        _c_(655898, _a_(655897, _a_(655896, _n_(655895, "self", lambda: self), "master"), "title"), 'Calculator')
        _l_(655899)
        _c_(655903, _a_(655901, _n_(655900, "self", lambda: self), "pack"), fill=_n_(655902, "BOTH", lambda: BOTH), expand=1)
        _l_(655904)
        Button1 = _c_(655906, _n_(655905, "num_but_gen", lambda: num_but_gen), '1', xloc=0, yloc=200, wid=40, hei=40)
        _l_(655907)


root = _c_(655911, _n_(655910, "Tk", lambda: Tk))
_l_(655912)
app = _c_(655915, _n_(655913, "Window", lambda: Window), _n_(655914, "root", lambda: root))
_l_(655916)
_c_(655923, _a_(655918, _n_(655917, "root", lambda: root), "geometry"), _c_(655922, _a_(655919, "{}x{}", "format"), _n_(655920, "WINDOW_WIDTH", lambda: WINDOW_WIDTH),_n_(655921, "WINDOW_HEIGHT", lambda: WINDOW_HEIGHT)))
_l_(655924)
_c_(655927, _a_(655926, _n_(655925, "root", lambda: root), "mainloop"))
_l_(655928)