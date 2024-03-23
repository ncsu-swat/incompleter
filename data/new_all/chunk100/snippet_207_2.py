# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(16062)

except ImportError:
    pass
x = _c_(16066, _a_(16064, _n_(16063, "np", lambda: np), "array"), _n_(16065, "a", lambda: a))
_l_(16067)
a2 = _c_(16070, _a_(16069, _n_(16068, "x", lambda: x), "tolist"))
_l_(16071)
_c_(16075, _n_(16072, "print", lambda: print), _n_(16073, "a", lambda: a) == _n_(16074, "a2", lambda: a2))
_l_(16076)