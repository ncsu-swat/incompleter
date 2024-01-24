# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74967046/how-can-i-import-a-function-into-class-of-an-external-file-nameerror-name-cli
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(617990)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(617992)

except ImportError:
    pass

class Page1(_a_(617994, _n_(617993, "tk", lambda: tk), "Frame")):
    _l_(618026)

    def __init__(self, master, **kw):
        _l_(618025)

        _c_(617999, _a_(617996, _n_(617995, "super", lambda: super)(), "__init__"), _n_(617997, "master", lambda: master), **_n_(617998, "kw", lambda: kw))
        _l_(618000)

        Checkbutton1 = _c_(618003, _a_(618002, _n_(618001, "tk", lambda: tk), "IntVar"))
        _l_(618004)

        def Button1_func():
            _l_(618008)

            x = "test"
            _l_(618005)
            aux = _n_(618006, "x", lambda: x)
            _l_(618007)
            return aux
  
        Button1 = _c_(618019, _a_(618010, _n_(618009, "tk", lambda: tk), "Checkbutton"), _n_(618011, "self", lambda: self), text = "Checkbox1", variable = _n_(618012, "Checkbutton1", lambda: Checkbutton1), onvalue = 1, offvalue = 0, height = 1,
                                 bg="white", foreground='black', activebackground="white", highlightthickness = 0,
                                 command=lambda: _c_(618018, _n_(618013, "clicked", lambda: clicked), _c_(618016, _a_(618015, _n_(618014, "Checkbutton1", lambda: Checkbutton1), "get")), _n_(618017, "Button1_func", lambda: Button1_func)))
        _l_(618020)
        _c_(618023, _a_(618022, _n_(618021, "Button1", lambda: Button1), "place"), x=10, y=30)
        _l_(618024)