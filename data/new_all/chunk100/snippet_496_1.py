# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51927)

except ImportError:
    pass
m = _c_(51930, _a_(51929, _n_(51928, "np", lambda: np), "array"), [[1, 2], [3, 4]])
_l_(51931)
_c_(51933, _n_(51932, "print", lambda: print), 'Original matrix:')
_l_(51934)
_c_(51937, _n_(51935, "print", lambda: print), _n_(51936, "m", lambda: m))
_l_(51938)
_c_(51940, _n_(51939, "print", lambda: print), 'Condition number of the said matrix:')
_l_(51941)
_c_(51944, _n_(51942, "print", lambda: print), _n_(51943, "result", lambda: result))
_l_(51945)