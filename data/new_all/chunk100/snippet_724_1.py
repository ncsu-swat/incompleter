# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(73585)

except ImportError:
    pass
b = _c_(73588, _a_(73587, _n_(73586, "np", lambda: np), "array"), [[0, 2, 4], [6, 8, 10]])
_l_(73589)
c = _c_(73594, _a_(73591, _n_(73590, "np", lambda: np), "concatenate"), (_n_(73592, "a", lambda: a), _n_(73593, "b", lambda: b)), 1)
_l_(73595)
_c_(73598, _n_(73596, "print", lambda: print), _n_(73597, "c", lambda: c))
_l_(73599)