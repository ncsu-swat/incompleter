# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(6100)

except ImportError:
    pass
v = _c_(6103, _a_(6102, _n_(6101, "np", lambda: np), "arange"), 7)
_l_(6104)
result = _c_(6109, _a_(6107, _a_(6106, _n_(6105, "np", lambda: np), "linalg"), "norm"), _n_(6108, "v", lambda: v))
_l_(6110)
_c_(6112, _n_(6111, "print", lambda: print), 'Vector norm:')
_l_(6113)
_c_(6116, _n_(6114, "print", lambda: print), _n_(6115, "result", lambda: result))
_l_(6117)
result1 = _c_(6122, _a_(6120, _a_(6119, _n_(6118, "np", lambda: np), "linalg"), "norm"), _n_(6121, "m", lambda: m))
_l_(6123)
_c_(6125, _n_(6124, "print", lambda: print), 'Matrix norm:')
_l_(6126)
_c_(6129, _n_(6127, "print", lambda: print), _n_(6128, "result1", lambda: result1))
_l_(6130)