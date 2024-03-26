# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(103760)

except ImportError:
    pass
_c_(103762, _n_(103761, "print", lambda: print), 'Original arrays:')
_l_(103763)
_c_(103766, _n_(103764, "print", lambda: print), _n_(103765, "array1", lambda: array1))
_l_(103767)
k = 4
_l_(103768)
result = _c_(103773, _a_(103770, _n_(103769, "np", lambda: np), "argpartition"), _n_(103771, "array1", lambda: array1), _n_(103772, "k", lambda: k))
_l_(103774)
_c_(103776, _n_(103775, "print", lambda: print), '\nk smallest values:')
_l_(103777)
_c_(103782, _n_(103778, "print", lambda: print), _n_(103779, "array1", lambda: array1)[_n_(103780, "result", lambda: result)[:_n_(103781, "k", lambda: k)]])
_l_(103783)