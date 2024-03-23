# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(32782)

except ImportError:
    pass
x = _c_(32785, _a_(32784, _n_(32783, "np", lambda: np), "array"), [[1, 2, 3], [4, 5, 6]])
_l_(32786)
_c_(32788, _n_(32787, "print", lambda: print), 'Original array: ')
_l_(32789)
_c_(32792, _n_(32790, "print", lambda: print), _n_(32791, "x", lambda: x))
_l_(32793)
_c_(32795, _n_(32794, "print", lambda: print), 'Cumulative sum of the elements along a given axis:')
_l_(32796)
_c_(32799, _n_(32797, "print", lambda: print), _n_(32798, "r", lambda: r))
_l_(32800)
_c_(32802, _n_(32801, "print", lambda: print), '\nSum over rows for each of the 3 columns:')
_l_(32803)
r = _c_(32807, _a_(32805, _n_(32804, "np", lambda: np), "cumsum"), _n_(32806, "x", lambda: x), axis=0)
_l_(32808)
_c_(32811, _n_(32809, "print", lambda: print), _n_(32810, "r", lambda: r))
_l_(32812)
_c_(32814, _n_(32813, "print", lambda: print), '\nSum over columns for each of the 2 rows:')
_l_(32815)
r = _c_(32819, _a_(32817, _n_(32816, "np", lambda: np), "cumsum"), _n_(32818, "x", lambda: x), axis=1)
_l_(32820)
_c_(32823, _n_(32821, "print", lambda: print), _n_(32822, "r", lambda: r))
_l_(32824)