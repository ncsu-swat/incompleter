# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51756)

except ImportError:
    pass
a = _c_(51761, _a_(51758, _n_(51757, "np", lambda: np), "array"), [[4, 12, -16], [12, 37, -53], [-16, -53, 98]], dtype=_a_(51760, _n_(51759, "np", lambda: np), "int32"))
_l_(51762)
_c_(51764, _n_(51763, "print", lambda: print), 'Original array:')
_l_(51765)
_c_(51768, _n_(51766, "print", lambda: print), _n_(51767, "a", lambda: a))
_l_(51769)
_c_(51771, _n_(51770, "print", lambda: print), 'Lower-trianglular L in the Cholesky decomposition of the said array:')
_l_(51772)
_c_(51775, _n_(51773, "print", lambda: print), _n_(51774, "L", lambda: L))
_l_(51776)