# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(57850)

except ImportError:
    pass
try:
    import numpy as np
    _l_(57852)

except ImportError:
    pass
x = _c_(57855, _a_(57854, _n_(57853, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
_l_(57856)
_c_(57858, _n_(57857, "print", lambda: print), 'Original series:')
_l_(57859)
_c_(57862, _n_(57860, "print", lambda: print), _n_(57861, "x", lambda: x))
_l_(57863)
_c_(57866, _n_(57864, "print", lambda: print), _n_(57865, "y", lambda: y))
_l_(57867)
_c_(57869, _n_(57868, "print", lambda: print), '\nEuclidean distance between two said series:')
_l_(57870)
_c_(57878, _n_(57871, "print", lambda: print), _c_(57877, _a_(57874, _a_(57873, _n_(57872, "np", lambda: np), "linalg"), "norm"), _n_(57875, "x", lambda: x) - _n_(57876, "y", lambda: y)))
_l_(57879)