# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64989)

except ImportError:
    pass
a = _c_(64992, _a_(64991, _n_(64990, "np", lambda: np), "array"), [1, 2, 3])
_l_(64993)
b = _c_(64996, _a_(64995, _n_(64994, "np", lambda: np), "array"), [0, 1, 0])
_l_(64997)
_c_(64999, _n_(64998, "print", lambda: print), 'Original 1-d arrays:')
_l_(65000)
_c_(65003, _n_(65001, "print", lambda: print), _n_(65002, "a", lambda: a))
_l_(65004)
_c_(65007, _n_(65005, "print", lambda: print), _n_(65006, "b", lambda: b))
_l_(65008)
result = _c_(65013, _a_(65010, _n_(65009, "np", lambda: np), "einsum"), 'n,n', _n_(65011, "a", lambda: a), _n_(65012, "b", lambda: b))
_l_(65014)
_c_(65016, _n_(65015, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(65017)
_c_(65020, _n_(65018, "print", lambda: print), _n_(65019, "result", lambda: result))
_l_(65021)
x = _c_(65026, _a_(65025, _c_(65024, _a_(65023, _n_(65022, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(65027)
_c_(65029, _n_(65028, "print", lambda: print), 'Original Higher dimension:')
_l_(65030)
_c_(65033, _n_(65031, "print", lambda: print), _n_(65032, "x", lambda: x))
_l_(65034)
_c_(65037, _n_(65035, "print", lambda: print), _n_(65036, "y", lambda: y))
_l_(65038)
result = _c_(65043, _a_(65040, _n_(65039, "np", lambda: np), "einsum"), 'mk,kn', _n_(65041, "x", lambda: x), _n_(65042, "y", lambda: y))
_l_(65044)
_c_(65046, _n_(65045, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(65047)
_c_(65050, _n_(65048, "print", lambda: print), _n_(65049, "result", lambda: result))
_l_(65051)