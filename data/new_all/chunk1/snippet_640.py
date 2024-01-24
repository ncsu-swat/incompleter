# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77208733/import-widgets-into-a-function-from-a-class-in-another-file-nameerror-name-te
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(404118)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(404120)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(404122)

except ImportError:
    pass
try:
    from page1 import Page1
    _l_(404124)

except ImportError:
    pass

root = _c_(404127, _a_(404126, _n_(404125, "tk", lambda: tk), "Tk"))
_l_(404128)
_c_(404131, _a_(404130, _n_(404129, "root", lambda: root), "geometry"), '480x320')
_l_(404132)

style = _c_(404135, _a_(404134, _n_(404133, "ttk", lambda: ttk), "Style"))
_l_(404136)
_c_(404139, _a_(404138, _n_(404137, "style", lambda: style), "theme_use"), 'default') 
_l_(404140) 
_c_(404143, _a_(404142, _n_(404141, "style", lambda: style), "configure"), 'TNotebook', tabposition='wn', background='white', tabmargins=0)
_l_(404144)
_c_(404147, _a_(404146, _n_(404145, "style", lambda: style), "configure"), 'TNotebook.Tab', background='white', width=10, focuscolor='yellow', borderwidth=0)
_l_(404148)
_c_(404151, _a_(404150, _n_(404149, "style", lambda: style), "map"), 'TNotebook.Tab', background=[('selected', 'yellow')])
_l_(404152)

nb = _c_(404156, _a_(404154, _n_(404153, "ttk", lambda: ttk), "Notebook"), _n_(404155, "root", lambda: root))
_l_(404157)
_c_(404160, _a_(404159, _n_(404158, "nb", lambda: nb), "place"), x=0, y=70)
_l_(404161)
page1 = _c_(404164, _n_(404162, "Page1", lambda: Page1), _n_(404163, "nb", lambda: nb), width=492, height=905)
_l_(404165)
_c_(404169, _a_(404167, _n_(404166, "nb", lambda: nb), "add"), _n_(404168, "page1", lambda: page1), text='Tab 1', compound='left')
_l_(404170)

def function1(textbox1, textbox2):
    _l_(404183)


    val_1 = "example 1"
    _l_(404171)
    _c_(404175, _a_(404173, _n_(404172, "textbox1", lambda: textbox1), "insert"), 0, _n_(404174, "val_1", lambda: val_1))
    _l_(404176)

    val_2 = "example 1"
    _l_(404177)
    _c_(404181, _a_(404179, _n_(404178, "textbox2", lambda: textbox2), "insert"), 0, _n_(404180, "val_2", lambda: val_2))
    _l_(404182)

button1 = _c_(404190, _n_(404184, "Button", lambda: Button), _n_(404185, "root", lambda: root), text="Button", command= _c_(404189, _n_(404186, "function1", lambda: function1), _n_(404187, "textbox1", lambda: textbox1), _n_(404188, "textbox2", lambda: textbox2)))
_l_(404191)
_c_(404194, _a_(404193, _n_(404192, "button1", lambda: button1), "place"), x=0, y=0)
_l_(404195)

_c_(404198, _a_(404197, _n_(404196, "root", lambda: root), "mainloop"))
_l_(404199)