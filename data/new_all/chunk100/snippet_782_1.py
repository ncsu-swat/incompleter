# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(78926)

except ImportError:
    pass
z = _c_(78930, _a_(78929, _a_(78928, _n_(78927, "np", lambda: np), "random"), "random"), (10, 2))
_l_(78931)
(x, y) = (_n_(78932, "z", lambda: z)[:, 0], _n_(78933, "z", lambda: z)[:, 1])
_l_(78934)
r = _c_(78939, _a_(78936, _n_(78935, "np", lambda: np), "sqrt"), _n_(78937, "x", lambda: x) ** 2 + _n_(78938, "y", lambda: y) ** 2)
_l_(78940)
_c_(78943, _n_(78941, "print", lambda: print), _n_(78942, "r", lambda: r))
_l_(78944)
_c_(78947, _n_(78945, "print", lambda: print), _n_(78946, "t", lambda: t))
_l_(78948)