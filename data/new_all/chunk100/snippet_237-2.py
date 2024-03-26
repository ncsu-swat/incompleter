# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106363)

except ImportError:
    pass
_c_(106365, _n_(106364, "print", lambda: print), 'Original array: ')
_l_(106366)
_c_(106369, _n_(106367, "print", lambda: print), _n_(106368, "x", lambda: x))
_l_(106370)
r1 = _c_(106374, _a_(106372, _n_(106371, "np", lambda: np), "negative"), _n_(106373, "x", lambda: x))
_l_(106375)
r2 = -_n_(106376, "x", lambda: x)
_l_(106377)
assert _c_(106382, _a_(106379, _n_(106378, "np", lambda: np), "array_equal"), _n_(106380, "r1", lambda: r1), _n_(106381, "r2", lambda: r2))
_l_(106383)
_c_(106385, _n_(106384, "print", lambda: print), 'Numerical negative value for all elements of the said array:')
_l_(106386)
_c_(106389, _n_(106387, "print", lambda: print), _n_(106388, "r1", lambda: r1))
_l_(106390)