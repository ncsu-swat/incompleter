# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80383)

except ImportError:
    pass
array1 = _c_(80386, _a_(80385, _n_(80384, "np", lambda: np), "array"), [0, 10, 20, 40, 60, 80])
_l_(80387)
_c_(80390, _n_(80388, "print", lambda: print), 'Array1: ', _n_(80389, "array1", lambda: array1))
_l_(80391)
_c_(80394, _n_(80392, "print", lambda: print), 'Array2: ', _n_(80393, "array2", lambda: array2))
_l_(80395)
_c_(80397, _n_(80396, "print", lambda: print), 'Unique values that are in only one (not both) of the input arrays:')
_l_(80398)
_c_(80405, _n_(80399, "print", lambda: print), _c_(80404, _a_(80401, _n_(80400, "np", lambda: np), "setxor1d"), _n_(80402, "array1", lambda: array1), _n_(80403, "array2", lambda: array2)))
_l_(80406)