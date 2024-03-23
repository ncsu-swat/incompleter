# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(91431)

except ImportError:
    pass
x = _c_(91434, _a_(91433, _n_(91432, "np", lambda: np), "array"), [3.1, 3.5, 4.5, 2.9, -3.1, -3.5, -5.9])
_l_(91435)
_c_(91437, _n_(91436, "print", lambda: print), 'Original array: ')
_l_(91438)
_c_(91441, _n_(91439, "print", lambda: print), _n_(91440, "x", lambda: x))
_l_(91442)
r1 = _c_(91446, _a_(91444, _n_(91443, "np", lambda: np), "around"), _n_(91445, "x", lambda: x))
_l_(91447)
r2 = _c_(91451, _a_(91449, _n_(91448, "np", lambda: np), "floor"), _n_(91450, "x", lambda: x))
_l_(91452)
r4 = _c_(91456, _a_(91454, _n_(91453, "np", lambda: np), "trunc"), _n_(91455, "x", lambda: x))
_l_(91457)
r5 = [_c_(91460, _n_(91458, "round", lambda: round), _n_(91459, "elem", lambda: elem)) for elem in _n_(91461, "x", lambda: x)]
_l_(91462)
_c_(91465, _n_(91463, "print", lambda: print), '\naround:   ', _n_(91464, "r1", lambda: r1))
_l_(91466)
_c_(91469, _n_(91467, "print", lambda: print), 'floor:    ', _n_(91468, "r2", lambda: r2))
_l_(91470)
_c_(91473, _n_(91471, "print", lambda: print), 'ceil:     ', _n_(91472, "r3", lambda: r3))
_l_(91474)
_c_(91477, _n_(91475, "print", lambda: print), 'trunc:    ', _n_(91476, "r4", lambda: r4))
_l_(91478)
_c_(91481, _n_(91479, "print", lambda: print), 'round:    ', _n_(91480, "r5", lambda: r5))
_l_(91482)