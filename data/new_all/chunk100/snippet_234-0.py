# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106175)

except ImportError:
    pass
x = _c_(106178, _a_(106177, _n_(106176, "np", lambda: np), "zeros"), (3,), dtype='i4,f4,a40')
_l_(106179)
_n_(106180, "x", lambda: x)[:] = _n_(106181, "new_data", lambda: new_data)
_l_(106182)
_c_(106185, _n_(106183, "print", lambda: print), _n_(106184, "x", lambda: x))
_l_(106186)