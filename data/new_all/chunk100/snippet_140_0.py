# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(9803)

except ImportError:
    pass
y = _c_(9806, _a_(9805, _n_(9804, "np", lambda: np), "array"), [2, 4, 5])
_l_(9807)
_c_(9809, _n_(9808, "print", lambda: print), '\nOriginal array1:')
_l_(9810)
_c_(9813, _n_(9811, "print", lambda: print), _n_(9812, "x", lambda: x))
_l_(9814)
_c_(9816, _n_(9815, "print", lambda: print), '\nOriginal array1:')
_l_(9817)
_c_(9820, _n_(9818, "print", lambda: print), _n_(9819, "y", lambda: y))
_l_(9821)
_c_(9828, _n_(9822, "print", lambda: print), '\nCross-correlation of the said arrays:\n', _c_(9827, _a_(9824, _n_(9823, "np", lambda: np), "cov"), _n_(9825, "x", lambda: x), _n_(9826, "y", lambda: y)))
_l_(9829)