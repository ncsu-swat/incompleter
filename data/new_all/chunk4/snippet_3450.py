# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74072555/how-can-i-use-value-of-a-combobox-in-another-external-file-to-help-cursor-excute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import ttk
    _l_(635828)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(635830)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(635832)

except ImportError:
    pass
try:
    import sqlite3
    _l_(635834)

except ImportError:
    pass
try:
    from two import *
    _l_(635836)

except ImportError:
    pass

window = _c_(635839, _a_(635838, _n_(635837, "tk", lambda: tk), "Tk"))  
_l_(635840)  
_c_(635843, _a_(635842, _n_(635841, "window", lambda: window), "geometry"), "350x200")
_l_(635844)
style = _c_(635848, _a_(635846, _n_(635845, "ttk", lambda: ttk), "Style"), _n_(635847, "window", lambda: window))
_l_(635849)

combo1=_c_(635853, _a_(635851, _n_(635850, "ttk", lambda: ttk), "Combobox"), _n_(635852, "window", lambda: window), width = 22)
_l_(635854)
_n_(635855, "combo1", lambda: combo1)['value'] =["Item 1", "Item 2", "Item 3"]
_l_(635856)
_c_(635859, _a_(635858, _n_(635857, "combo1", lambda: combo1), "place"), x=10, y=10)
_l_(635860)
_c_(635863, _a_(635862, _n_(635861, "combo1", lambda: combo1), "set"), "Select")
_l_(635864)

btn = _c_(635867, _n_(635865, "Button", lambda: Button), _n_(635866, "window", lambda: window), text="Click")
_l_(635868)
_c_(635871, _a_(635870, _n_(635869, "btn", lambda: btn), "place"), x=10, y=80)
_l_(635872)