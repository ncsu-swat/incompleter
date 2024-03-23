# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(76949)

except ImportError:
    pass
nums1 = _c_(76955, _a_(76952, _a_(76951, _n_(76950, "np", lambda: np), "random"), "randint"), low=0, high=256, size=(200, 300, 3), dtype=_a_(76954, _n_(76953, "np", lambda: np), "uint8"))
_l_(76956)
_c_(76958, _n_(76957, "print", lambda: print), 'Array1:')
_l_(76959)
_c_(76962, _n_(76960, "print", lambda: print), _n_(76961, "nums1", lambda: nums1))
_l_(76963)
_c_(76965, _n_(76964, "print", lambda: print), '\nArray2:')
_l_(76966)
_c_(76969, _n_(76967, "print", lambda: print), _n_(76968, "nums2", lambda: nums2))
_l_(76970)
nums1 = _c_(76974, _a_(76972, _n_(76971, "np", lambda: np), "expand_dims"), _n_(76973, "nums1", lambda: nums1), axis=0)
_l_(76975)
nums2 = _c_(76979, _a_(76977, _n_(76976, "np", lambda: np), "expand_dims"), _n_(76978, "nums2", lambda: nums2), axis=0)
_l_(76980)
nums = _c_(76985, _a_(76982, _n_(76981, "np", lambda: np), "append"), _n_(76983, "nums1", lambda: nums1), _n_(76984, "nums2", lambda: nums2), axis=0)
_l_(76986)
_c_(76988, _n_(76987, "print", lambda: print), '\nCombined array:')
_l_(76989)
_c_(76992, _n_(76990, "print", lambda: print), _n_(76991, "nums", lambda: nums))
_l_(76993)