# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(92554)

except ImportError:
    pass
x = _c_(92557, _a_(92556, _n_(92555, "np", lambda: np), "array"), [1, 2, 3])
_l_(92558)
_c_(92560, _n_(92559, "print", lambda: print), 'Original arrays:')
_l_(92561)
_c_(92564, _n_(92562, "print", lambda: print), _n_(92563, "x", lambda: x))
_l_(92565)
_c_(92568, _n_(92566, "print", lambda: print), _n_(92567, "y", lambda: y))
_l_(92569)
_c_(92571, _n_(92570, "print", lambda: print), 'Sequence of arrays along a new axis:')
_l_(92572)
_c_(92579, _n_(92573, "print", lambda: print), _c_(92578, _a_(92575, _n_(92574, "np", lambda: np), "vstack"), (_n_(92576, "x", lambda: x), _n_(92577, "y", lambda: y))))
_l_(92580)
x = _c_(92583, _a_(92582, _n_(92581, "np", lambda: np), "array"), [[1], [2], [3]])
_l_(92584)
y = _c_(92587, _a_(92586, _n_(92585, "np", lambda: np), "array"), [[2], [3], [4]])
_l_(92588)
_c_(92590, _n_(92589, "print", lambda: print), '\nOriginal arrays:')
_l_(92591)
_c_(92594, _n_(92592, "print", lambda: print), _n_(92593, "x", lambda: x))
_l_(92595)
_c_(92597, _n_(92596, "print", lambda: print))
_l_(92598)
_c_(92601, _n_(92599, "print", lambda: print), _n_(92600, "y", lambda: y))
_l_(92602)
_c_(92604, _n_(92603, "print", lambda: print), 'Sequence of arrays along a new axis:')
_l_(92605)
_c_(92612, _n_(92606, "print", lambda: print), _c_(92611, _a_(92608, _n_(92607, "np", lambda: np), "vstack"), (_n_(92609, "x", lambda: x), _n_(92610, "y", lambda: y))))
_l_(92613)