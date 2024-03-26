# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106816)

except ImportError:
    pass
_c_(106818, _n_(106817, "print", lambda: print), 'Original array:')
_l_(106819)
_c_(106822, _n_(106820, "print", lambda: print), _n_(106821, "x", lambda: x))
_l_(106823)
_c_(106828, _a_(106826, _a_(106825, _n_(106824, "np", lambda: np), "random"), "shuffle"), _n_(106827, "x", lambda: x))
_l_(106829)
n = 1
_l_(106830)
_c_(106838, _n_(106831, "print", lambda: print), _n_(106832, "x", lambda: x)[_c_(106836, _a_(106834, _n_(106833, "np", lambda: np), "argsort"), _n_(106835, "x", lambda: x))[-_n_(106837, "n", lambda: n):]])
_l_(106839)