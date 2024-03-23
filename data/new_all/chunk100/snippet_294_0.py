# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(25002)

except ImportError:
    pass
n = _n_(25003, "x", lambda: x)[(_n_(25004, "x", lambda: x) % 3 == 0) | (_n_(25005, "x", lambda: x) % 5 == 0)]
_l_(25006)
_c_(25009, _n_(25007, "print", lambda: print), _n_(25008, "n", lambda: n)[:1000])
_l_(25010)
_c_(25015, _n_(25011, "print", lambda: print), _c_(25014, _a_(25013, _n_(25012, "n", lambda: n), "sum")))
_l_(25016)