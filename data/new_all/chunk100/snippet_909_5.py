# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(91644)

except ImportError:
    pass
x = _c_(91647, _a_(91646, _n_(91645, "np", lambda: np), "array"), [3.1, 3.5, 4.5, 2.9, -3.1, -3.5, -5.9])
_l_(91648)
_c_(91650, _n_(91649, "print", lambda: print), 'Original array: ')
_l_(91651)
_c_(91654, _n_(91652, "print", lambda: print), _n_(91653, "x", lambda: x))
_l_(91655)
r1 = _c_(91659, _a_(91657, _n_(91656, "np", lambda: np), "around"), _n_(91658, "x", lambda: x))
_l_(91660)
r2 = _c_(91664, _a_(91662, _n_(91661, "np", lambda: np), "floor"), _n_(91663, "x", lambda: x))
_l_(91665)
r3 = _c_(91669, _a_(91667, _n_(91666, "np", lambda: np), "ceil"), _n_(91668, "x", lambda: x))
_l_(91670)
r4 = _c_(91674, _a_(91672, _n_(91671, "np", lambda: np), "trunc"), _n_(91673, "x", lambda: x))
_l_(91675)
_c_(91678, _n_(91676, "print", lambda: print), '\naround:   ', _n_(91677, "r1", lambda: r1))
_l_(91679)
_c_(91682, _n_(91680, "print", lambda: print), 'floor:    ', _n_(91681, "r2", lambda: r2))
_l_(91683)
_c_(91686, _n_(91684, "print", lambda: print), 'ceil:     ', _n_(91685, "r3", lambda: r3))
_l_(91687)
_c_(91690, _n_(91688, "print", lambda: print), 'trunc:    ', _n_(91689, "r4", lambda: r4))
_l_(91691)
_c_(91694, _n_(91692, "print", lambda: print), 'round:    ', _n_(91693, "r5", lambda: r5))
_l_(91695)