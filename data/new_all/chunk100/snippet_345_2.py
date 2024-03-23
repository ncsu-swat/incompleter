# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(34570)

except ImportError:
    pass
_c_(34572, _n_(34571, "print", lambda: print), 'Original array: ')
_l_(34573)
_c_(34576, _n_(34574, "print", lambda: print), _n_(34575, "x", lambda: x))
_l_(34577)
_c_(34579, _n_(34578, "print", lambda: print), 'Cumulative product  of the elements along a given axis:')
_l_(34580)
r = _c_(34584, _a_(34582, _n_(34581, "np", lambda: np), "cumprod"), _n_(34583, "x", lambda: x))
_l_(34585)
_c_(34588, _n_(34586, "print", lambda: print), _n_(34587, "r", lambda: r))
_l_(34589)
_c_(34591, _n_(34590, "print", lambda: print), '\nProduct over rows for each of the 3 columns:')
_l_(34592)
r = _c_(34596, _a_(34594, _n_(34593, "np", lambda: np), "cumprod"), _n_(34595, "x", lambda: x), axis=0)
_l_(34597)
_c_(34600, _n_(34598, "print", lambda: print), _n_(34599, "r", lambda: r))
_l_(34601)
_c_(34603, _n_(34602, "print", lambda: print), '\nProduct  over columns for each of the 2 rows:')
_l_(34604)
r = _c_(34608, _a_(34606, _n_(34605, "np", lambda: np), "cumprod"), _n_(34607, "x", lambda: x), axis=1)
_l_(34609)
_c_(34612, _n_(34610, "print", lambda: print), _n_(34611, "r", lambda: r))
_l_(34613)