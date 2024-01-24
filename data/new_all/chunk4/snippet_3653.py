# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70628464/importerror-or-attributeerror-while-using-tkinter
#testUI.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(643018)

except ImportError:
    pass
try:
    from test2 import nameit
    _l_(643020)

except ImportError:
    pass


root = _c_(643022, _n_(643021, "Tk", lambda: Tk))
_l_(643023)
_c_(643026, _a_(643025, _n_(643024, "root", lambda: root), "title"), 'Scott Window')
_l_(643027)
_c_(643030, _a_(643029, _n_(643028, "root", lambda: root), "geometry"), '500x350')
_l_(643031)

greet = _c_(643033, _n_(643032, "nameit", lambda: nameit), 'John')
_l_(643034)

mylabel = _c_(643038, _n_(643035, "Label", lambda: Label), _n_(643036, "root", lambda: root), text=_n_(643037, "greet", lambda: greet))
_l_(643039)
_c_(643042, _a_(643041, _n_(643040, "mylabel", lambda: mylabel), "pack"), pady=20)
_l_(643043)


_c_(643046, _a_(643045, _n_(643044, "root", lambda: root), "mainloop"))
_l_(643047)