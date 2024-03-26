# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105634)

except ImportError:
    pass
nums1 = _c_(105637, _a_(105636, _n_(105635, "np", lambda: np), "array"), [[2, 5, 2], [1, 5, 5]])
_l_(105638)
_c_(105640, _n_(105639, "print", lambda: print), 'Array1:')
_l_(105641)
_c_(105644, _n_(105642, "print", lambda: print), _n_(105643, "nums1", lambda: nums1))
_l_(105645)
_c_(105647, _n_(105646, "print", lambda: print), 'Array2:')
_l_(105648)
_c_(105651, _n_(105649, "print", lambda: print), _n_(105650, "nums2", lambda: nums2))
_l_(105652)
_c_(105654, _n_(105653, "print", lambda: print), '\nMultiply said arrays of same size element-by-element:')
_l_(105655)
_c_(105662, _n_(105656, "print", lambda: print), _c_(105661, _a_(105658, _n_(105657, "np", lambda: np), "multiply"), _n_(105659, "nums1", lambda: nums1), _n_(105660, "nums2", lambda: nums2)))
_l_(105663)