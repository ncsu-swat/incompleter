# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(40045)

except ImportError:
    pass
nums2 = _c_(40048, _a_(40047, _n_(40046, "pd", lambda: pd), "Series"), [1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
_l_(40049)
_c_(40051, _n_(40050, "print", lambda: print), 'Original Series:')
_l_(40052)
_c_(40055, _n_(40053, "print", lambda: print), _n_(40054, "nums1", lambda: nums1))
_l_(40056)
_c_(40059, _n_(40057, "print", lambda: print), _n_(40058, "nums2", lambda: nums2))
_l_(40060)
_c_(40062, _n_(40061, "print", lambda: print), 'Check 2 series are equal or not?')
_l_(40063)
_c_(40067, _n_(40064, "print", lambda: print), _n_(40065, "nums1", lambda: nums1) == _n_(40066, "nums2", lambda: nums2))
_l_(40068)