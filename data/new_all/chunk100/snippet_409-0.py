# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114815)

except ImportError:
    pass
nums2 = _c_(114818, _a_(114817, _n_(114816, "pd", lambda: pd), "Series"), [1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
_l_(114819)
_c_(114821, _n_(114820, "print", lambda: print), 'Original Series:')
_l_(114822)
_c_(114825, _n_(114823, "print", lambda: print), _n_(114824, "nums1", lambda: nums1))
_l_(114826)
_c_(114829, _n_(114827, "print", lambda: print), _n_(114828, "nums2", lambda: nums2))
_l_(114830)
_c_(114832, _n_(114831, "print", lambda: print), 'Check 2 series are equal or not?')
_l_(114833)
_c_(114837, _n_(114834, "print", lambda: print), _n_(114835, "nums1", lambda: nums1) == _n_(114836, "nums2", lambda: nums2))
_l_(114838)