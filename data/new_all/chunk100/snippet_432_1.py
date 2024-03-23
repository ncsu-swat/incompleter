# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(44037)

except ImportError:
    pass
b = _c_(44040, _a_(44039, _n_(44038, "np", lambda: np), "array"), [[40], [50], [60]])
_l_(44041)
c = _c_(44046, _a_(44043, _n_(44042, "np", lambda: np), "dstack"), (_n_(44044, "a", lambda: a), _n_(44045, "b", lambda: b)))
_l_(44047)
_c_(44050, _n_(44048, "print", lambda: print), _n_(44049, "c", lambda: c))
_l_(44051)