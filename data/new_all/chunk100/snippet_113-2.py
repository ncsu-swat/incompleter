# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(100863)

except ImportError:
    pass
nums1 = _c_(100866, _a_(100865, _n_(100864, "np", lambda: np), "ones"), (2, 2, 3))
_l_(100867)
nums2 = 3 * _c_(100870, _a_(100869, _n_(100868, "np", lambda: np), "ones"), (2, 2))
_l_(100871)
_c_(100873, _n_(100872, "print", lambda: print), 'Original array:')
_l_(100874)
_c_(100877, _n_(100875, "print", lambda: print), _n_(100876, "nums1", lambda: nums1))
_l_(100878)
_c_(100880, _n_(100879, "print", lambda: print), '\nNew array:')
_l_(100881)
_c_(100884, _n_(100882, "print", lambda: print), _n_(100883, "new_array", lambda: new_array))
_l_(100885)