# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(91484)

except ImportError:
    pass
x = _c_(91487, _a_(91486, _n_(91485, "np", lambda: np), "array"), [3.1, 3.5, 4.5, 2.9, -3.1, -3.5, -5.9])
_l_(91488)
_c_(91490, _n_(91489, "print", lambda: print), 'Original array: ')
_l_(91491)
_c_(91494, _n_(91492, "print", lambda: print), _n_(91493, "x", lambda: x))
_l_(91495)
r1 = _c_(91499, _a_(91497, _n_(91496, "np", lambda: np), "around"), _n_(91498, "x", lambda: x))
_l_(91500)
r2 = _c_(91504, _a_(91502, _n_(91501, "np", lambda: np), "floor"), _n_(91503, "x", lambda: x))
_l_(91505)
r3 = _c_(91509, _a_(91507, _n_(91506, "np", lambda: np), "ceil"), _n_(91508, "x", lambda: x))
_l_(91510)
r5 = [_c_(91513, _n_(91511, "round", lambda: round), _n_(91512, "elem", lambda: elem)) for elem in _n_(91514, "x", lambda: x)]
_l_(91515)
_c_(91518, _n_(91516, "print", lambda: print), '\naround:   ', _n_(91517, "r1", lambda: r1))
_l_(91519)
_c_(91522, _n_(91520, "print", lambda: print), 'floor:    ', _n_(91521, "r2", lambda: r2))
_l_(91523)
_c_(91526, _n_(91524, "print", lambda: print), 'ceil:     ', _n_(91525, "r3", lambda: r3))
_l_(91527)
_c_(91530, _n_(91528, "print", lambda: print), 'trunc:    ', _n_(91529, "r4", lambda: r4))
_l_(91531)
_c_(91534, _n_(91532, "print", lambda: print), 'round:    ', _n_(91533, "r5", lambda: r5))
_l_(91535)