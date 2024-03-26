# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(116100)

except ImportError:
    pass
b = _c_(116103, _a_(116102, _n_(116101, "np", lambda: np), "array"), [[40], [50], [60]])
_l_(116104)
c = _c_(116109, _a_(116106, _n_(116105, "np", lambda: np), "dstack"), (_n_(116107, "a", lambda: a), _n_(116108, "b", lambda: b)))
_l_(116110)
_c_(116113, _n_(116111, "print", lambda: print), _n_(116112, "c", lambda: c))
_l_(116114)