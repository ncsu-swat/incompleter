# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(100840)

except ImportError:
    pass
nums2 = 3 * _c_(100843, _a_(100842, _n_(100841, "np", lambda: np), "ones"), (2, 2))
_l_(100844)
_c_(100846, _n_(100845, "print", lambda: print), 'Original array:')
_l_(100847)
_c_(100850, _n_(100848, "print", lambda: print), _n_(100849, "nums1", lambda: nums1))
_l_(100851)
new_array = _n_(100852, "nums1", lambda: nums1) * _n_(100853, "nums2", lambda: nums2)[:, :, None]
_l_(100854)
_c_(100856, _n_(100855, "print", lambda: print), '\nNew array:')
_l_(100857)
_c_(100860, _n_(100858, "print", lambda: print), _n_(100859, "new_array", lambda: new_array))
_l_(100861)