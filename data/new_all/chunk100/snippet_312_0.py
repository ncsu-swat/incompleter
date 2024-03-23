# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(29472)

except ImportError:
    pass
array1 = _c_(29475, _a_(29474, _n_(29473, "np", lambda: np), "array"), [0, 10, 20, 40, 60, 80])
_l_(29476)
_c_(29479, _n_(29477, "print", lambda: print), 'Array1: ', _n_(29478, "array1", lambda: array1))
_l_(29480)
_c_(29483, _n_(29481, "print", lambda: print), 'Array2: ', _n_(29482, "array2", lambda: array2))
_l_(29484)
_c_(29486, _n_(29485, "print", lambda: print), 'Unique sorted array of values that are in either of the two input arrays:')
_l_(29487)
_c_(29494, _n_(29488, "print", lambda: print), _c_(29493, _a_(29490, _n_(29489, "np", lambda: np), "union1d"), _n_(29491, "array1", lambda: array1), _n_(29492, "array2", lambda: array2)))
_l_(29495)