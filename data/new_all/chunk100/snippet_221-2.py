# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105789)

except ImportError:
    pass
_c_(105791, _n_(105790, "print", lambda: print), 'Original array: ')
_l_(105792)
_c_(105795, _n_(105793, "print", lambda: print), _n_(105794, "x", lambda: x))
_l_(105796)
r1 = _c_(105800, _a_(105798, _n_(105797, "np", lambda: np), "ediff1d"), _n_(105799, "x", lambda: x), to_begin=[0, 0], to_end=[200])
_l_(105801)
r2 = _c_(105811, _a_(105803, _n_(105802, "np", lambda: np), "insert"), _c_(105810, _a_(105805, _n_(105804, "np", lambda: np), "append"), _c_(105809, _a_(105807, _n_(105806, "np", lambda: np), "diff"), _n_(105808, "x", lambda: x)), 200), 0, [0, 0])
_l_(105812)
assert _c_(105817, _a_(105814, _n_(105813, "np", lambda: np), "array_equiv"), _n_(105815, "r1", lambda: r1), _n_(105816, "r2", lambda: r2))
_l_(105818)
_c_(105820, _n_(105819, "print", lambda: print), 'Difference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:')
_l_(105821)
_c_(105824, _n_(105822, "print", lambda: print), _n_(105823, "r2", lambda: r2))
_l_(105825)