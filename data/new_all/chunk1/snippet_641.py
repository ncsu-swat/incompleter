# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77208733/import-widgets-into-a-function-from-a-class-in-another-file-nameerror-name-te
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(400424)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(400426)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(400428)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(400430)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(400432)

except ImportError:
    pass
try:
    import tkinter.font as tkFont
    _l_(400434)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(400436)

except ImportError:
    pass

class Page1(_a_(400438, _n_(400437, "tk", lambda: tk), "Frame")):
    _l_(400468)

    def __init__(self, master, **kw):
        _l_(400467)

        _c_(400443, _a_(400440, _n_(400439, "super", lambda: super)(), "__init__"), _n_(400441, "master", lambda: master), **_n_(400442, "kw", lambda: kw))
        _l_(400444)

        _n_(400445, "self", lambda: self).textbox1 = _c_(400449, _a_(400447, _n_(400446, "ttk", lambda: ttk), "Entry"), _n_(400448, "self", lambda: self), width=7)
        _l_(400450)
        _c_(400454, _a_(400453, _a_(400452, _n_(400451, "self", lambda: self), "textbox1"), "place"), x=10, y=10)
        _l_(400455)

        _n_(400456, "self", lambda: self).textbox2 = _c_(400460, _a_(400458, _n_(400457, "ttk", lambda: ttk), "Entry"), _n_(400459, "self", lambda: self), width=7)
        _l_(400461)
        _c_(400465, _a_(400464, _a_(400463, _n_(400462, "self", lambda: self), "textbox2"), "place"), x=10, y=40)
        _l_(400466)