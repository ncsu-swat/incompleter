# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(91537)

except ImportError:
    pass
_c_(91539, _n_(91538, "print", lambda: print), 'Original array: ')
_l_(91540)
_c_(91543, _n_(91541, "print", lambda: print), _n_(91542, "x", lambda: x))
_l_(91544)
r1 = _c_(91548, _a_(91546, _n_(91545, "np", lambda: np), "around"), _n_(91547, "x", lambda: x))
_l_(91549)
r2 = _c_(91553, _a_(91551, _n_(91550, "np", lambda: np), "floor"), _n_(91552, "x", lambda: x))
_l_(91554)
r3 = _c_(91558, _a_(91556, _n_(91555, "np", lambda: np), "ceil"), _n_(91557, "x", lambda: x))
_l_(91559)
r4 = _c_(91563, _a_(91561, _n_(91560, "np", lambda: np), "trunc"), _n_(91562, "x", lambda: x))
_l_(91564)
r5 = [_c_(91567, _n_(91565, "round", lambda: round), _n_(91566, "elem", lambda: elem)) for elem in _n_(91568, "x", lambda: x)]
_l_(91569)
_c_(91572, _n_(91570, "print", lambda: print), '\naround:   ', _n_(91571, "r1", lambda: r1))
_l_(91573)
_c_(91576, _n_(91574, "print", lambda: print), 'floor:    ', _n_(91575, "r2", lambda: r2))
_l_(91577)
_c_(91580, _n_(91578, "print", lambda: print), 'ceil:     ', _n_(91579, "r3", lambda: r3))
_l_(91581)
_c_(91584, _n_(91582, "print", lambda: print), 'trunc:    ', _n_(91583, "r4", lambda: r4))
_l_(91585)
_c_(91588, _n_(91586, "print", lambda: print), 'round:    ', _n_(91587, "r5", lambda: r5))
_l_(91589)