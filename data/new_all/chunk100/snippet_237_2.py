# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(18787)

except ImportError:
    pass
x = _c_(18790, _a_(18789, _n_(18788, "np", lambda: np), "array"), [0, 1, -1])
_l_(18791)
_c_(18793, _n_(18792, "print", lambda: print), 'Original array: ')
_l_(18794)
_c_(18797, _n_(18795, "print", lambda: print), _n_(18796, "x", lambda: x))
_l_(18798)
r1 = _c_(18802, _a_(18800, _n_(18799, "np", lambda: np), "negative"), _n_(18801, "x", lambda: x))
_l_(18803)
assert _c_(18808, _a_(18805, _n_(18804, "np", lambda: np), "array_equal"), _n_(18806, "r1", lambda: r1), _n_(18807, "r2", lambda: r2))
_l_(18809)
_c_(18811, _n_(18810, "print", lambda: print), 'Numerical negative value for all elements of the said array:')
_l_(18812)
_c_(18815, _n_(18813, "print", lambda: print), _n_(18814, "r1", lambda: r1))
_l_(18816)