# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(18758)

except ImportError:
    pass
_c_(18760, _n_(18759, "print", lambda: print), 'Original array: ')
_l_(18761)
_c_(18764, _n_(18762, "print", lambda: print), _n_(18763, "x", lambda: x))
_l_(18765)
r1 = _c_(18769, _a_(18767, _n_(18766, "np", lambda: np), "negative"), _n_(18768, "x", lambda: x))
_l_(18770)
r2 = -_n_(18771, "x", lambda: x)
_l_(18772)
assert _c_(18777, _a_(18774, _n_(18773, "np", lambda: np), "array_equal"), _n_(18775, "r1", lambda: r1), _n_(18776, "r2", lambda: r2))
_l_(18778)
_c_(18780, _n_(18779, "print", lambda: print), 'Numerical negative value for all elements of the said array:')
_l_(18781)
_c_(18784, _n_(18782, "print", lambda: print), _n_(18783, "r1", lambda: r1))
_l_(18785)