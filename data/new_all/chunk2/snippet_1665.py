# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65484647/why-have-i-a-nameerror-when-i-transform-a-local-variable-in-global-variable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(435877)

except ImportError:
    pass
try:
    from tkinter import colorchooser
    _l_(435879)

except ImportError:
    pass

window = _c_(435881, _n_(435880, "Tk", lambda: Tk))
_l_(435882)
_c_(435885, _a_(435884, _n_(435883, "window", lambda: window), "geometry"), "500x500")
_l_(435886)

def chooseColor() :
    _l_(435900)

    global colorCode
    _l_(435887)
    global colorName
    _l_(435888)

    colorCode = _c_(435891, _a_(435890, _n_(435889, "colorchooser", lambda: colorchooser), "askcolor"), title="Choose color")
    _l_(435892)
    colorName = _n_(435893, "colorCode", lambda: colorCode)[1]
    _l_(435894)
    _c_(435898, _a_(435896, _n_(435895, "window", lambda: window), "configure"), bg=_n_(435897, "colorName", lambda: colorName))
    _l_(435899)

title = _c_(435904, _n_(435901, "Label", lambda: Label), _n_(435902, "window", lambda: window), text="Voyons ce que réserve Tkinter", font="none 25", fg=_n_(435903, "colorName", lambda: colorName))
_l_(435905)
_c_(435908, _a_(435907, _n_(435906, "title", lambda: title), "pack"))
_l_(435909)

but = _c_(435913, _n_(435910, "Button", lambda: Button), _n_(435911, "window", lambda: window), text="Please click :D", command=_n_(435912, "chooseColor", lambda: chooseColor))
_l_(435914)
_c_(435917, _a_(435916, _n_(435915, "but", lambda: but), "pack"))
_l_(435918)

_c_(435921, _a_(435920, _n_(435919, "window", lambda: window), "mainloop"))
_l_(435922)