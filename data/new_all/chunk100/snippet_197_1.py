# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(15625)

except ImportError:
    pass
y = _c_(15628, _a_(15627, _n_(15626, "np", lambda: np), "array"), [[1, 2], [1, 2]])
_l_(15629)
_c_(15631, _n_(15630, "print", lambda: print), 'Array1: ')
_l_(15632)
_c_(15635, _n_(15633, "print", lambda: print), _n_(15634, "x", lambda: x))
_l_(15636)
_c_(15638, _n_(15637, "print", lambda: print), 'Array1: ')
_l_(15639)
_c_(15642, _n_(15640, "print", lambda: print), _n_(15641, "y", lambda: y))
_l_(15643)
_c_(15645, _n_(15644, "print", lambda: print), 'Result- x^y:')
_l_(15646)
r1 = _c_(15651, _a_(15648, _n_(15647, "np", lambda: np), "power"), _n_(15649, "x", lambda: x), _n_(15650, "y", lambda: y))
_l_(15652)
_c_(15655, _n_(15653, "print", lambda: print), _n_(15654, "r1", lambda: r1))
_l_(15656)