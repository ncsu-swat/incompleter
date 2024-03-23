# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(35700)

except ImportError:
    pass
a = _c_(35703, _a_(35702, _n_(35701, "np", lambda: np), "array"), [[4, 6], [2, 1]])
_l_(35704)
_c_(35706, _n_(35705, "print", lambda: print), 'Original array: ')
_l_(35707)
_c_(35710, _n_(35708, "print", lambda: print), _n_(35709, "a", lambda: a))
_l_(35711)
_c_(35713, _n_(35712, "print", lambda: print), 'Sort along the first axis: ')
_l_(35714)
_c_(35717, _n_(35715, "print", lambda: print), _n_(35716, "x", lambda: x))
_l_(35718)
_c_(35720, _n_(35719, "print", lambda: print), 'Sort along the last axis: ')
_l_(35721)
y = _c_(35725, _a_(35723, _n_(35722, "np", lambda: np), "sort"), _n_(35724, "x", lambda: x), axis=1)
_l_(35726)
_c_(35729, _n_(35727, "print", lambda: print), _n_(35728, "y", lambda: y))
_l_(35730)