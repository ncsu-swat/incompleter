# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(35765)

except ImportError:
    pass
a = _c_(35768, _a_(35767, _n_(35766, "np", lambda: np), "array"), [[4, 6], [2, 1]])
_l_(35769)
_c_(35771, _n_(35770, "print", lambda: print), 'Original array: ')
_l_(35772)
_c_(35775, _n_(35773, "print", lambda: print), _n_(35774, "a", lambda: a))
_l_(35776)
_c_(35778, _n_(35777, "print", lambda: print), 'Sort along the first axis: ')
_l_(35779)
x = _c_(35783, _a_(35781, _n_(35780, "np", lambda: np), "sort"), _n_(35782, "a", lambda: a), axis=0)
_l_(35784)
_c_(35787, _n_(35785, "print", lambda: print), _n_(35786, "x", lambda: x))
_l_(35788)
_c_(35790, _n_(35789, "print", lambda: print), 'Sort along the last axis: ')
_l_(35791)
_c_(35794, _n_(35792, "print", lambda: print), _n_(35793, "y", lambda: y))
_l_(35795)