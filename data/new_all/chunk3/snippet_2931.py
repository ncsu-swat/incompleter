# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57998473/np-vectorize-for-typeerror-only-size-1-arrays-can-be-converted-to-python-scalar
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(565803)

except ImportError:
    pass
try:
    import math
    _l_(565805)

except ImportError:
    pass


S0 = 50
_l_(565806)

k_list = _c_(565811, _a_(565808, _n_(565807, "np", lambda: np), "linspace"), _n_(565809, "S0", lambda: S0) * 0.6, _n_(565810, "S0", lambda: S0) * 1.4, 50)
_l_(565812)

K=_n_(565813, "k_list", lambda: k_list)
_l_(565814)

d1 = _c_(565822, _a_(565816, _n_(565815, "np", lambda: np), "vectorize"), _c_(565821, _a_(565818, _n_(565817, "math", lambda: math), "log"), _n_(565819, "S0", lambda: S0) / _n_(565820, "K", lambda: K)))
_l_(565823)

_c_(565826, _n_(565824, "print", lambda: print), _n_(565825, "d1", lambda: d1))
_l_(565827)