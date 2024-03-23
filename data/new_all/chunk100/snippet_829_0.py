# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82901)

except ImportError:
    pass
nums2 = _c_(82904, _a_(82903, _n_(82902, "np", lambda: np), "array"), [[1], [2]])
_l_(82905)
_c_(82907, _n_(82906, "print", lambda: print), 'Original arrays:')
_l_(82908)
_c_(82911, _n_(82909, "print", lambda: print), _n_(82910, "nums1", lambda: nums1))
_l_(82912)
_c_(82915, _n_(82913, "print", lambda: print), _n_(82914, "nums2", lambda: nums2))
_l_(82916)
_c_(82918, _n_(82917, "print", lambda: print), '\nConcatenating the said two arrays:')
_l_(82919)
_c_(82926, _n_(82920, "print", lambda: print), _c_(82925, _a_(82922, _n_(82921, "np", lambda: np), "concatenate"), (_n_(82923, "nums1", lambda: nums1), _n_(82924, "nums2", lambda: nums2)), axis=1))
_l_(82927)