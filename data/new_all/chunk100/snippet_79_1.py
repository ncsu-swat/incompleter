# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80821)

except ImportError:
    pass
a = _c_(80825, _a_(80824, _a_(80823, _n_(80822, "np", lambda: np), "random"), "random"), (10, 2))
_l_(80826)
(x, y) = _c_(80831, _a_(80828, _n_(80827, "np", lambda: np), "atleast_2d"), _n_(80829, "a", lambda: a)[:, 0], _n_(80830, "a", lambda: a)[:, 1])
_l_(80832)
_c_(80835, _n_(80833, "print", lambda: print), _n_(80834, "d", lambda: d))
_l_(80836)