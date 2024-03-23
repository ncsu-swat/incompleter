# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(81071)

except ImportError:
    pass
even_nums = (2, 4, 6, 8, 10)
_l_(81072)
even_deque = _c_(81076, _a_(81074, _n_(81073, "collections", lambda: collections), "deque"), _n_(81075, "even_nums", lambda: even_nums))
_l_(81077)
_c_(81079, _n_(81078, "print", lambda: print), 'Even numbers:')
_l_(81080)
_c_(81083, _n_(81081, "print", lambda: print), _n_(81082, "even_deque", lambda: even_deque))
_l_(81084)
_c_(81088, _a_(81086, _n_(81085, "even_deque", lambda: even_deque), "extend"), _n_(81087, "more_even_nums", lambda: more_even_nums))
_l_(81089)
_c_(81091, _n_(81090, "print", lambda: print), 'More even numbers:')
_l_(81092)
_c_(81095, _n_(81093, "print", lambda: print), _n_(81094, "even_deque", lambda: even_deque))
_l_(81096)