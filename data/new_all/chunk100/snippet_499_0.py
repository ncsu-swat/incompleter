# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51966)

except ImportError:
    pass
_c_(51968, _n_(51967, "print", lambda: print), 'Original array:')
_l_(51969)
_c_(51972, _n_(51970, "print", lambda: print), _n_(51971, "arr1", lambda: arr1))
_l_(51973)
result = _c_(51979, _a_(51975, _n_(51974, "np", lambda: np), "mean"), _c_(51978, _a_(51977, _n_(51976, "arr1", lambda: arr1), "reshape"), -1, 3), axis=1)
_l_(51980)
_c_(51982, _n_(51981, "print", lambda: print), 'Average of every consecutive triplet of elements of the said array:')
_l_(51983)
_c_(51986, _n_(51984, "print", lambda: print), _n_(51985, "result", lambda: result))
_l_(51987)