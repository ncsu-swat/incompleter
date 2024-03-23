# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain, combinations
    _l_(61530)

except ImportError:
    pass

def powerset(iterable):
    _l_(61546)

    aux = _c_(61544, _n_(61531, "list", lambda: list), _c_(61543, _a_(61533, _n_(61532, "chain", lambda: chain), "from_iterable"), (_c_(61537, _n_(61534, "combinations", lambda: combinations), _n_(61535, "s", lambda: s), _n_(61536, "r", lambda: r)) for r in _c_(61542, _n_(61538, "range", lambda: range), _c_(61541, _n_(61539, "len", lambda: len), _n_(61540, "s", lambda: s)) + 1))))
    _l_(61545)
    return aux
nums = [1, 2]
_l_(61547)
_c_(61549, _n_(61548, "print", lambda: print), 'Original list elements:')
_l_(61550)
_c_(61553, _n_(61551, "print", lambda: print), _n_(61552, "nums", lambda: nums))
_l_(61554)
_c_(61556, _n_(61555, "print", lambda: print), 'Powerset of the said list:')
_l_(61557)
_c_(61562, _n_(61558, "print", lambda: print), _c_(61561, _n_(61559, "powerset", lambda: powerset), _n_(61560, "nums", lambda: nums)))
_l_(61563)
nums = [1, 2, 3, 4]
_l_(61564)
_c_(61566, _n_(61565, "print", lambda: print), '\nOriginal list elements:')
_l_(61567)
_c_(61570, _n_(61568, "print", lambda: print), _n_(61569, "nums", lambda: nums))
_l_(61571)
_c_(61573, _n_(61572, "print", lambda: print), 'Powerset of the said list:')
_l_(61574)
_c_(61579, _n_(61575, "print", lambda: print), _c_(61578, _n_(61576, "powerset", lambda: powerset), _n_(61577, "nums", lambda: nums)))
_l_(61580)