# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(29497)

except ImportError:
    pass
_c_(29500, _n_(29498, "print", lambda: print), 'Array1: ', _n_(29499, "array1", lambda: array1))
_l_(29501)
array2 = [10, 30, 40, 50, 70]
_l_(29502)
_c_(29505, _n_(29503, "print", lambda: print), 'Array2: ', _n_(29504, "array2", lambda: array2))
_l_(29506)
_c_(29508, _n_(29507, "print", lambda: print), 'Unique sorted array of values that are in either of the two input arrays:')
_l_(29509)
_c_(29516, _n_(29510, "print", lambda: print), _c_(29515, _a_(29512, _n_(29511, "np", lambda: np), "union1d"), _n_(29513, "array1", lambda: array1), _n_(29514, "array2", lambda: array2)))
_l_(29517)