# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(34526)

except ImportError:
    pass
x = _c_(34529, _a_(34528, _n_(34527, "np", lambda: np), "array"), [[1, 2, 3], [4, 5, 6]])
_l_(34530)
_c_(34532, _n_(34531, "print", lambda: print), 'Original array: ')
_l_(34533)
_c_(34536, _n_(34534, "print", lambda: print), _n_(34535, "x", lambda: x))
_l_(34537)
_c_(34539, _n_(34538, "print", lambda: print), 'Cumulative product  of the elements along a given axis:')
_l_(34540)
_c_(34543, _n_(34541, "print", lambda: print), _n_(34542, "r", lambda: r))
_l_(34544)
_c_(34546, _n_(34545, "print", lambda: print), '\nProduct over rows for each of the 3 columns:')
_l_(34547)
r = _c_(34551, _a_(34549, _n_(34548, "np", lambda: np), "cumprod"), _n_(34550, "x", lambda: x), axis=0)
_l_(34552)
_c_(34555, _n_(34553, "print", lambda: print), _n_(34554, "r", lambda: r))
_l_(34556)
_c_(34558, _n_(34557, "print", lambda: print), '\nProduct  over columns for each of the 2 rows:')
_l_(34559)
r = _c_(34563, _a_(34561, _n_(34560, "np", lambda: np), "cumprod"), _n_(34562, "x", lambda: x), axis=1)
_l_(34564)
_c_(34567, _n_(34565, "print", lambda: print), _n_(34566, "r", lambda: r))
_l_(34568)