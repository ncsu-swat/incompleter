# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(91591)

except ImportError:
    pass
x = _c_(91594, _a_(91593, _n_(91592, "np", lambda: np), "array"), [3.1, 3.5, 4.5, 2.9, -3.1, -3.5, -5.9])
_l_(91595)
_c_(91597, _n_(91596, "print", lambda: print), 'Original array: ')
_l_(91598)
_c_(91601, _n_(91599, "print", lambda: print), _n_(91600, "x", lambda: x))
_l_(91602)
r1 = _c_(91606, _a_(91604, _n_(91603, "np", lambda: np), "around"), _n_(91605, "x", lambda: x))
_l_(91607)
r3 = _c_(91611, _a_(91609, _n_(91608, "np", lambda: np), "ceil"), _n_(91610, "x", lambda: x))
_l_(91612)
r4 = _c_(91616, _a_(91614, _n_(91613, "np", lambda: np), "trunc"), _n_(91615, "x", lambda: x))
_l_(91617)
r5 = [_c_(91620, _n_(91618, "round", lambda: round), _n_(91619, "elem", lambda: elem)) for elem in _n_(91621, "x", lambda: x)]
_l_(91622)
_c_(91625, _n_(91623, "print", lambda: print), '\naround:   ', _n_(91624, "r1", lambda: r1))
_l_(91626)
_c_(91629, _n_(91627, "print", lambda: print), 'floor:    ', _n_(91628, "r2", lambda: r2))
_l_(91630)
_c_(91633, _n_(91631, "print", lambda: print), 'ceil:     ', _n_(91632, "r3", lambda: r3))
_l_(91634)
_c_(91637, _n_(91635, "print", lambda: print), 'trunc:    ', _n_(91636, "r4", lambda: r4))
_l_(91638)
_c_(91641, _n_(91639, "print", lambda: print), 'round:    ', _n_(91640, "r5", lambda: r5))
_l_(91642)