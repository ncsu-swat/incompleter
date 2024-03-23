# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(77042)

except ImportError:
    pass
nums1 = _c_(77048, _a_(77045, _a_(77044, _n_(77043, "np", lambda: np), "random"), "randint"), low=0, high=256, size=(200, 300, 3), dtype=_a_(77047, _n_(77046, "np", lambda: np), "uint8"))
_l_(77049)
nums2 = _c_(77055, _a_(77052, _a_(77051, _n_(77050, "np", lambda: np), "random"), "randint"), low=0, high=256, size=(200, 300, 3), dtype=_a_(77054, _n_(77053, "np", lambda: np), "uint8"))
_l_(77056)
_c_(77058, _n_(77057, "print", lambda: print), 'Array1:')
_l_(77059)
_c_(77062, _n_(77060, "print", lambda: print), _n_(77061, "nums1", lambda: nums1))
_l_(77063)
_c_(77065, _n_(77064, "print", lambda: print), '\nArray2:')
_l_(77066)
_c_(77069, _n_(77067, "print", lambda: print), _n_(77068, "nums2", lambda: nums2))
_l_(77070)
nums2 = _c_(77074, _a_(77072, _n_(77071, "np", lambda: np), "expand_dims"), _n_(77073, "nums2", lambda: nums2), axis=0)
_l_(77075)
nums = _c_(77080, _a_(77077, _n_(77076, "np", lambda: np), "append"), _n_(77078, "nums1", lambda: nums1), _n_(77079, "nums2", lambda: nums2), axis=0)
_l_(77081)
_c_(77083, _n_(77082, "print", lambda: print), '\nCombined array:')
_l_(77084)
_c_(77087, _n_(77085, "print", lambda: print), _n_(77086, "nums", lambda: nums))
_l_(77088)