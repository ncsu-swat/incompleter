# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(78950)

except ImportError:
    pass
(x, y) = (_n_(78951, "z", lambda: z)[:, 0], _n_(78952, "z", lambda: z)[:, 1])
_l_(78953)
r = _c_(78958, _a_(78955, _n_(78954, "np", lambda: np), "sqrt"), _n_(78956, "x", lambda: x) ** 2 + _n_(78957, "y", lambda: y) ** 2)
_l_(78959)
t = _c_(78964, _a_(78961, _n_(78960, "np", lambda: np), "arctan2"), _n_(78962, "y", lambda: y), _n_(78963, "x", lambda: x))
_l_(78965)
_c_(78968, _n_(78966, "print", lambda: print), _n_(78967, "r", lambda: r))
_l_(78969)
_c_(78972, _n_(78970, "print", lambda: print), _n_(78971, "t", lambda: t))
_l_(78973)