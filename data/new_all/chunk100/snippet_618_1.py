# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64797)

except ImportError:
    pass
_c_(64800, _n_(64798, "print", lambda: print), 'Array1: ', _n_(64799, "array1", lambda: array1))
_l_(64801)
array2 = [10, 30, 40, 50, 70]
_l_(64802)
_c_(64805, _n_(64803, "print", lambda: print), 'Array2: ', _n_(64804, "array2", lambda: array2))
_l_(64806)
_c_(64808, _n_(64807, "print", lambda: print), 'Unique values in array1 that are not in array2:')
_l_(64809)
_c_(64816, _n_(64810, "print", lambda: print), _c_(64815, _a_(64812, _n_(64811, "np", lambda: np), "setdiff1d"), _n_(64813, "array1", lambda: array1), _n_(64814, "array2", lambda: array2)))
_l_(64817)