# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(18730)

except ImportError:
    pass
x = _c_(18733, _a_(18732, _n_(18731, "np", lambda: np), "array"), [0, 1, -1])
_l_(18734)
_c_(18736, _n_(18735, "print", lambda: print), 'Original array: ')
_l_(18737)
_c_(18740, _n_(18738, "print", lambda: print), _n_(18739, "x", lambda: x))
_l_(18741)
r2 = -_n_(18742, "x", lambda: x)
_l_(18743)
assert _c_(18748, _a_(18745, _n_(18744, "np", lambda: np), "array_equal"), _n_(18746, "r1", lambda: r1), _n_(18747, "r2", lambda: r2))
_l_(18749)
_c_(18751, _n_(18750, "print", lambda: print), 'Numerical negative value for all elements of the said array:')
_l_(18752)
_c_(18755, _n_(18753, "print", lambda: print), _n_(18754, "r1", lambda: r1))
_l_(18756)