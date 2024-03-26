# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(110959)

except ImportError:
    pass
x = _c_(110963, _a_(110962, _a_(110961, _n_(110960, "np", lambda: np), "random"), "uniform"), 1, 12, 5)
_l_(110964)
n = _a_(110966, _n_(110965, "x", lambda: x), "flat")[_c_(110973, _a_(110972, _c_(110971, _a_(110968, _n_(110967, "np", lambda: np), "abs"), _n_(110969, "x", lambda: x) - _n_(110970, "v", lambda: v)), "argmin"))]
_l_(110974)
_c_(110977, _n_(110975, "print", lambda: print), _n_(110976, "n", lambda: n))
_l_(110978)