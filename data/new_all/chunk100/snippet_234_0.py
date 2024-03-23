# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(18601)

except ImportError:
    pass
x = _c_(18604, _a_(18603, _n_(18602, "np", lambda: np), "zeros"), (3,), dtype='i4,f4,a40')
_l_(18605)
_n_(18606, "x", lambda: x)[:] = _n_(18607, "new_data", lambda: new_data)
_l_(18608)
_c_(18611, _n_(18609, "print", lambda: print), _n_(18610, "x", lambda: x))
_l_(18612)