# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(72351)

except ImportError:
    pass
v = _c_(72354, _a_(72353, _n_(72352, "np", lambda: np), "array"), [1, 1, 0])
_l_(72355)
_c_(72357, _n_(72356, "print", lambda: print), 'Original vector:')
_l_(72358)
_c_(72361, _n_(72359, "print", lambda: print), _n_(72360, "v", lambda: v))
_l_(72362)
_c_(72364, _n_(72363, "print", lambda: print), 'Original matrix:')
_l_(72365)
_c_(72368, _n_(72366, "print", lambda: print), _n_(72367, "m", lambda: m))
_l_(72369)
result = _c_(72373, _a_(72371, _n_(72370, "np", lambda: np), "empty_like"), _n_(72372, "m", lambda: m))
_l_(72374)
for i in _c_(72376, _n_(72375, "range", lambda: range), 4):
    _l_(72383)

    _n_(72377, "result", lambda: result)[_n_(72378, "i", lambda: i), :] = _n_(72379, "m", lambda: m)[_n_(72380, "i", lambda: i), :] + _n_(72381, "v", lambda: v)
    _l_(72382)
_c_(72385, _n_(72384, "print", lambda: print), '\nAfter adding the vector v to each row of the matrix m:')
_l_(72386)
_c_(72389, _n_(72387, "print", lambda: print), _n_(72388, "result", lambda: result))
_l_(72390)