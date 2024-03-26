# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(100817)

except ImportError:
    pass
nums1 = _c_(100820, _a_(100819, _n_(100818, "np", lambda: np), "ones"), (2, 2, 3))
_l_(100821)
_c_(100823, _n_(100822, "print", lambda: print), 'Original array:')
_l_(100824)
_c_(100827, _n_(100825, "print", lambda: print), _n_(100826, "nums1", lambda: nums1))
_l_(100828)
new_array = _n_(100829, "nums1", lambda: nums1) * _n_(100830, "nums2", lambda: nums2)[:, :, None]
_l_(100831)
_c_(100833, _n_(100832, "print", lambda: print), '\nNew array:')
_l_(100834)
_c_(100837, _n_(100835, "print", lambda: print), _n_(100836, "new_array", lambda: new_array))
_l_(100838)