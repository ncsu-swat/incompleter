# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(84599)

except ImportError:
    pass
array_nums1 = _c_(84604, _a_(84603, _c_(84602, _a_(84601, _n_(84600, "np", lambda: np), "arange"), 20), "reshape"), 4, 5)
_l_(84605)
_c_(84607, _n_(84606, "print", lambda: print), 'Original arrays:')
_l_(84608)
_c_(84611, _n_(84609, "print", lambda: print), _n_(84610, "array_nums1", lambda: array_nums1))
_l_(84612)
_c_(84615, _n_(84613, "print", lambda: print), _n_(84614, "array_nums2", lambda: array_nums2))
_l_(84616)
_c_(84618, _n_(84617, "print", lambda: print), '\nAll the nan of array_nums2 replaced by the mean of array_nums1:')
_l_(84619)
_n_(84620, "array_nums2", lambda: array_nums2)[_c_(84624, _a_(84622, _n_(84621, "np", lambda: np), "isnan"), _n_(84623, "array_nums2", lambda: array_nums2))] = _c_(84628, _a_(84626, _n_(84625, "np", lambda: np), "nanmean"), _n_(84627, "array_nums1", lambda: array_nums1))
_l_(84629)
_c_(84632, _n_(84630, "print", lambda: print), _n_(84631, "array_nums2", lambda: array_nums2))
_l_(84633)