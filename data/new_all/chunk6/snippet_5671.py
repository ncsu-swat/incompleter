# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52182578/typeerror-str-object-is-not-callable-in-messgaebox-of-tkinter-in-python
#other codes

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(339934)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(339936)

except ImportError:
    pass
try:
    from tkinter import messagebox
    _l_(339938)

except ImportError:
    pass

#othercodes

root = _c_(339940, _n_(339939, "Tk", lambda: Tk))
_l_(339941)
frame = _c_(339944, _n_(339942, "Frame", lambda: Frame), _n_(339943, "root", lambda: root))
_l_(339945)

#other codes

def net_connection_error():
    _l_(339950)

    #print(dir(messagebox))
    _c_(339948, _a_(339947, _n_(339946, "messagebox", lambda: messagebox), "INFO"), "info",
        "No Connection!"
    )
    _l_(339949)

#other codes

_c_(339952, _n_(339951, "net_connection_error", lambda: net_connection_error))
_l_(339953)

#other codes

_c_(339956, _a_(339955, _n_(339954, "root", lambda: root), "mainloop"))
_l_(339957)