# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64664)

except ImportError:
    pass
y = _c_(64667, _a_(64666, _n_(64665, "np", lambda: np), "array"), [2, 4, 5])
_l_(64668)
_c_(64670, _n_(64669, "print", lambda: print), '\nOriginal array1:')
_l_(64671)
_c_(64674, _n_(64672, "print", lambda: print), _n_(64673, "x", lambda: x))
_l_(64675)
_c_(64677, _n_(64676, "print", lambda: print), '\nOriginal array1:')
_l_(64678)
_c_(64681, _n_(64679, "print", lambda: print), _n_(64680, "y", lambda: y))
_l_(64682)
_c_(64689, _n_(64683, "print", lambda: print), '\nPearson product-moment correlation coefficients of the said arrays:\n', _c_(64688, _a_(64685, _n_(64684, "np", lambda: np), "corrcoef"), _n_(64686, "x", lambda: x), _n_(64687, "y", lambda: y)))
_l_(64690)