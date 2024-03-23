# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(92615)

except ImportError:
    pass
x = _c_(92618, _a_(92617, _n_(92616, "np", lambda: np), "array"), [1, 2, 3])
_l_(92619)
y = _c_(92622, _a_(92621, _n_(92620, "np", lambda: np), "array"), [2, 3, 4])
_l_(92623)
_c_(92625, _n_(92624, "print", lambda: print), 'Original arrays:')
_l_(92626)
_c_(92629, _n_(92627, "print", lambda: print), _n_(92628, "x", lambda: x))
_l_(92630)
_c_(92633, _n_(92631, "print", lambda: print), _n_(92632, "y", lambda: y))
_l_(92634)
_c_(92636, _n_(92635, "print", lambda: print), 'Sequence of arrays along a new axis:')
_l_(92637)
_c_(92644, _n_(92638, "print", lambda: print), _c_(92643, _a_(92640, _n_(92639, "np", lambda: np), "vstack"), (_n_(92641, "x", lambda: x), _n_(92642, "y", lambda: y))))
_l_(92645)
y = _c_(92648, _a_(92647, _n_(92646, "np", lambda: np), "array"), [[2], [3], [4]])
_l_(92649)
_c_(92651, _n_(92650, "print", lambda: print), '\nOriginal arrays:')
_l_(92652)
_c_(92655, _n_(92653, "print", lambda: print), _n_(92654, "x", lambda: x))
_l_(92656)
_c_(92658, _n_(92657, "print", lambda: print))
_l_(92659)
_c_(92662, _n_(92660, "print", lambda: print), _n_(92661, "y", lambda: y))
_l_(92663)
_c_(92665, _n_(92664, "print", lambda: print), 'Sequence of arrays along a new axis:')
_l_(92666)
_c_(92673, _n_(92667, "print", lambda: print), _c_(92672, _a_(92669, _n_(92668, "np", lambda: np), "vstack"), (_n_(92670, "x", lambda: x), _n_(92671, "y", lambda: y))))
_l_(92674)