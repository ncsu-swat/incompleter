# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118768)

except ImportError:
    pass
a = _c_(118773, _a_(118770, _n_(118769, "np", lambda: np), "array"), [[4, 12, -16], [12, 37, -53], [-16, -53, 98]], dtype=_a_(118772, _n_(118771, "np", lambda: np), "int32"))
_l_(118774)
_c_(118776, _n_(118775, "print", lambda: print), 'Original array:')
_l_(118777)
_c_(118780, _n_(118778, "print", lambda: print), _n_(118779, "a", lambda: a))
_l_(118781)
_c_(118783, _n_(118782, "print", lambda: print), 'Lower-trianglular L in the Cholesky decomposition of the said array:')
_l_(118784)
_c_(118787, _n_(118785, "print", lambda: print), _n_(118786, "L", lambda: L))
_l_(118788)