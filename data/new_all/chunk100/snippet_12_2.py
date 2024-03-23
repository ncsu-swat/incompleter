# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(8689)

except ImportError:
    pass
nums = _c_(8692, _a_(8691, _n_(8690, "np", lambda: np), "array"), [1, 2, 3, 4, 5, 6, 7, 8])
_l_(8693)
_c_(8695, _n_(8694, "print", lambda: print), 'Original array:')
_l_(8696)
_c_(8699, _n_(8697, "print", lambda: print), _n_(8698, "nums", lambda: nums))
_l_(8700)
p = 2
_l_(8701)
_n_(8702, "new_nums", lambda: new_nums)[::_n_(8703, "p", lambda: p) + 1] = _n_(8704, "nums", lambda: nums)
_l_(8705)
_c_(8707, _n_(8706, "print", lambda: print), '\nNew array:')
_l_(8708)
_c_(8711, _n_(8709, "print", lambda: print), _n_(8710, "new_nums", lambda: new_nums))
_l_(8712)