# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105089)

except ImportError:
    pass
a = [[1, 2], [3, 4]]
_l_(105090)
a2 = _c_(105093, _a_(105092, _n_(105091, "x", lambda: x), "tolist"))
_l_(105094)
_c_(105098, _n_(105095, "print", lambda: print), _n_(105096, "a", lambda: a) == _n_(105097, "a2", lambda: a2))
_l_(105099)