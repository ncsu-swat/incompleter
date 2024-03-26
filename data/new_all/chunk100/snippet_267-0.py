# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(107698)

except ImportError:
    pass
_c_(107700, _n_(107699, "print", lambda: print), 'Elements of the array in Fortan array:')
_l_(107701)
for x in _c_(107705, _a_(107703, _n_(107702, "np", lambda: np), "nditer"), _n_(107704, "x", lambda: x), order='F'):
    _l_(107710)

    _c_(107708, _n_(107706, "print", lambda: print), _n_(107707, "x", lambda: x), end=' ')
    _l_(107709)
_c_(107712, _n_(107711, "print", lambda: print), '\n')
_l_(107713)