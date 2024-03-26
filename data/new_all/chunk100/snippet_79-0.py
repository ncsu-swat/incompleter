# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(120311)

except ImportError:
    pass
x, y = _c_(120316, _a_(120313, _n_(120312, "np", lambda: np), "atleast_2d"), _n_(120314, "a", lambda: a)[:, 0], _n_(120315, "a", lambda: a)[:, 1])
_l_(120317)
d = _c_(120326, _a_(120319, _n_(120318, "np", lambda: np), "sqrt"), (_n_(120320, "x", lambda: x) - _a_(120322, _n_(120321, "x", lambda: x), "T")) ** 2 + (_n_(120323, "y", lambda: y) - _a_(120325, _n_(120324, "y", lambda: y), "T")) ** 2)
_l_(120327)
_c_(120330, _n_(120328, "print", lambda: print), _n_(120329, "d", lambda: d))
_l_(120331)