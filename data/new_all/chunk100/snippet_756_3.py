# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(76995)

except ImportError:
    pass
nums1 = _c_(77001, _a_(76998, _a_(76997, _n_(76996, "np", lambda: np), "random"), "randint"), low=0, high=256, size=(200, 300, 3), dtype=_a_(77000, _n_(76999, "np", lambda: np), "uint8"))
_l_(77002)
nums2 = _c_(77008, _a_(77005, _a_(77004, _n_(77003, "np", lambda: np), "random"), "randint"), low=0, high=256, size=(200, 300, 3), dtype=_a_(77007, _n_(77006, "np", lambda: np), "uint8"))
_l_(77009)
_c_(77011, _n_(77010, "print", lambda: print), 'Array1:')
_l_(77012)
_c_(77015, _n_(77013, "print", lambda: print), _n_(77014, "nums1", lambda: nums1))
_l_(77016)
_c_(77018, _n_(77017, "print", lambda: print), '\nArray2:')
_l_(77019)
_c_(77022, _n_(77020, "print", lambda: print), _n_(77021, "nums2", lambda: nums2))
_l_(77023)
nums1 = _c_(77027, _a_(77025, _n_(77024, "np", lambda: np), "expand_dims"), _n_(77026, "nums1", lambda: nums1), axis=0)
_l_(77028)
nums2 = _c_(77032, _a_(77030, _n_(77029, "np", lambda: np), "expand_dims"), _n_(77031, "nums2", lambda: nums2), axis=0)
_l_(77033)
_c_(77035, _n_(77034, "print", lambda: print), '\nCombined array:')
_l_(77036)
_c_(77039, _n_(77037, "print", lambda: print), _n_(77038, "nums", lambda: nums))
_l_(77040)