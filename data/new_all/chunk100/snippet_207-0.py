# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105076)

except ImportError:
    pass
a = [[1, 2], [3, 4]]
_l_(105077)
x = _c_(105081, _a_(105079, _n_(105078, "np", lambda: np), "array"), _n_(105080, "a", lambda: a))
_l_(105082)
_c_(105086, _n_(105083, "print", lambda: print), _n_(105084, "a", lambda: a) == _n_(105085, "a2", lambda: a2))
_l_(105087)