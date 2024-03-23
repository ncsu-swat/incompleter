# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(73902)

except ImportError:
    pass
array1 = _c_(73905, _a_(73904, _n_(73903, "np", lambda: np), "array"), [0, 10, 20, 40, 60])
_l_(73906)
_c_(73909, _n_(73907, "print", lambda: print), 'Array1: ', _n_(73908, "array1", lambda: array1))
_l_(73910)
_c_(73913, _n_(73911, "print", lambda: print), 'Array2: ', _n_(73912, "array2", lambda: array2))
_l_(73914)
_c_(73916, _n_(73915, "print", lambda: print), 'Common values between two arrays:')
_l_(73917)
_c_(73924, _n_(73918, "print", lambda: print), _c_(73923, _a_(73920, _n_(73919, "np", lambda: np), "intersect1d"), _n_(73921, "array1", lambda: array1), _n_(73922, "array2", lambda: array2)))
_l_(73925)