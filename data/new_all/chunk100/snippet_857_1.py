# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(84635)

except ImportError:
    pass
array_nums2 = _c_(84644, _a_(84637, _n_(84636, "np", lambda: np), "array"), [[1, 2, _a_(84639, _n_(84638, "np", lambda: np), "nan")], [4, 5, 6], [_a_(84641, _n_(84640, "np", lambda: np), "nan"), 7, _a_(84643, _n_(84642, "np", lambda: np), "nan")]])
_l_(84645)
_c_(84647, _n_(84646, "print", lambda: print), 'Original arrays:')
_l_(84648)
_c_(84651, _n_(84649, "print", lambda: print), _n_(84650, "array_nums1", lambda: array_nums1))
_l_(84652)
_c_(84655, _n_(84653, "print", lambda: print), _n_(84654, "array_nums2", lambda: array_nums2))
_l_(84656)
_c_(84658, _n_(84657, "print", lambda: print), '\nAll the nan of array_nums2 replaced by the mean of array_nums1:')
_l_(84659)
_n_(84660, "array_nums2", lambda: array_nums2)[_c_(84664, _a_(84662, _n_(84661, "np", lambda: np), "isnan"), _n_(84663, "array_nums2", lambda: array_nums2))] = _c_(84668, _a_(84666, _n_(84665, "np", lambda: np), "nanmean"), _n_(84667, "array_nums1", lambda: array_nums1))
_l_(84669)
_c_(84672, _n_(84670, "print", lambda: print), _n_(84671, "array_nums2", lambda: array_nums2))
_l_(84673)