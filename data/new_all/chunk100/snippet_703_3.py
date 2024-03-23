# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(72144)

except ImportError:
    pass
n = 4
_l_(72145)
e = 10
_l_(72146)
array_nums1 = _c_(72151, _a_(72148, _n_(72147, "np", lambda: np), "zeros"), (_n_(72149, "n", lambda: n), _n_(72150, "n", lambda: n)))
_l_(72152)
_c_(72154, _n_(72153, "print", lambda: print), 'Original array:')
_l_(72155)
_c_(72158, _n_(72156, "print", lambda: print), _n_(72157, "array_nums1", lambda: array_nums1))
_l_(72159)
_c_(72173, _a_(72161, _n_(72160, "np", lambda: np), "put"), _n_(72162, "array_nums1", lambda: array_nums1), _c_(72171, _a_(72165, _a_(72164, _n_(72163, "np", lambda: np), "random"), "choice"), _c_(72169, _n_(72166, "range", lambda: range), _n_(72167, "n", lambda: n) * _n_(72168, "n", lambda: n)), _n_(72170, "i", lambda: i), replace=False), _n_(72172, "e", lambda: e))
_l_(72174)
_c_(72176, _n_(72175, "print", lambda: print), '\nPlace a specified element in specified time randomly:')
_l_(72177)
_c_(72180, _n_(72178, "print", lambda: print), _n_(72179, "array_nums1", lambda: array_nums1))
_l_(72181)