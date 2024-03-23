# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(10020)

except ImportError:
    pass
y = _c_(10023, _a_(10022, _n_(10021, "np", lambda: np), "array"), [[100], [200]])
_l_(10024)
_c_(10031, _n_(10025, "print", lambda: print), _c_(10030, _a_(10027, _n_(10026, "np", lambda: np), "append"), _n_(10028, "x", lambda: x), _n_(10029, "y", lambda: y), axis=1))
_l_(10032)