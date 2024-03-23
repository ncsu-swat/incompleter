# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51734)

except ImportError:
    pass
_c_(51736, _n_(51735, "print", lambda: print), 'Original array:')
_l_(51737)
_c_(51740, _n_(51738, "print", lambda: print), _n_(51739, "a", lambda: a))
_l_(51741)
L = _c_(51746, _a_(51744, _a_(51743, _n_(51742, "np", lambda: np), "linalg"), "cholesky"), _n_(51745, "a", lambda: a))
_l_(51747)
_c_(51749, _n_(51748, "print", lambda: print), 'Lower-trianglular L in the Cholesky decomposition of the said array:')
_l_(51750)
_c_(51753, _n_(51751, "print", lambda: print), _n_(51752, "L", lambda: L))
_l_(51754)