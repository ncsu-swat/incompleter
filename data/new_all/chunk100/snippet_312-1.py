# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(109915)

except ImportError:
    pass
array1 = _c_(109918, _a_(109917, _n_(109916, "np", lambda: np), "array"), [0, 10, 20, 40, 60, 80])
_l_(109919)
_c_(109922, _n_(109920, "print", lambda: print), 'Array1: ', _n_(109921, "array1", lambda: array1))
_l_(109923)
_c_(109926, _n_(109924, "print", lambda: print), 'Array2: ', _n_(109925, "array2", lambda: array2))
_l_(109927)
_c_(109929, _n_(109928, "print", lambda: print), 'Unique sorted array of values that are in either of the two input arrays:')
_l_(109930)
_c_(109937, _n_(109931, "print", lambda: print), _c_(109936, _a_(109933, _n_(109932, "np", lambda: np), "union1d"), _n_(109934, "array1", lambda: array1), _n_(109935, "array2", lambda: array2)))
_l_(109938)