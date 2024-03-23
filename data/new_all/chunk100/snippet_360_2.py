# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(35648)

except ImportError:
    pass
try:
    import os
    _l_(35650)

except ImportError:
    pass
a = _c_(35653, _a_(35652, _n_(35651, "np", lambda: np), "array"), [1, 2, 3, 4, 5, 6])
_l_(35654)
_c_(35656, _n_(35655, "print", lambda: print), 'Original array:')
_l_(35657)
_c_(35660, _n_(35658, "print", lambda: print), _n_(35659, "a", lambda: a))
_l_(35661)
a2 = _c_(35667, _a_(35663, _n_(35662, "np", lambda: np), "fromstring"), _n_(35664, "a_bytes", lambda: a_bytes), dtype=_a_(35666, _n_(35665, "a", lambda: a), "dtype"))
_l_(35668)
_c_(35670, _n_(35669, "print", lambda: print), 'After loading, content of the text file:')
_l_(35671)
_c_(35674, _n_(35672, "print", lambda: print), _n_(35673, "a2", lambda: a2))
_l_(35675)
_c_(35682, _n_(35676, "print", lambda: print), _c_(35681, _a_(35678, _n_(35677, "np", lambda: np), "array_equal"), _n_(35679, "a", lambda: a), _n_(35680, "a2", lambda: a2)))
_l_(35683)