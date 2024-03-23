# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64692)

except ImportError:
    pass
x = _c_(64695, _a_(64694, _n_(64693, "np", lambda: np), "array"), [0, 1, 3])
_l_(64696)
_c_(64698, _n_(64697, "print", lambda: print), '\nOriginal array1:')
_l_(64699)
_c_(64702, _n_(64700, "print", lambda: print), _n_(64701, "x", lambda: x))
_l_(64703)
_c_(64705, _n_(64704, "print", lambda: print), '\nOriginal array1:')
_l_(64706)
_c_(64709, _n_(64707, "print", lambda: print), _n_(64708, "y", lambda: y))
_l_(64710)
_c_(64717, _n_(64711, "print", lambda: print), '\nPearson product-moment correlation coefficients of the said arrays:\n', _c_(64716, _a_(64713, _n_(64712, "np", lambda: np), "corrcoef"), _n_(64714, "x", lambda: x), _n_(64715, "y", lambda: y)))
_l_(64718)