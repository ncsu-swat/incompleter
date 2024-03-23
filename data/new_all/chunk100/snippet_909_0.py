# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(91378)

except ImportError:
    pass
x = _c_(91381, _a_(91380, _n_(91379, "np", lambda: np), "array"), [3.1, 3.5, 4.5, 2.9, -3.1, -3.5, -5.9])
_l_(91382)
_c_(91384, _n_(91383, "print", lambda: print), 'Original array: ')
_l_(91385)
_c_(91388, _n_(91386, "print", lambda: print), _n_(91387, "x", lambda: x))
_l_(91389)
r2 = _c_(91393, _a_(91391, _n_(91390, "np", lambda: np), "floor"), _n_(91392, "x", lambda: x))
_l_(91394)
r3 = _c_(91398, _a_(91396, _n_(91395, "np", lambda: np), "ceil"), _n_(91397, "x", lambda: x))
_l_(91399)
r4 = _c_(91403, _a_(91401, _n_(91400, "np", lambda: np), "trunc"), _n_(91402, "x", lambda: x))
_l_(91404)
r5 = [_c_(91407, _n_(91405, "round", lambda: round), _n_(91406, "elem", lambda: elem)) for elem in _n_(91408, "x", lambda: x)]
_l_(91409)
_c_(91412, _n_(91410, "print", lambda: print), '\naround:   ', _n_(91411, "r1", lambda: r1))
_l_(91413)
_c_(91416, _n_(91414, "print", lambda: print), 'floor:    ', _n_(91415, "r2", lambda: r2))
_l_(91417)
_c_(91420, _n_(91418, "print", lambda: print), 'ceil:     ', _n_(91419, "r3", lambda: r3))
_l_(91421)
_c_(91424, _n_(91422, "print", lambda: print), 'trunc:    ', _n_(91423, "r4", lambda: r4))
_l_(91425)
_c_(91428, _n_(91426, "print", lambda: print), 'round:    ', _n_(91427, "r5", lambda: r5))
_l_(91429)