# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(44053)

except ImportError:
    pass
a = _c_(44056, _a_(44055, _n_(44054, "np", lambda: np), "array"), [[10], [20], [30]])
_l_(44057)
c = _c_(44062, _a_(44059, _n_(44058, "np", lambda: np), "dstack"), (_n_(44060, "a", lambda: a), _n_(44061, "b", lambda: b)))
_l_(44063)
_c_(44066, _n_(44064, "print", lambda: print), _n_(44065, "c", lambda: c))
_l_(44067)