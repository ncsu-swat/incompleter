# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(78222)

except ImportError:
    pass
_c_(78224, _n_(78223, "print", lambda: print), 'Original array elements:')
_l_(78225)
_c_(78228, _n_(78226, "print", lambda: print), _n_(78227, "x", lambda: x))
_l_(78229)
_c_(78231, _n_(78230, "print", lambda: print), 'Print array values with precision 3:')
_l_(78232)
_c_(78235, _a_(78234, _n_(78233, "np", lambda: np), "set_printoptions"), precision=3)
_l_(78236)
_c_(78239, _n_(78237, "print", lambda: print), _n_(78238, "x", lambda: x))
_l_(78240)