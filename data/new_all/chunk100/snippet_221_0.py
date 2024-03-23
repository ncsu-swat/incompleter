# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17320)

except ImportError:
    pass
x = _c_(17323, _a_(17322, _n_(17321, "np", lambda: np), "array"), [1, 3, 5, 7, 0])
_l_(17324)
_c_(17326, _n_(17325, "print", lambda: print), 'Original array: ')
_l_(17327)
_c_(17330, _n_(17328, "print", lambda: print), _n_(17329, "x", lambda: x))
_l_(17331)
r2 = _c_(17341, _a_(17333, _n_(17332, "np", lambda: np), "insert"), _c_(17340, _a_(17335, _n_(17334, "np", lambda: np), "append"), _c_(17339, _a_(17337, _n_(17336, "np", lambda: np), "diff"), _n_(17338, "x", lambda: x)), 200), 0, [0, 0])
_l_(17342)
assert _c_(17347, _a_(17344, _n_(17343, "np", lambda: np), "array_equiv"), _n_(17345, "r1", lambda: r1), _n_(17346, "r2", lambda: r2))
_l_(17348)
_c_(17350, _n_(17349, "print", lambda: print), 'Difference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:')
_l_(17351)
_c_(17354, _n_(17352, "print", lambda: print), _n_(17353, "r2", lambda: r2))
_l_(17355)