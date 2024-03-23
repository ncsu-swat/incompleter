# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(72066)

except ImportError:
    pass
i = 3
_l_(72067)
e = 10
_l_(72068)
array_nums1 = _c_(72073, _a_(72070, _n_(72069, "np", lambda: np), "zeros"), (_n_(72071, "n", lambda: n), _n_(72072, "n", lambda: n)))
_l_(72074)
_c_(72076, _n_(72075, "print", lambda: print), 'Original array:')
_l_(72077)
_c_(72080, _n_(72078, "print", lambda: print), _n_(72079, "array_nums1", lambda: array_nums1))
_l_(72081)
_c_(72095, _a_(72083, _n_(72082, "np", lambda: np), "put"), _n_(72084, "array_nums1", lambda: array_nums1), _c_(72093, _a_(72087, _a_(72086, _n_(72085, "np", lambda: np), "random"), "choice"), _c_(72091, _n_(72088, "range", lambda: range), _n_(72089, "n", lambda: n) * _n_(72090, "n", lambda: n)), _n_(72092, "i", lambda: i), replace=False), _n_(72094, "e", lambda: e))
_l_(72096)
_c_(72098, _n_(72097, "print", lambda: print), '\nPlace a specified element in specified time randomly:')
_l_(72099)
_c_(72102, _n_(72100, "print", lambda: print), _n_(72101, "array_nums1", lambda: array_nums1))
_l_(72103)