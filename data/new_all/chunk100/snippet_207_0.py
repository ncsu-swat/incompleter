# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(16037)

except ImportError:
    pass
a = [[1, 2], [3, 4]]
_l_(16038)
a2 = _c_(16041, _a_(16040, _n_(16039, "x", lambda: x), "tolist"))
_l_(16042)
_c_(16046, _n_(16043, "print", lambda: print), _n_(16044, "a", lambda: a) == _n_(16045, "a2", lambda: a2))
_l_(16047)