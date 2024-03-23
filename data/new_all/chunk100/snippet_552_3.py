# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(55891)

except ImportError:
    pass
nums1 = _c_(55895, _a_(55894, _a_(55893, _n_(55892, "np", lambda: np), "random"), "randint"), 0, 6, (6, 4))
_l_(55896)
nums2 = _c_(55900, _a_(55899, _a_(55898, _n_(55897, "np", lambda: np), "random"), "randint"), 0, 6, (2, 3))
_l_(55901)
_c_(55903, _n_(55902, "print", lambda: print), 'Original arrays:')
_l_(55904)
_c_(55907, _n_(55905, "print", lambda: print), _n_(55906, "nums1", lambda: nums1))
_l_(55908)
_c_(55911, _n_(55909, "print", lambda: print), '\n', _n_(55910, "nums2", lambda: nums2))
_l_(55912)
temp = _n_(55913, "nums1", lambda: nums1)[..., _a_(55915, _n_(55914, "np", lambda: np), "newaxis"), _a_(55917, _n_(55916, "np", lambda: np), "newaxis")] == _n_(55918, "nums2", lambda: nums2)
_l_(55919)
_c_(55921, _n_(55920, "print", lambda: print), '\nRows of a given array that contain elements of each row of another given array:')
_l_(55922)
_c_(55925, _n_(55923, "print", lambda: print), _n_(55924, "rows", lambda: rows))
_l_(55926)