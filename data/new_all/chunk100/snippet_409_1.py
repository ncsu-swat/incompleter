# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(40070)

except ImportError:
    pass
nums1 = _c_(40073, _a_(40072, _n_(40071, "pd", lambda: pd), "Series"), [1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
_l_(40074)
_c_(40076, _n_(40075, "print", lambda: print), 'Original Series:')
_l_(40077)
_c_(40080, _n_(40078, "print", lambda: print), _n_(40079, "nums1", lambda: nums1))
_l_(40081)
_c_(40084, _n_(40082, "print", lambda: print), _n_(40083, "nums2", lambda: nums2))
_l_(40085)
_c_(40087, _n_(40086, "print", lambda: print), 'Check 2 series are equal or not?')
_l_(40088)
_c_(40092, _n_(40089, "print", lambda: print), _n_(40090, "nums1", lambda: nums1) == _n_(40091, "nums2", lambda: nums2))
_l_(40093)