# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105721)

except ImportError:
    pass
x = _c_(105724, _a_(105723, _n_(105722, "np", lambda: np), "array"), [1, 3, 5, 7, 0])
_l_(105725)
_c_(105727, _n_(105726, "print", lambda: print), 'Original array: ')
_l_(105728)
_c_(105731, _n_(105729, "print", lambda: print), _n_(105730, "x", lambda: x))
_l_(105732)
r2 = _c_(105742, _a_(105734, _n_(105733, "np", lambda: np), "insert"), _c_(105741, _a_(105736, _n_(105735, "np", lambda: np), "append"), _c_(105740, _a_(105738, _n_(105737, "np", lambda: np), "diff"), _n_(105739, "x", lambda: x)), 200), 0, [0, 0])
_l_(105743)
assert _c_(105748, _a_(105745, _n_(105744, "np", lambda: np), "array_equiv"), _n_(105746, "r1", lambda: r1), _n_(105747, "r2", lambda: r2))
_l_(105749)
_c_(105751, _n_(105750, "print", lambda: print), 'Difference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:')
_l_(105752)
_c_(105755, _n_(105753, "print", lambda: print), _n_(105754, "r2", lambda: r2))
_l_(105756)