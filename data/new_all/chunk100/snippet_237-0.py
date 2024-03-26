# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106304)

except ImportError:
    pass
x = _c_(106307, _a_(106306, _n_(106305, "np", lambda: np), "array"), [0, 1, -1])
_l_(106308)
_c_(106310, _n_(106309, "print", lambda: print), 'Original array: ')
_l_(106311)
_c_(106314, _n_(106312, "print", lambda: print), _n_(106313, "x", lambda: x))
_l_(106315)
r2 = -_n_(106316, "x", lambda: x)
_l_(106317)
assert _c_(106322, _a_(106319, _n_(106318, "np", lambda: np), "array_equal"), _n_(106320, "r1", lambda: r1), _n_(106321, "r2", lambda: r2))
_l_(106323)
_c_(106325, _n_(106324, "print", lambda: print), 'Numerical negative value for all elements of the said array:')
_l_(106326)
_c_(106329, _n_(106327, "print", lambda: print), _n_(106328, "r1", lambda: r1))
_l_(106330)