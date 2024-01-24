# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71583588/typeerror-menus-init-takes-1-positional-argument-but-2-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(663071)

except ImportError:
    pass
try:
    from meanu_items import *
    _l_(663073)

except ImportError:
    pass


def main():
    _l_(663132)

    windows = _c_(663075, _n_(663074, "Tk", lambda: Tk))
    _l_(663076)
    _c_(663079, _a_(663078, _n_(663077, "windows", lambda: windows), "title"), "NotePad")
    _l_(663080)
    _c_(663083, _a_(663082, _n_(663081, "windows", lambda: windows), "minsize"), width=60, height=80)
    _l_(663084)
    _c_(663087, _a_(663086, _n_(663085, "windows", lambda: windows), "config"))
    _l_(663088)
    # Create place to write a text
    text = _c_(663091, _n_(663089, "Text", lambda: Text), _n_(663090, "windows", lambda: windows))
    _l_(663092)
    _c_(663095, _a_(663094, _n_(663093, "text", lambda: text), "focus"))
    _l_(663096)
    _c_(663099, _a_(663098, _n_(663097, "text", lambda: text), "grid"), pady=0.5, padx=10)
    _l_(663100)

    # Creating Scale
    scroll = _c_(663104, _n_(663101, "Scrollbar", lambda: Scrollbar), _n_(663102, "windows", lambda: windows), orient=_n_(663103, "VERTICAL", lambda: VERTICAL), )
    _l_(663105)
    _c_(663110, _a_(663107, _n_(663106, "scroll", lambda: scroll), "grid"), row=0, column=1, sticky=_n_(663108, "NS", lambda: NS) + _n_(663109, "SE", lambda: SE))
    _l_(663111)
    _c_(663116, _a_(663113, _n_(663112, "text", lambda: text), "config"), yscrollcommand=_a_(663115, _n_(663114, "scroll", lambda: scroll), "set"))
    _l_(663117)
    _c_(663122, _a_(663119, _n_(663118, "scroll", lambda: scroll), "config"), command=_a_(663121, _n_(663120, "text", lambda: text), "yview"))
    _l_(663123)

    menu = _c_(663126, _n_(663124, "Menus", lambda: Menus), _n_(663125, "windows", lambda: windows))
    _l_(663127)

    _c_(663130, _a_(663129, _n_(663128, "windows", lambda: windows), "mainloop"))
    _l_(663131)


if _n_(663133, "__name__", lambda: __name__) == '__main__':
    _l_(663137)

    _c_(663135, _n_(663134, "main", lambda: main))
    _l_(663136)