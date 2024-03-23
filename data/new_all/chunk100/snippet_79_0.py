# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80799)

except ImportError:
    pass
(x, y) = _c_(80804, _a_(80801, _n_(80800, "np", lambda: np), "atleast_2d"), _n_(80802, "a", lambda: a)[:, 0], _n_(80803, "a", lambda: a)[:, 1])
_l_(80805)
d = _c_(80814, _a_(80807, _n_(80806, "np", lambda: np), "sqrt"), (_n_(80808, "x", lambda: x) - _a_(80810, _n_(80809, "x", lambda: x), "T")) ** 2 + (_n_(80811, "y", lambda: y) - _a_(80813, _n_(80812, "y", lambda: y), "T")) ** 2)
_l_(80815)
_c_(80818, _n_(80816, "print", lambda: print), _n_(80817, "d", lambda: d))
_l_(80819)