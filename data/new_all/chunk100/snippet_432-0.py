# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(116084)

except ImportError:
    pass
a = _c_(116087, _a_(116086, _n_(116085, "np", lambda: np), "array"), [[10], [20], [30]])
_l_(116088)
c = _c_(116093, _a_(116090, _n_(116089, "np", lambda: np), "dstack"), (_n_(116091, "a", lambda: a), _n_(116092, "b", lambda: b)))
_l_(116094)
_c_(116097, _n_(116095, "print", lambda: print), _n_(116096, "c", lambda: c))
_l_(116098)