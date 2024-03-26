# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(119765)

except ImportError:
    pass
x = _c_(119768, _a_(119767, _n_(119766, "np", lambda: np), "array"), [-180.0, -90.0, 90.0, 180.0])
_l_(119769)
r2 = _c_(119773, _a_(119771, _n_(119770, "np", lambda: np), "deg2rad"), _n_(119772, "x", lambda: x))
_l_(119774)
assert _c_(119779, _a_(119776, _n_(119775, "np", lambda: np), "array_equiv"), _n_(119777, "r1", lambda: r1), _n_(119778, "r2", lambda: r2))
_l_(119780)
_c_(119783, _n_(119781, "print", lambda: print), _n_(119782, "r1", lambda: r1))
_l_(119784)