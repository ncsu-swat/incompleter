# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(103785)

except ImportError:
    pass
array1 = _c_(103788, _a_(103787, _n_(103786, "np", lambda: np), "array"), [1, 7, 8, 2, 0.1, 3, 15, 2.5])
_l_(103789)
_c_(103791, _n_(103790, "print", lambda: print), 'Original arrays:')
_l_(103792)
_c_(103795, _n_(103793, "print", lambda: print), _n_(103794, "array1", lambda: array1))
_l_(103796)
k = 4
_l_(103797)
_c_(103799, _n_(103798, "print", lambda: print), '\nk smallest values:')
_l_(103800)
_c_(103805, _n_(103801, "print", lambda: print), _n_(103802, "array1", lambda: array1)[_n_(103803, "result", lambda: result)[:_n_(103804, "k", lambda: k)]])
_l_(103806)