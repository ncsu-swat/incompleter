# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(34482)

except ImportError:
    pass
x = _c_(34485, _a_(34484, _n_(34483, "np", lambda: np), "array"), [[1, 2, 3], [4, 5, 6]])
_l_(34486)
_c_(34488, _n_(34487, "print", lambda: print), 'Original array: ')
_l_(34489)
_c_(34492, _n_(34490, "print", lambda: print), _n_(34491, "x", lambda: x))
_l_(34493)
_c_(34495, _n_(34494, "print", lambda: print), 'Cumulative product  of the elements along a given axis:')
_l_(34496)
r = _c_(34500, _a_(34498, _n_(34497, "np", lambda: np), "cumprod"), _n_(34499, "x", lambda: x))
_l_(34501)
_c_(34504, _n_(34502, "print", lambda: print), _n_(34503, "r", lambda: r))
_l_(34505)
_c_(34507, _n_(34506, "print", lambda: print), '\nProduct over rows for each of the 3 columns:')
_l_(34508)
_c_(34511, _n_(34509, "print", lambda: print), _n_(34510, "r", lambda: r))
_l_(34512)
_c_(34514, _n_(34513, "print", lambda: print), '\nProduct  over columns for each of the 2 rows:')
_l_(34515)
r = _c_(34519, _a_(34517, _n_(34516, "np", lambda: np), "cumprod"), _n_(34518, "x", lambda: x), axis=1)
_l_(34520)
_c_(34523, _n_(34521, "print", lambda: print), _n_(34522, "r", lambda: r))
_l_(34524)