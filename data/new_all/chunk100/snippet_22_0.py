# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(18180)

except ImportError:
    pass
nums2 = _c_(18183, _a_(18182, _n_(18181, "np", lambda: np), "array"), [[5, 3, 4], [3, 2, 5]])
_l_(18184)
_c_(18186, _n_(18185, "print", lambda: print), 'Array1:')
_l_(18187)
_c_(18190, _n_(18188, "print", lambda: print), _n_(18189, "nums1", lambda: nums1))
_l_(18191)
_c_(18193, _n_(18192, "print", lambda: print), 'Array2:')
_l_(18194)
_c_(18197, _n_(18195, "print", lambda: print), _n_(18196, "nums2", lambda: nums2))
_l_(18198)
_c_(18200, _n_(18199, "print", lambda: print), '\nMultiply said arrays of same size element-by-element:')
_l_(18201)
_c_(18208, _n_(18202, "print", lambda: print), _c_(18207, _a_(18204, _n_(18203, "np", lambda: np), "multiply"), _n_(18205, "nums1", lambda: nums1), _n_(18206, "nums2", lambda: nums2)))
_l_(18209)