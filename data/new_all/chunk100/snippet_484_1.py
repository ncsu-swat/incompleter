# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(50602)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(50604)

except ImportError:
    pass
nums = _c_(50607, _a_(50606, _n_(50605, "np", lambda: np), "array"), [0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
_l_(50608)
_c_(50611, _n_(50609, "print", lambda: print), 'nums: ', _n_(50610, "nums", lambda: nums))
_l_(50612)
_c_(50615, _n_(50613, "print", lambda: print), 'bins: ', _n_(50614, "bins", lambda: bins))
_l_(50616)
_c_(50623, _n_(50617, "print", lambda: print), 'Result:', _c_(50622, _a_(50619, _n_(50618, "np", lambda: np), "histogram"), _n_(50620, "nums", lambda: nums), _n_(50621, "bins", lambda: bins)))
_l_(50624)
_c_(50629, _a_(50626, _n_(50625, "plt", lambda: plt), "hist"), _n_(50627, "nums", lambda: nums), bins=_n_(50628, "bins", lambda: bins))
_l_(50630)
_c_(50633, _a_(50632, _n_(50631, "plt", lambda: plt), "show"))
_l_(50634)