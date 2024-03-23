# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(55773)

except ImportError:
    pass
nums2 = _c_(55777, _a_(55776, _a_(55775, _n_(55774, "np", lambda: np), "random"), "randint"), 0, 6, (2, 3))
_l_(55778)
_c_(55780, _n_(55779, "print", lambda: print), 'Original arrays:')
_l_(55781)
_c_(55784, _n_(55782, "print", lambda: print), _n_(55783, "nums1", lambda: nums1))
_l_(55785)
_c_(55788, _n_(55786, "print", lambda: print), '\n', _n_(55787, "nums2", lambda: nums2))
_l_(55789)
temp = _n_(55790, "nums1", lambda: nums1)[..., _a_(55792, _n_(55791, "np", lambda: np), "newaxis"), _a_(55794, _n_(55793, "np", lambda: np), "newaxis")] == _n_(55795, "nums2", lambda: nums2)
_l_(55796)
rows = _c_(55803, _a_(55802, (_c_(55799, _a_(55798, _n_(55797, "temp", lambda: temp), "sum"), axis=(1, 2, 3)) >= _a_(55801, _n_(55800, "nums2", lambda: nums2), "shape")[1]), "nonzero"))[0]
_l_(55804)
_c_(55806, _n_(55805, "print", lambda: print), '\nRows of a given array that contain elements of each row of another given array:')
_l_(55807)
_c_(55810, _n_(55808, "print", lambda: print), _n_(55809, "rows", lambda: rows))
_l_(55811)