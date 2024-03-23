# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5742)

except ImportError:
    pass
nums2 = 3 * _c_(5745, _a_(5744, _n_(5743, "np", lambda: np), "ones"), (2, 2))
_l_(5746)
_c_(5748, _n_(5747, "print", lambda: print), 'Original array:')
_l_(5749)
_c_(5752, _n_(5750, "print", lambda: print), _n_(5751, "nums1", lambda: nums1))
_l_(5753)
new_array = _n_(5754, "nums1", lambda: nums1) * _n_(5755, "nums2", lambda: nums2)[:, :, None]
_l_(5756)
_c_(5758, _n_(5757, "print", lambda: print), '\nNew array:')
_l_(5759)
_c_(5762, _n_(5760, "print", lambda: print), _n_(5761, "new_array", lambda: new_array))
_l_(5763)