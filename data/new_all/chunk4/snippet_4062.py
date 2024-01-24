# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63275396/nameerror-name-ntxtbox-is-not-defined-even-though-ntxtbox-is-a-global-variab
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Tkinter import *
    _l_(642775)

except ImportError:
    pass

admin = _c_(642777, _n_(642776, "Tk", lambda: Tk))
_l_(642778)
def button(an):
    _l_(642786)

    _c_(642781, _n_(642779, "print", lambda: print), _n_(642780, "an", lambda: an))
    _l_(642782)
    _c_(642784, _n_(642783, "print", lambda: print), 'het')
    _l_(642785)

b = _c_(642791, _n_(642787, "Button", lambda: Button), _n_(642788, "admin", lambda: admin), text='as', command=_c_(642790, _n_(642789, "button", lambda: button), 'hey'))
_l_(642792)
_c_(642795, _a_(642794, _n_(642793, "b", lambda: b), "pack"))
_l_(642796)
_c_(642798, _n_(642797, "mainloop", lambda: mainloop))
_l_(642799)