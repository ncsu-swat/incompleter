# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(16049)

except ImportError:
    pass
a = [[1, 2], [3, 4]]
_l_(16050)
x = _c_(16054, _a_(16052, _n_(16051, "np", lambda: np), "array"), _n_(16053, "a", lambda: a))
_l_(16055)
_c_(16059, _n_(16056, "print", lambda: print), _n_(16057, "a", lambda: a) == _n_(16058, "a2", lambda: a2))
_l_(16060)