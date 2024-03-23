# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(73052)

except ImportError:
    pass
nums = _c_(73055, _a_(73054, _n_(73053, "np", lambda: np), "array"), [[5.54, 3.38, 7.99], [3.54, 4.38, 6.99], [1.54, 2.39, 9.29]])
_l_(73056)
_c_(73058, _n_(73057, "print", lambda: print), 'Original array:')
_l_(73059)
_c_(73062, _n_(73060, "print", lambda: print), _n_(73061, "nums", lambda: nums))
_l_(73063)
n = 5
_l_(73064)
_c_(73067, _n_(73065, "print", lambda: print), '\nElements of the said array greater than', _n_(73066, "n", lambda: n))
_l_(73068)
_c_(73073, _n_(73069, "print", lambda: print), _n_(73070, "nums", lambda: nums)[_n_(73071, "nums", lambda: nums) > _n_(73072, "n", lambda: n)])
_l_(73074)
_c_(73077, _n_(73075, "print", lambda: print), '\nElements of the said array less than', _n_(73076, "n", lambda: n))
_l_(73078)
_c_(73083, _n_(73079, "print", lambda: print), _n_(73080, "nums", lambda: nums)[_n_(73081, "nums", lambda: nums) < _n_(73082, "n", lambda: n)])
_l_(73084)