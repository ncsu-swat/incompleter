# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(121087)

except ImportError:
    pass
_c_(121089, _n_(121088, "print", lambda: print), 'Original array: ')
_l_(121090)
_c_(121093, _n_(121091, "print", lambda: print), _n_(121092, "x", lambda: x))
_l_(121094)
r1 = _c_(121098, _a_(121096, _n_(121095, "np", lambda: np), "reciprocal"), _n_(121097, "x", lambda: x))
_l_(121099)
r2 = 1 / _n_(121100, "x", lambda: x)
_l_(121101)
assert _c_(121106, _a_(121103, _n_(121102, "np", lambda: np), "array_equal"), _n_(121104, "r1", lambda: r1), _n_(121105, "r2", lambda: r2))
_l_(121107)
_c_(121109, _n_(121108, "print", lambda: print), 'Reciprocal for all elements of the said array:')
_l_(121110)
_c_(121113, _n_(121111, "print", lambda: print), _n_(121112, "r1", lambda: r1))
_l_(121114)