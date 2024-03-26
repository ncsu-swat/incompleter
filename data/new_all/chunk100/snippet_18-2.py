# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(103808)

except ImportError:
    pass
array1 = _c_(103811, _a_(103810, _n_(103809, "np", lambda: np), "array"), [1, 7, 8, 2, 0.1, 3, 15, 2.5])
_l_(103812)
_c_(103814, _n_(103813, "print", lambda: print), 'Original arrays:')
_l_(103815)
_c_(103818, _n_(103816, "print", lambda: print), _n_(103817, "array1", lambda: array1))
_l_(103819)
result = _c_(103824, _a_(103821, _n_(103820, "np", lambda: np), "argpartition"), _n_(103822, "array1", lambda: array1), _n_(103823, "k", lambda: k))
_l_(103825)
_c_(103827, _n_(103826, "print", lambda: print), '\nk smallest values:')
_l_(103828)
_c_(103833, _n_(103829, "print", lambda: print), _n_(103830, "array1", lambda: array1)[_n_(103831, "result", lambda: result)[:_n_(103832, "k", lambda: k)]])
_l_(103834)