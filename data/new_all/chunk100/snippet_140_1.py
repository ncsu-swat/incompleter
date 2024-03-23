# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(9831)

except ImportError:
    pass
x = _c_(9834, _a_(9833, _n_(9832, "np", lambda: np), "array"), [0, 1, 3])
_l_(9835)
_c_(9837, _n_(9836, "print", lambda: print), '\nOriginal array1:')
_l_(9838)
_c_(9841, _n_(9839, "print", lambda: print), _n_(9840, "x", lambda: x))
_l_(9842)
_c_(9844, _n_(9843, "print", lambda: print), '\nOriginal array1:')
_l_(9845)
_c_(9848, _n_(9846, "print", lambda: print), _n_(9847, "y", lambda: y))
_l_(9849)
_c_(9856, _n_(9850, "print", lambda: print), '\nCross-correlation of the said arrays:\n', _c_(9855, _a_(9852, _n_(9851, "np", lambda: np), "cov"), _n_(9853, "x", lambda: x), _n_(9854, "y", lambda: y)))
_l_(9857)