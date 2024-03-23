# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(81021)

except ImportError:
    pass
even_deque = _c_(81025, _a_(81023, _n_(81022, "collections", lambda: collections), "deque"), _n_(81024, "even_nums", lambda: even_nums))
_l_(81026)
_c_(81028, _n_(81027, "print", lambda: print), 'Even numbers:')
_l_(81029)
_c_(81032, _n_(81030, "print", lambda: print), _n_(81031, "even_deque", lambda: even_deque))
_l_(81033)
more_even_nums = (12, 14, 16, 18, 20)
_l_(81034)
_c_(81038, _a_(81036, _n_(81035, "even_deque", lambda: even_deque), "extend"), _n_(81037, "more_even_nums", lambda: more_even_nums))
_l_(81039)
_c_(81041, _n_(81040, "print", lambda: print), 'More even numbers:')
_l_(81042)
_c_(81045, _n_(81043, "print", lambda: print), _n_(81044, "even_deque", lambda: even_deque))
_l_(81046)