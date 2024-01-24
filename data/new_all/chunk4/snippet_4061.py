# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63275396/nameerror-name-ntxtbox-is-not-defined-even-though-ntxtbox-is-a-global-variab
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Tkinter import *
    _l_(585214)

except ImportError:
    pass

admin = _c_(585216, _n_(585215, "Tk", lambda: Tk))
_l_(585217)
def button(an):
    _l_(585225)

    _c_(585220, _n_(585218, "print", lambda: print), _n_(585219, "an", lambda: an))
    _l_(585221)
    _c_(585223, _n_(585222, "print", lambda: print), 'het')
    _l_(585224)

b = _c_(585230, _n_(585226, "Button", lambda: Button), _n_(585227, "admin", lambda: admin), text='as', command=_c_(585229, _n_(585228, "button", lambda: button), 'hey'))
_l_(585231)
_c_(585234, _a_(585233, _n_(585232, "b", lambda: b), "pack"))
_l_(585235)
_c_(585237, _n_(585236, "mainloop", lambda: mainloop))
_l_(585238)