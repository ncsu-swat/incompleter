# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5949)

except ImportError:
    pass
x = _c_(5952, _a_(5951, _n_(5950, "np", lambda: np), "array"), [72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
_l_(5953)
_c_(5955, _n_(5954, "print", lambda: print), 'Original numbers:')
_l_(5956)
_c_(5959, _n_(5957, "print", lambda: print), _n_(5958, "x", lambda: x))
_l_(5960)
_c_(5963, _n_(5961, "print", lambda: print), _n_(5962, "y", lambda: y))
_l_(5964)
_c_(5966, _n_(5965, "print", lambda: print), 'Comparison - equal:')
_l_(5967)
_c_(5974, _n_(5968, "print", lambda: print), _c_(5973, _a_(5970, _n_(5969, "np", lambda: np), "equal"), _n_(5971, "x", lambda: x), _n_(5972, "y", lambda: y)))
_l_(5975)
_c_(5977, _n_(5976, "print", lambda: print), 'Comparison - equal within a tolerance:')
_l_(5978)
_c_(5985, _n_(5979, "print", lambda: print), _c_(5984, _a_(5981, _n_(5980, "np", lambda: np), "allclose"), _n_(5982, "x", lambda: x), _n_(5983, "y", lambda: y)))
_l_(5986)