# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105101)

except ImportError:
    pass
x = _c_(105105, _a_(105103, _n_(105102, "np", lambda: np), "array"), _n_(105104, "a", lambda: a))
_l_(105106)
a2 = _c_(105109, _a_(105108, _n_(105107, "x", lambda: x), "tolist"))
_l_(105110)
_c_(105114, _n_(105111, "print", lambda: print), _n_(105112, "a", lambda: a) == _n_(105113, "a2", lambda: a2))
_l_(105115)