# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(34615)

except ImportError:
    pass
x = _c_(34618, _a_(34617, _n_(34616, "np", lambda: np), "array"), [[1, 2, 3], [4, 5, 6]])
_l_(34619)
_c_(34621, _n_(34620, "print", lambda: print), 'Original array: ')
_l_(34622)
_c_(34625, _n_(34623, "print", lambda: print), _n_(34624, "x", lambda: x))
_l_(34626)
_c_(34628, _n_(34627, "print", lambda: print), 'Cumulative product  of the elements along a given axis:')
_l_(34629)
r = _c_(34633, _a_(34631, _n_(34630, "np", lambda: np), "cumprod"), _n_(34632, "x", lambda: x))
_l_(34634)
_c_(34637, _n_(34635, "print", lambda: print), _n_(34636, "r", lambda: r))
_l_(34638)
_c_(34640, _n_(34639, "print", lambda: print), '\nProduct over rows for each of the 3 columns:')
_l_(34641)
r = _c_(34645, _a_(34643, _n_(34642, "np", lambda: np), "cumprod"), _n_(34644, "x", lambda: x), axis=0)
_l_(34646)
_c_(34649, _n_(34647, "print", lambda: print), _n_(34648, "r", lambda: r))
_l_(34650)
_c_(34652, _n_(34651, "print", lambda: print), '\nProduct  over columns for each of the 2 rows:')
_l_(34653)
_c_(34656, _n_(34654, "print", lambda: print), _n_(34655, "r", lambda: r))
_l_(34657)