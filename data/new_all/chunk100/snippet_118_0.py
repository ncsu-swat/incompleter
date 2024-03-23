# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(6038)

except ImportError:
    pass
v = _c_(6041, _a_(6040, _n_(6039, "np", lambda: np), "arange"), 7)
_l_(6042)
_c_(6044, _n_(6043, "print", lambda: print), 'Vector norm:')
_l_(6045)
_c_(6048, _n_(6046, "print", lambda: print), _n_(6047, "result", lambda: result))
_l_(6049)
m = _c_(6052, _a_(6051, _n_(6050, "np", lambda: np), "matrix"), '1, 2; 3, 4')
_l_(6053)
result1 = _c_(6058, _a_(6056, _a_(6055, _n_(6054, "np", lambda: np), "linalg"), "norm"), _n_(6057, "m", lambda: m))
_l_(6059)
_c_(6061, _n_(6060, "print", lambda: print), 'Matrix norm:')
_l_(6062)
_c_(6065, _n_(6063, "print", lambda: print), _n_(6064, "result1", lambda: result1))
_l_(6066)