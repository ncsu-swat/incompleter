# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82929)

except ImportError:
    pass
nums1 = _c_(82932, _a_(82931, _n_(82930, "np", lambda: np), "array"), [[4.5, 3.5], [5.1, 2.3]])
_l_(82933)
_c_(82935, _n_(82934, "print", lambda: print), 'Original arrays:')
_l_(82936)
_c_(82939, _n_(82937, "print", lambda: print), _n_(82938, "nums1", lambda: nums1))
_l_(82940)
_c_(82943, _n_(82941, "print", lambda: print), _n_(82942, "nums2", lambda: nums2))
_l_(82944)
_c_(82946, _n_(82945, "print", lambda: print), '\nConcatenating the said two arrays:')
_l_(82947)
_c_(82954, _n_(82948, "print", lambda: print), _c_(82953, _a_(82950, _n_(82949, "np", lambda: np), "concatenate"), (_n_(82951, "nums1", lambda: nums1), _n_(82952, "nums2", lambda: nums2)), axis=1))
_l_(82955)