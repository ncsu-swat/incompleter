# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(73086)

except ImportError:
    pass
nums = _c_(73089, _a_(73088, _n_(73087, "np", lambda: np), "array"), [[5.54, 3.38, 7.99], [3.54, 4.38, 6.99], [1.54, 2.39, 9.29]])
_l_(73090)
_c_(73092, _n_(73091, "print", lambda: print), 'Original array:')
_l_(73093)
_c_(73096, _n_(73094, "print", lambda: print), _n_(73095, "nums", lambda: nums))
_l_(73097)
_c_(73100, _n_(73098, "print", lambda: print), '\nElements of the said array greater than', _n_(73099, "n", lambda: n))
_l_(73101)
_c_(73106, _n_(73102, "print", lambda: print), _n_(73103, "nums", lambda: nums)[_n_(73104, "nums", lambda: nums) > _n_(73105, "n", lambda: n)])
_l_(73107)
n = 6
_l_(73108)
_c_(73111, _n_(73109, "print", lambda: print), '\nElements of the said array less than', _n_(73110, "n", lambda: n))
_l_(73112)
_c_(73117, _n_(73113, "print", lambda: print), _n_(73114, "nums", lambda: nums)[_n_(73115, "nums", lambda: nums) < _n_(73116, "n", lambda: n)])
_l_(73118)