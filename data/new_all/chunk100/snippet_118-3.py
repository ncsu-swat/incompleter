# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(101205)

except ImportError:
    pass
result = _c_(101210, _a_(101208, _a_(101207, _n_(101206, "np", lambda: np), "linalg"), "norm"), _n_(101209, "v", lambda: v))
_l_(101211)
_c_(101213, _n_(101212, "print", lambda: print), 'Vector norm:')
_l_(101214)
_c_(101217, _n_(101215, "print", lambda: print), _n_(101216, "result", lambda: result))
_l_(101218)
m = _c_(101221, _a_(101220, _n_(101219, "np", lambda: np), "matrix"), '1, 2; 3, 4')
_l_(101222)
result1 = _c_(101227, _a_(101225, _a_(101224, _n_(101223, "np", lambda: np), "linalg"), "norm"), _n_(101226, "m", lambda: m))
_l_(101228)
_c_(101230, _n_(101229, "print", lambda: print), 'Matrix norm:')
_l_(101231)
_c_(101234, _n_(101232, "print", lambda: print), _n_(101233, "result1", lambda: result1))
_l_(101235)