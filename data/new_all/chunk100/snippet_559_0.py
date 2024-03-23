# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(57819)

except ImportError:
    pass
try:
    import numpy as np
    _l_(57821)

except ImportError:
    pass
y = _c_(57824, _a_(57823, _n_(57822, "pd", lambda: pd), "Series"), [11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
_l_(57825)
_c_(57827, _n_(57826, "print", lambda: print), 'Original series:')
_l_(57828)
_c_(57831, _n_(57829, "print", lambda: print), _n_(57830, "x", lambda: x))
_l_(57832)
_c_(57835, _n_(57833, "print", lambda: print), _n_(57834, "y", lambda: y))
_l_(57836)
_c_(57838, _n_(57837, "print", lambda: print), '\nEuclidean distance between two said series:')
_l_(57839)
_c_(57847, _n_(57840, "print", lambda: print), _c_(57846, _a_(57843, _a_(57842, _n_(57841, "np", lambda: np), "linalg"), "norm"), _n_(57844, "x", lambda: x) - _n_(57845, "y", lambda: y)))
_l_(57848)