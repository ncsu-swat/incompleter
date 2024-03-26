# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(109893)

except ImportError:
    pass
_c_(109896, _n_(109894, "print", lambda: print), 'Array1: ', _n_(109895, "array1", lambda: array1))
_l_(109897)
array2 = [10, 30, 40, 50, 70]
_l_(109898)
_c_(109901, _n_(109899, "print", lambda: print), 'Array2: ', _n_(109900, "array2", lambda: array2))
_l_(109902)
_c_(109904, _n_(109903, "print", lambda: print), 'Unique sorted array of values that are in either of the two input arrays:')
_l_(109905)
_c_(109912, _n_(109906, "print", lambda: print), _c_(109911, _a_(109908, _n_(109907, "np", lambda: np), "union1d"), _n_(109909, "array1", lambda: array1), _n_(109910, "array2", lambda: array2)))
_l_(109913)