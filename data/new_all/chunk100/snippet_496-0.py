# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118878)

except ImportError:
    pass
_c_(118880, _n_(118879, "print", lambda: print), 'Original matrix:')
_l_(118881)
_c_(118884, _n_(118882, "print", lambda: print), _n_(118883, "m", lambda: m))
_l_(118885)
result = _c_(118890, _a_(118888, _a_(118887, _n_(118886, "np", lambda: np), "linalg"), "cond"), _n_(118889, "m", lambda: m))
_l_(118891)
_c_(118893, _n_(118892, "print", lambda: print), 'Condition number of the said matrix:')
_l_(118894)
_c_(118897, _n_(118895, "print", lambda: print), _n_(118896, "result", lambda: result))
_l_(118898)