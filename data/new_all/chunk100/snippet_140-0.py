# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(102197)

except ImportError:
    pass
x = _c_(102200, _a_(102199, _n_(102198, "np", lambda: np), "array"), [0, 1, 3])
_l_(102201)
_c_(102203, _n_(102202, "print", lambda: print), '\nOriginal array1:')
_l_(102204)
_c_(102207, _n_(102205, "print", lambda: print), _n_(102206, "x", lambda: x))
_l_(102208)
_c_(102210, _n_(102209, "print", lambda: print), '\nOriginal array1:')
_l_(102211)
_c_(102214, _n_(102212, "print", lambda: print), _n_(102213, "y", lambda: y))
_l_(102215)
_c_(102222, _n_(102216, "print", lambda: print), '\nCross-correlation of the said arrays:\n', _c_(102221, _a_(102218, _n_(102217, "np", lambda: np), "cov"), _n_(102219, "x", lambda: x), _n_(102220, "y", lambda: y)))
_l_(102223)