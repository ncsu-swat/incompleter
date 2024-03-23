# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(72105)

except ImportError:
    pass
n = 4
_l_(72106)
i = 3
_l_(72107)
array_nums1 = _c_(72112, _a_(72109, _n_(72108, "np", lambda: np), "zeros"), (_n_(72110, "n", lambda: n), _n_(72111, "n", lambda: n)))
_l_(72113)
_c_(72115, _n_(72114, "print", lambda: print), 'Original array:')
_l_(72116)
_c_(72119, _n_(72117, "print", lambda: print), _n_(72118, "array_nums1", lambda: array_nums1))
_l_(72120)
_c_(72134, _a_(72122, _n_(72121, "np", lambda: np), "put"), _n_(72123, "array_nums1", lambda: array_nums1), _c_(72132, _a_(72126, _a_(72125, _n_(72124, "np", lambda: np), "random"), "choice"), _c_(72130, _n_(72127, "range", lambda: range), _n_(72128, "n", lambda: n) * _n_(72129, "n", lambda: n)), _n_(72131, "i", lambda: i), replace=False), _n_(72133, "e", lambda: e))
_l_(72135)
_c_(72137, _n_(72136, "print", lambda: print), '\nPlace a specified element in specified time randomly:')
_l_(72138)
_c_(72141, _n_(72139, "print", lambda: print), _n_(72140, "array_nums1", lambda: array_nums1))
_l_(72142)