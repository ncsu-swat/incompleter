# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105560)

except ImportError:
    pass
_c_(105562, _n_(105561, "print", lambda: print), 'Empty array:')
_l_(105563)
_c_(105566, _n_(105564, "print", lambda: print), _n_(105565, "arr", lambda: arr))
_l_(105567)
arr = _c_(105574, _a_(105569, _n_(105568, "np", lambda: np), "append"), _n_(105570, "arr", lambda: arr), _c_(105573, _a_(105572, _n_(105571, "np", lambda: np), "array"), [[10, 20, 30]]), axis=0)
_l_(105575)
arr = _c_(105582, _a_(105577, _n_(105576, "np", lambda: np), "append"), _n_(105578, "arr", lambda: arr), _c_(105581, _a_(105580, _n_(105579, "np", lambda: np), "array"), [[40, 50, 60]]), axis=0)
_l_(105583)
_c_(105585, _n_(105584, "print", lambda: print), 'After adding two new arrays:')
_l_(105586)
_c_(105589, _n_(105587, "print", lambda: print), _n_(105588, "arr", lambda: arr))
_l_(105590)