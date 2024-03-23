# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5765)

except ImportError:
    pass
nums1 = _c_(5768, _a_(5767, _n_(5766, "np", lambda: np), "ones"), (2, 2, 3))
_l_(5769)
_c_(5771, _n_(5770, "print", lambda: print), 'Original array:')
_l_(5772)
_c_(5775, _n_(5773, "print", lambda: print), _n_(5774, "nums1", lambda: nums1))
_l_(5776)
new_array = _n_(5777, "nums1", lambda: nums1) * _n_(5778, "nums2", lambda: nums2)[:, :, None]
_l_(5779)
_c_(5781, _n_(5780, "print", lambda: print), '\nNew array:')
_l_(5782)
_c_(5785, _n_(5783, "print", lambda: print), _n_(5784, "new_array", lambda: new_array))
_l_(5786)