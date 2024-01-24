# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52182578/typeerror-str-object-is-not-callable-in-messgaebox-of-tkinter-in-python
#other codes

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(345746)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(345748)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(345750)

except ImportError:
    pass

#othercodes

root = _c_(345752, _n_(345751, "Tk", lambda: Tk))
_l_(345753)
frame = _c_(345756, _n_(345754, "Frame", lambda: Frame), _n_(345755, "root", lambda: root))
_l_(345757)

#other codes

def net_connection_error():
    _l_(345762)

    #print(dir(messagebox))
    _c_(345760, _a_(345759, _n_(345758, "messagebox", lambda: messagebox), "INFO"), "info",
        "No Connection!"
    )
    _l_(345761)

#other codes

_c_(345764, _n_(345763, "net_connection_error", lambda: net_connection_error))
_l_(345765)

#other codes

_c_(345768, _a_(345767, _n_(345766, "root", lambda: root), "mainloop"))
_l_(345769)