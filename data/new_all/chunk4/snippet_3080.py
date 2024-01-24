# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48519145/nameerror-name-root-is-not-defined-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(624580)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(624582)

except ImportError:
    pass
try:
    from tkinter.ttk import *
    _l_(624584)

except ImportError:
    pass
try:
    from tkinter import LabelFrame, Label, Tk
    _l_(624586)

except ImportError:
    pass
try:
    from tkinter.ttk import Notebook
    _l_(624588)

except ImportError:
    pass
try:
    import tkinter.messagebox
    _l_(624590)

except ImportError:
    pass
try:
    import time
    _l_(624592)

except ImportError:
    pass
try:
    import os
    _l_(624594)

except ImportError:
    pass
try:
    import warnings
    _l_(624596)

except ImportError:
    pass
_c_(624599, _a_(624598, _n_(624597, "warnings", lambda: warnings), "filterwarnings"), 'ignore')
_l_(624600)

class GUIDesign():
    _l_(624620)

    def __init__(self,root):
        _l_(624606)

        _c_(624604, _a_(624602, _n_(624601, "self", lambda: self), "initUI"), _n_(624603, "root", lambda: root)) 
        _l_(624605) 

    def initUI(self,root):
        _l_(624610)

        _c_(624608, _n_(624607, "print", lambda: print), "hello")
        _l_(624609)

    LabelFrameFG="purple"
    _l_(624611)
    LabelFrameBG="SNOW"
    _l_(624612)

    note = _c_(624614, _n_(624613, "Notebook", lambda: Notebook), root)
    _l_(624615)
    tab1 = _c_(624616, Frame, note)
    _l_(624617)
    tab6 = _c_(624618, Frame, note)
    _l_(624619)

def main():
    _l_(624640)

    root = _c_(624622, _n_(624621, "Tk", lambda: Tk))
    _l_(624623)
    _c_(624626, _a_(624625, _n_(624624, "root", lambda: root), "resizable"), 0,0)
    _l_(624627)
    _c_(624630, _a_(624629, _n_(624628, "root", lambda: root), "state"), 'zoomed')
    _l_(624631)
    GUI=_c_(624634, _n_(624632, "GUIDesign", lambda: GUIDesign), _n_(624633, "root", lambda: root))
    _l_(624635)
    _c_(624638, _a_(624637, _n_(624636, "root", lambda: root), "mainloop"))
    _l_(624639)

if _n_(624641, "__name__", lambda: __name__) == '__main__':
    _l_(624645)

    _c_(624643, _n_(624642, "main", lambda: main))
    _l_(624644)