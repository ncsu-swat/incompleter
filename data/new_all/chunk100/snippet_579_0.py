# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(60180)

except ImportError:
    pass
try:
    from sys import getsizeof
    _l_(60182)

except ImportError:
    pass
y = _c_(60186, _a_(60184, _n_(60183, "np", lambda: np), "array"), _n_(60185, "x", lambda: x))
_l_(60187)
_c_(60192, _n_(60188, "print", lambda: print), _c_(60191, _n_(60189, "getsizeof", lambda: getsizeof), _n_(60190, "x", lambda: x)))
_l_(60193)