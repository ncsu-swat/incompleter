# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17395)

except ImportError:
    pass
x = _c_(17398, _a_(17397, _n_(17396, "np", lambda: np), "array"), [1, 3, 5, 7, 0])
_l_(17399)
_c_(17401, _n_(17400, "print", lambda: print), 'Original array: ')
_l_(17402)
_c_(17405, _n_(17403, "print", lambda: print), _n_(17404, "x", lambda: x))
_l_(17406)
r1 = _c_(17410, _a_(17408, _n_(17407, "np", lambda: np), "ediff1d"), _n_(17409, "x", lambda: x), to_begin=[0, 0], to_end=[200])
_l_(17411)
assert _c_(17416, _a_(17413, _n_(17412, "np", lambda: np), "array_equiv"), _n_(17414, "r1", lambda: r1), _n_(17415, "r2", lambda: r2))
_l_(17417)
_c_(17419, _n_(17418, "print", lambda: print), 'Difference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:')
_l_(17420)
_c_(17423, _n_(17421, "print", lambda: print), _n_(17422, "r2", lambda: r2))
_l_(17424)