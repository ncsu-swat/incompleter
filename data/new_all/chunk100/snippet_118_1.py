# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(6068)

except ImportError:
    pass
result = _c_(6073, _a_(6071, _a_(6070, _n_(6069, "np", lambda: np), "linalg"), "norm"), _n_(6072, "v", lambda: v))
_l_(6074)
_c_(6076, _n_(6075, "print", lambda: print), 'Vector norm:')
_l_(6077)
_c_(6080, _n_(6078, "print", lambda: print), _n_(6079, "result", lambda: result))
_l_(6081)
m = _c_(6084, _a_(6083, _n_(6082, "np", lambda: np), "matrix"), '1, 2; 3, 4')
_l_(6085)
result1 = _c_(6090, _a_(6088, _a_(6087, _n_(6086, "np", lambda: np), "linalg"), "norm"), _n_(6089, "m", lambda: m))
_l_(6091)
_c_(6093, _n_(6092, "print", lambda: print), 'Matrix norm:')
_l_(6094)
_c_(6097, _n_(6095, "print", lambda: print), _n_(6096, "result1", lambda: result1))
_l_(6098)