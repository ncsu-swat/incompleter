# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105665)

except ImportError:
    pass
nums2 = _c_(105668, _a_(105667, _n_(105666, "np", lambda: np), "array"), [[5, 3, 4], [3, 2, 5]])
_l_(105669)
_c_(105671, _n_(105670, "print", lambda: print), 'Array1:')
_l_(105672)
_c_(105675, _n_(105673, "print", lambda: print), _n_(105674, "nums1", lambda: nums1))
_l_(105676)
_c_(105678, _n_(105677, "print", lambda: print), 'Array2:')
_l_(105679)
_c_(105682, _n_(105680, "print", lambda: print), _n_(105681, "nums2", lambda: nums2))
_l_(105683)
_c_(105685, _n_(105684, "print", lambda: print), '\nMultiply said arrays of same size element-by-element:')
_l_(105686)
_c_(105693, _n_(105687, "print", lambda: print), _c_(105692, _a_(105689, _n_(105688, "np", lambda: np), "multiply"), _n_(105690, "nums1", lambda: nums1), _n_(105691, "nums2", lambda: nums2)))
_l_(105694)