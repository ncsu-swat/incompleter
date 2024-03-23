# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(55813)

except ImportError:
    pass
nums1 = _c_(55817, _a_(55816, _a_(55815, _n_(55814, "np", lambda: np), "random"), "randint"), 0, 6, (6, 4))
_l_(55818)
nums2 = _c_(55822, _a_(55821, _a_(55820, _n_(55819, "np", lambda: np), "random"), "randint"), 0, 6, (2, 3))
_l_(55823)
_c_(55825, _n_(55824, "print", lambda: print), 'Original arrays:')
_l_(55826)
_c_(55829, _n_(55827, "print", lambda: print), _n_(55828, "nums1", lambda: nums1))
_l_(55830)
_c_(55833, _n_(55831, "print", lambda: print), '\n', _n_(55832, "nums2", lambda: nums2))
_l_(55834)
rows = _c_(55841, _a_(55840, (_c_(55837, _a_(55836, _n_(55835, "temp", lambda: temp), "sum"), axis=(1, 2, 3)) >= _a_(55839, _n_(55838, "nums2", lambda: nums2), "shape")[1]), "nonzero"))[0]
_l_(55842)
_c_(55844, _n_(55843, "print", lambda: print), '\nRows of a given array that contain elements of each row of another given array:')
_l_(55845)
_c_(55848, _n_(55846, "print", lambda: print), _n_(55847, "rows", lambda: rows))
_l_(55849)