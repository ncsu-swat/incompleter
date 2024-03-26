# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(113917)

except ImportError:
    pass
_c_(113919, _n_(113918, "print", lambda: print), 'Original array:')
_l_(113920)
_c_(113923, _n_(113921, "print", lambda: print), _n_(113922, "x", lambda: x))
_l_(113924)
y = _c_(113928, _a_(113926, _n_(113925, "np", lambda: np), "empty_like"), _n_(113927, "x", lambda: x))
_l_(113929)
_n_(113930, "y", lambda: y)[:] = _n_(113931, "x", lambda: x)
_l_(113932)
_c_(113934, _n_(113933, "print", lambda: print), '\nCopy of the said array:')
_l_(113935)
_c_(113938, _n_(113936, "print", lambda: print), _n_(113937, "y", lambda: y))
_l_(113939)