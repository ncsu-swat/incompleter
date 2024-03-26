# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(101145)

except ImportError:
    pass
v = _c_(101148, _a_(101147, _n_(101146, "np", lambda: np), "arange"), 7)
_l_(101149)
result = _c_(101154, _a_(101152, _a_(101151, _n_(101150, "np", lambda: np), "linalg"), "norm"), _n_(101153, "v", lambda: v))
_l_(101155)
_c_(101157, _n_(101156, "print", lambda: print), 'Vector norm:')
_l_(101158)
_c_(101161, _n_(101159, "print", lambda: print), _n_(101160, "result", lambda: result))
_l_(101162)
m = _c_(101165, _a_(101164, _n_(101163, "np", lambda: np), "matrix"), '1, 2; 3, 4')
_l_(101166)
_c_(101168, _n_(101167, "print", lambda: print), 'Matrix norm:')
_l_(101169)
_c_(101172, _n_(101170, "print", lambda: print), _n_(101171, "result1", lambda: result1))
_l_(101173)