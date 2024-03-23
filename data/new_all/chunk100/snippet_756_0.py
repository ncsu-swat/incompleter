# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(76855)

except ImportError:
    pass
nums2 = _c_(76861, _a_(76858, _a_(76857, _n_(76856, "np", lambda: np), "random"), "randint"), low=0, high=256, size=(200, 300, 3), dtype=_a_(76860, _n_(76859, "np", lambda: np), "uint8"))
_l_(76862)
_c_(76864, _n_(76863, "print", lambda: print), 'Array1:')
_l_(76865)
_c_(76868, _n_(76866, "print", lambda: print), _n_(76867, "nums1", lambda: nums1))
_l_(76869)
_c_(76871, _n_(76870, "print", lambda: print), '\nArray2:')
_l_(76872)
_c_(76875, _n_(76873, "print", lambda: print), _n_(76874, "nums2", lambda: nums2))
_l_(76876)
nums1 = _c_(76880, _a_(76878, _n_(76877, "np", lambda: np), "expand_dims"), _n_(76879, "nums1", lambda: nums1), axis=0)
_l_(76881)
nums2 = _c_(76885, _a_(76883, _n_(76882, "np", lambda: np), "expand_dims"), _n_(76884, "nums2", lambda: nums2), axis=0)
_l_(76886)
nums = _c_(76891, _a_(76888, _n_(76887, "np", lambda: np), "append"), _n_(76889, "nums1", lambda: nums1), _n_(76890, "nums2", lambda: nums2), axis=0)
_l_(76892)
_c_(76894, _n_(76893, "print", lambda: print), '\nCombined array:')
_l_(76895)
_c_(76898, _n_(76896, "print", lambda: print), _n_(76897, "nums", lambda: nums))
_l_(76899)