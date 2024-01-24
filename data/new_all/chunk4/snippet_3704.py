# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69578986/attributeerror-function-object-has-no-attribute-set-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(581779)

except ImportError:
    pass
w = _c_(581781, _n_(581780, "Tk", lambda: Tk))
_l_(581782)
_c_(581785, _a_(581784, _n_(581783, "w", lambda: w), "geometry"), "250x250")
_l_(581786)
_c_(581789, _a_(581788, _n_(581787, "w", lambda: w), "title"), "OptionMenu Testing")
_l_(581790)
def DoNothing():
    _l_(581792)

    pass
    _l_(581791)
options = ["Option1", "Option2", "Option3"]
_l_(581793)
DropdownMenuVar = _c_(581795, _n_(581794, "StringVar", lambda: StringVar))
_l_(581796)
_c_(581799, _a_(581798, _n_(581797, "DropdownMenuVar", lambda: DropdownMenuVar), "set"), "Option1")
_l_(581800)
DropdownMenu = _c_(581805, _n_(581801, "OptionMenu", lambda: OptionMenu), _n_(581802, "w", lambda: w), _n_(581803, "DoNothing", lambda: DoNothing), *_n_(581804, "options", lambda: options))
_l_(581806)
_c_(581809, _a_(581808, _n_(581807, "DropdownMenu", lambda: DropdownMenu), "place"), x=175, y=200)
_l_(581810)