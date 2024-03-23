# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70628464/importerror-or-attributeerror-while-using-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(581640)

except ImportError:
    pass
try:
    import test2
    _l_(581642)

except ImportError:
    pass


root = _c_(581644, _n_(581643, "Tk", lambda: Tk))
_l_(581645)
_c_(581648, _a_(581647, _n_(581646, "root", lambda: root), "title"), 'Scott Window')
_l_(581649)
_c_(581652, _a_(581651, _n_(581650, "root", lambda: root), "geometry"), '500x350')
_l_(581653)

greet = _c_(581656, _a_(581655, _n_(581654, "test2", lambda: test2), "nameit"), 'John')
_l_(581657)

mylabel = _c_(581661, _n_(581658, "Label", lambda: Label), _n_(581659, "root", lambda: root), text=_n_(581660, "greet", lambda: greet))
_l_(581662)
_c_(581665, _a_(581664, _n_(581663, "mylabel", lambda: mylabel), "pack"), pady=20)
_l_(581666)


_c_(581669, _a_(581668, _n_(581667, "root", lambda: root), "mainloop"))
_l_(581670)