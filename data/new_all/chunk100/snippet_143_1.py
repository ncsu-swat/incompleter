# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(10034)

except ImportError:
    pass
x = _c_(10037, _a_(10036, _n_(10035, "np", lambda: np), "array"), [[10, 20, 30], [40, 50, 60]])
_l_(10038)
_c_(10045, _n_(10039, "print", lambda: print), _c_(10044, _a_(10041, _n_(10040, "np", lambda: np), "append"), _n_(10042, "x", lambda: x), _n_(10043, "y", lambda: y), axis=1))
_l_(10046)