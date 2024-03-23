# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5832)

except ImportError:
    pass
nums = _c_(5835, _a_(5834, _n_(5833, "np", lambda: np), "array"), [[[1, 2, 3, 4], [0, 1, 3, 4], [90, 91, 93, 94], [5, 0, 3, 2]]])
_l_(5836)
_c_(5838, _n_(5837, "print", lambda: print), 'Original array:')
_l_(5839)
_c_(5842, _n_(5840, "print", lambda: print), _n_(5841, "nums", lambda: nums))
_l_(5843)
_c_(5845, _n_(5844, "print", lambda: print), '\nSwap rows and columns of the said array in reverse order:')
_l_(5846)
_c_(5849, _n_(5847, "print", lambda: print), _n_(5848, "new_nums", lambda: new_nums))
_l_(5850)