# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(119744)

except ImportError:
    pass
x = _c_(119747, _a_(119746, _n_(119745, "np", lambda: np), "array"), [-180.0, -90.0, 90.0, 180.0])
_l_(119748)
r1 = _c_(119752, _a_(119750, _n_(119749, "np", lambda: np), "radians"), _n_(119751, "x", lambda: x))
_l_(119753)
assert _c_(119758, _a_(119755, _n_(119754, "np", lambda: np), "array_equiv"), _n_(119756, "r1", lambda: r1), _n_(119757, "r2", lambda: r2))
_l_(119759)
_c_(119762, _n_(119760, "print", lambda: print), _n_(119761, "r1", lambda: r1))
_l_(119763)