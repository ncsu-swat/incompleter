# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114840)

except ImportError:
    pass
nums1 = _c_(114843, _a_(114842, _n_(114841, "pd", lambda: pd), "Series"), [1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
_l_(114844)
_c_(114846, _n_(114845, "print", lambda: print), 'Original Series:')
_l_(114847)
_c_(114850, _n_(114848, "print", lambda: print), _n_(114849, "nums1", lambda: nums1))
_l_(114851)
_c_(114854, _n_(114852, "print", lambda: print), _n_(114853, "nums2", lambda: nums2))
_l_(114855)
_c_(114857, _n_(114856, "print", lambda: print), 'Check 2 series are equal or not?')
_l_(114858)
_c_(114862, _n_(114859, "print", lambda: print), _n_(114860, "nums1", lambda: nums1) == _n_(114861, "nums2", lambda: nums2))
_l_(114863)