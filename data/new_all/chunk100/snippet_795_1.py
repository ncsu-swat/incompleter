# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80408)

except ImportError:
    pass
_c_(80411, _n_(80409, "print", lambda: print), 'Array1: ', _n_(80410, "array1", lambda: array1))
_l_(80412)
array2 = [10, 30, 40, 50, 70]
_l_(80413)
_c_(80416, _n_(80414, "print", lambda: print), 'Array2: ', _n_(80415, "array2", lambda: array2))
_l_(80417)
_c_(80419, _n_(80418, "print", lambda: print), 'Unique values that are in only one (not both) of the input arrays:')
_l_(80420)
_c_(80427, _n_(80421, "print", lambda: print), _c_(80426, _a_(80423, _n_(80422, "np", lambda: np), "setxor1d"), _n_(80424, "array1", lambda: array1), _n_(80425, "array2", lambda: array2)))
_l_(80428)