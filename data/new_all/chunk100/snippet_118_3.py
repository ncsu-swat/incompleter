# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(6132)

except ImportError:
    pass
v = _c_(6135, _a_(6134, _n_(6133, "np", lambda: np), "arange"), 7)
_l_(6136)
result = _c_(6141, _a_(6139, _a_(6138, _n_(6137, "np", lambda: np), "linalg"), "norm"), _n_(6140, "v", lambda: v))
_l_(6142)
_c_(6144, _n_(6143, "print", lambda: print), 'Vector norm:')
_l_(6145)
_c_(6148, _n_(6146, "print", lambda: print), _n_(6147, "result", lambda: result))
_l_(6149)
m = _c_(6152, _a_(6151, _n_(6150, "np", lambda: np), "matrix"), '1, 2; 3, 4')
_l_(6153)
_c_(6155, _n_(6154, "print", lambda: print), 'Matrix norm:')
_l_(6156)
_c_(6159, _n_(6157, "print", lambda: print), _n_(6158, "result1", lambda: result1))
_l_(6160)