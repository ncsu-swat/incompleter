# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106788)

except ImportError:
    pass
x = _c_(106791, _a_(106790, _n_(106789, "np", lambda: np), "arange"), 10)
_l_(106792)
_c_(106794, _n_(106793, "print", lambda: print), 'Original array:')
_l_(106795)
_c_(106798, _n_(106796, "print", lambda: print), _n_(106797, "x", lambda: x))
_l_(106799)
_c_(106804, _a_(106802, _a_(106801, _n_(106800, "np", lambda: np), "random"), "shuffle"), _n_(106803, "x", lambda: x))
_l_(106805)
_c_(106813, _n_(106806, "print", lambda: print), _n_(106807, "x", lambda: x)[_c_(106811, _a_(106809, _n_(106808, "np", lambda: np), "argsort"), _n_(106810, "x", lambda: x))[-_n_(106812, "n", lambda: n):]])
_l_(106814)