# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(100887)

except ImportError:
    pass
nums = _c_(100890, _a_(100889, _n_(100888, "np", lambda: np), "array"), [[[1, 2, 3, 4], [0, 1, 3, 4], [90, 91, 93, 94], [5, 0, 3, 2]]])
_l_(100891)
_c_(100893, _n_(100892, "print", lambda: print), 'Original array:')
_l_(100894)
_c_(100897, _n_(100895, "print", lambda: print), _n_(100896, "nums", lambda: nums))
_l_(100898)
_c_(100900, _n_(100899, "print", lambda: print), '\nSwap rows and columns of the said array in reverse order:')
_l_(100901)
_c_(100904, _n_(100902, "print", lambda: print), _n_(100903, "new_nums", lambda: new_nums))
_l_(100905)