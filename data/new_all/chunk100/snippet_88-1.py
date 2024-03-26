# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(121056)

except ImportError:
    pass
x = _c_(121059, _a_(121058, _n_(121057, "np", lambda: np), "array"), [1.0, 2.0, 0.2, 0.3])
_l_(121060)
_c_(121062, _n_(121061, "print", lambda: print), 'Original array: ')
_l_(121063)
_c_(121066, _n_(121064, "print", lambda: print), _n_(121065, "x", lambda: x))
_l_(121067)
r1 = _c_(121071, _a_(121069, _n_(121068, "np", lambda: np), "reciprocal"), _n_(121070, "x", lambda: x))
_l_(121072)
assert _c_(121077, _a_(121074, _n_(121073, "np", lambda: np), "array_equal"), _n_(121075, "r1", lambda: r1), _n_(121076, "r2", lambda: r2))
_l_(121078)
_c_(121080, _n_(121079, "print", lambda: print), 'Reciprocal for all elements of the said array:')
_l_(121081)
_c_(121084, _n_(121082, "print", lambda: print), _n_(121083, "r1", lambda: r1))
_l_(121085)