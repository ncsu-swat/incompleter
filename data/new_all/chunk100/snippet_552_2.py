# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(55851)

except ImportError:
    pass
nums1 = _c_(55855, _a_(55854, _a_(55853, _n_(55852, "np", lambda: np), "random"), "randint"), 0, 6, (6, 4))
_l_(55856)
_c_(55858, _n_(55857, "print", lambda: print), 'Original arrays:')
_l_(55859)
_c_(55862, _n_(55860, "print", lambda: print), _n_(55861, "nums1", lambda: nums1))
_l_(55863)
_c_(55866, _n_(55864, "print", lambda: print), '\n', _n_(55865, "nums2", lambda: nums2))
_l_(55867)
temp = _n_(55868, "nums1", lambda: nums1)[..., _a_(55870, _n_(55869, "np", lambda: np), "newaxis"), _a_(55872, _n_(55871, "np", lambda: np), "newaxis")] == _n_(55873, "nums2", lambda: nums2)
_l_(55874)
rows = _c_(55881, _a_(55880, (_c_(55877, _a_(55876, _n_(55875, "temp", lambda: temp), "sum"), axis=(1, 2, 3)) >= _a_(55879, _n_(55878, "nums2", lambda: nums2), "shape")[1]), "nonzero"))[0]
_l_(55882)
_c_(55884, _n_(55883, "print", lambda: print), '\nRows of a given array that contain elements of each row of another given array:')
_l_(55885)
_c_(55888, _n_(55886, "print", lambda: print), _n_(55887, "rows", lambda: rows))
_l_(55889)