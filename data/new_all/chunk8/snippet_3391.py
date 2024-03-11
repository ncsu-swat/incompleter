# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74967046/how-can-i-import-a-function-into-class-of-an-external-file-nameerror-name-cli
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(608975)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(608977)

except ImportError:
    pass
try:
    from page1 import *
    _l_(608979)

except ImportError:
    pass

root = _c_(608982, _a_(608981, _n_(608980, "tk", lambda: tk), "Tk"))
_l_(608983)
_c_(608986, _a_(608985, _n_(608984, "root", lambda: root), "geometry"), '480x320')
_l_(608987)

style = _c_(608990, _a_(608989, _n_(608988, "ttk", lambda: ttk), "Style"))
_l_(608991)
_c_(608994, _a_(608993, _n_(608992, "style", lambda: style), "theme_use"), 'default')
_l_(608995)
_c_(608998, _a_(608997, _n_(608996, "style", lambda: style), "configure"), 'TNotebook', tabposition='ws', background='white', tabmargins=0)
_l_(608999)

nb = _c_(609003, _a_(609001, _n_(609000, "ttk", lambda: ttk), "Notebook"), _n_(609002, "root", lambda: root))
_l_(609004)
_c_(609007, _a_(609006, _n_(609005, "nb", lambda: nb), "pack"), fill='both', expand=1)
_l_(609008)
page1 = _c_(609011, _n_(609009, "Page1", lambda: Page1), _n_(609010, "nb", lambda: nb))
_l_(609012)
_c_(609016, _a_(609014, _n_(609013, "nb", lambda: nb), "add"), _n_(609015, "page1", lambda: page1), text='Page 1', compound='left')
_l_(609017)

datalist = []
_l_(609018)
        
def clicked(flag, func):
    _l_(609033)

    if _n_(609019, "flag", lambda: flag):
        _l_(609032)

        _c_(609024, _a_(609021, _n_(609020, "datalist", lambda: datalist), "append"), _c_(609023, _n_(609022, "func", lambda: func)))
        _l_(609025)
    else:
        _c_(609030, _a_(609027, _n_(609026, "datalist", lambda: datalist), "remove"), _c_(609029, _n_(609028, "func", lambda: func)))
        _l_(609031)

def try_print():
    _l_(609041)

    if _c_(609036, _n_(609034, "len", lambda: len), _n_(609035, "datalist", lambda: datalist)) > 0:
        _l_(609040)

        _c_(609038, _n_(609037, "print", lambda: print), "ok")
        _l_(609039)

button = _c_(609047, _a_(609043, _n_(609042, "tk", lambda: tk), "Button"), _n_(609044, "root", lambda: root), text="Print", command= _c_(609046, _n_(609045, "try_print", lambda: try_print)))
_l_(609048)
_c_(609051, _a_(609050, _n_(609049, "button", lambda: button), "place"), x=60, y=100)
_l_(609052)

_c_(609055, _a_(609054, _n_(609053, "root", lambda: root), "mainloop"))
_l_(609056)