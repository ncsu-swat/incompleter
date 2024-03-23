# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(72310)

except ImportError:
    pass
m = _c_(72313, _a_(72312, _n_(72311, "np", lambda: np), "array"), [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
_l_(72314)
_c_(72316, _n_(72315, "print", lambda: print), 'Original vector:')
_l_(72317)
_c_(72320, _n_(72318, "print", lambda: print), _n_(72319, "v", lambda: v))
_l_(72321)
_c_(72323, _n_(72322, "print", lambda: print), 'Original matrix:')
_l_(72324)
_c_(72327, _n_(72325, "print", lambda: print), _n_(72326, "m", lambda: m))
_l_(72328)
result = _c_(72332, _a_(72330, _n_(72329, "np", lambda: np), "empty_like"), _n_(72331, "m", lambda: m))
_l_(72333)
for i in _c_(72335, _n_(72334, "range", lambda: range), 4):
    _l_(72342)

    _n_(72336, "result", lambda: result)[_n_(72337, "i", lambda: i), :] = _n_(72338, "m", lambda: m)[_n_(72339, "i", lambda: i), :] + _n_(72340, "v", lambda: v)
    _l_(72341)
_c_(72344, _n_(72343, "print", lambda: print), '\nAfter adding the vector v to each row of the matrix m:')
_l_(72345)
_c_(72348, _n_(72346, "print", lambda: print), _n_(72347, "result", lambda: result))
_l_(72349)