# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(87544)

except ImportError:
    pass
_c_(87546, _n_(87545, "print", lambda: print), 'Original array: ')
_l_(87547)
_c_(87550, _n_(87548, "print", lambda: print), _n_(87549, "x", lambda: x))
_l_(87551)
r1 = _c_(87555, _a_(87553, _n_(87552, "np", lambda: np), "reciprocal"), _n_(87554, "x", lambda: x))
_l_(87556)
r2 = 1 / _n_(87557, "x", lambda: x)
_l_(87558)
assert _c_(87563, _a_(87560, _n_(87559, "np", lambda: np), "array_equal"), _n_(87561, "r1", lambda: r1), _n_(87562, "r2", lambda: r2))
_l_(87564)
_c_(87566, _n_(87565, "print", lambda: print), 'Reciprocal for all elements of the said array:')
_l_(87567)
_c_(87570, _n_(87568, "print", lambda: print), _n_(87569, "r1", lambda: r1))
_l_(87571)