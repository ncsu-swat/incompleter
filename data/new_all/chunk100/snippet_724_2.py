# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(73601)

except ImportError:
    pass
a = _c_(73604, _a_(73603, _n_(73602, "np", lambda: np), "array"), [[0, 1, 3], [5, 7, 9]])
_l_(73605)
c = _c_(73610, _a_(73607, _n_(73606, "np", lambda: np), "concatenate"), (_n_(73608, "a", lambda: a), _n_(73609, "b", lambda: b)), 1)
_l_(73611)
_c_(73614, _n_(73612, "print", lambda: print), _n_(73613, "c", lambda: c))
_l_(73615)