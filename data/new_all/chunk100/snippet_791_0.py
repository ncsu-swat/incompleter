# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(79640)

except ImportError:
    pass
_c_(79642, _n_(79641, "print", lambda: print), '\nTest element-wise for finiteness (not infinity or not Not a Number):')
_l_(79643)
_c_(79648, _n_(79644, "print", lambda: print), _c_(79647, _a_(79646, _n_(79645, "np", lambda: np), "isfinite"), 1))
_l_(79649)
_c_(79654, _n_(79650, "print", lambda: print), _c_(79653, _a_(79652, _n_(79651, "np", lambda: np), "isfinite"), 0))
_l_(79655)
_c_(79662, _n_(79656, "print", lambda: print), _c_(79661, _a_(79658, _n_(79657, "np", lambda: np), "isfinite"), _a_(79660, _n_(79659, "np", lambda: np), "nan")))
_l_(79663)
_c_(79665, _n_(79664, "print", lambda: print), '\nTest element-wise for positive or negative infinity:')
_l_(79666)
_c_(79673, _n_(79667, "print", lambda: print), _c_(79672, _a_(79669, _n_(79668, "np", lambda: np), "isinf"), _a_(79671, _n_(79670, "np", lambda: np), "inf")))
_l_(79674)
_c_(79681, _n_(79675, "print", lambda: print), _c_(79680, _a_(79677, _n_(79676, "np", lambda: np), "isinf"), _a_(79679, _n_(79678, "np", lambda: np), "nan")))
_l_(79682)
_c_(79689, _n_(79683, "print", lambda: print), _c_(79688, _a_(79685, _n_(79684, "np", lambda: np), "isinf"), _a_(79687, _n_(79686, "np", lambda: np), "NINF")))
_l_(79690)
_c_(79692, _n_(79691, "print", lambda: print), 'Test element-wise for NaN:')
_l_(79693)
_c_(79704, _n_(79694, "print", lambda: print), _c_(79703, _a_(79696, _n_(79695, "np", lambda: np), "isnan"), [_c_(79699, _a_(79698, _n_(79697, "np", lambda: np), "log"), -1.0), 1.0, _c_(79702, _a_(79701, _n_(79700, "np", lambda: np), "log"), 0)]))
_l_(79705)
_c_(79707, _n_(79706, "print", lambda: print), 'Test element-wise for NaT (not a time):')
_l_(79708)
_c_(79716, _n_(79709, "print", lambda: print), _c_(79715, _a_(79711, _n_(79710, "np", lambda: np), "isnat"), _c_(79714, _a_(79713, _n_(79712, "np", lambda: np), "array"), ['NaT', '2016-01-01'], dtype='datetime64[ns]')))
_l_(79717)
_c_(79719, _n_(79718, "print", lambda: print), 'Test element-wise for negative infinity:')
_l_(79720)
y = _c_(79723, _a_(79722, _n_(79721, "np", lambda: np), "array"), [2, 2, 2])
_l_(79724)
_c_(79731, _n_(79725, "print", lambda: print), _c_(79730, _a_(79727, _n_(79726, "np", lambda: np), "isneginf"), _n_(79728, "x", lambda: x), _n_(79729, "y", lambda: y)))
_l_(79732)
_c_(79734, _n_(79733, "print", lambda: print), 'Test element-wise for positive infinity:')
_l_(79735)
x = _c_(79742, _a_(79737, _n_(79736, "np", lambda: np), "array"), [-_a_(79739, _n_(79738, "np", lambda: np), "inf"), 0.0, _a_(79741, _n_(79740, "np", lambda: np), "inf")])
_l_(79743)
y = _c_(79746, _a_(79745, _n_(79744, "np", lambda: np), "array"), [2, 2, 2])
_l_(79747)
_c_(79754, _n_(79748, "print", lambda: print), _c_(79753, _a_(79750, _n_(79749, "np", lambda: np), "isposinf"), _n_(79751, "x", lambda: x), _n_(79752, "y", lambda: y)))
_l_(79755)