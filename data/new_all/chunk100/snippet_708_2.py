# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(72392)

except ImportError:
    pass
m = _c_(72395, _a_(72394, _n_(72393, "np", lambda: np), "array"), [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
_l_(72396)
v = _c_(72399, _a_(72398, _n_(72397, "np", lambda: np), "array"), [1, 1, 0])
_l_(72400)
_c_(72402, _n_(72401, "print", lambda: print), 'Original vector:')
_l_(72403)
_c_(72406, _n_(72404, "print", lambda: print), _n_(72405, "v", lambda: v))
_l_(72407)
_c_(72409, _n_(72408, "print", lambda: print), 'Original matrix:')
_l_(72410)
_c_(72413, _n_(72411, "print", lambda: print), _n_(72412, "m", lambda: m))
_l_(72414)
for i in _c_(72416, _n_(72415, "range", lambda: range), 4):
    _l_(72423)

    _n_(72417, "result", lambda: result)[_n_(72418, "i", lambda: i), :] = _n_(72419, "m", lambda: m)[_n_(72420, "i", lambda: i), :] + _n_(72421, "v", lambda: v)
    _l_(72422)
_c_(72425, _n_(72424, "print", lambda: print), '\nAfter adding the vector v to each row of the matrix m:')
_l_(72426)
_c_(72429, _n_(72427, "print", lambda: print), _n_(72428, "result", lambda: result))
_l_(72430)