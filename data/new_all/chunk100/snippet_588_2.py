# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain, combinations
    _l_(61582)

except ImportError:
    pass

def powerset(iterable):
    _l_(61602)

    s = _c_(61585, _n_(61583, "list", lambda: list), _n_(61584, "iterable", lambda: iterable))
    _l_(61586)
    aux = _c_(61600, _n_(61587, "list", lambda: list), _c_(61599, _a_(61589, _n_(61588, "chain", lambda: chain), "from_iterable"), (_c_(61593, _n_(61590, "combinations", lambda: combinations), _n_(61591, "s", lambda: s), _n_(61592, "r", lambda: r)) for r in _c_(61598, _n_(61594, "range", lambda: range), _c_(61597, _n_(61595, "len", lambda: len), _n_(61596, "s", lambda: s)) + 1))))
    _l_(61601)
    return aux
nums = [1, 2]
_l_(61603)
_c_(61605, _n_(61604, "print", lambda: print), 'Original list elements:')
_l_(61606)
_c_(61609, _n_(61607, "print", lambda: print), _n_(61608, "nums", lambda: nums))
_l_(61610)
_c_(61612, _n_(61611, "print", lambda: print), 'Powerset of the said list:')
_l_(61613)
_c_(61618, _n_(61614, "print", lambda: print), _c_(61617, _n_(61615, "powerset", lambda: powerset), _n_(61616, "nums", lambda: nums)))
_l_(61619)
_c_(61621, _n_(61620, "print", lambda: print), '\nOriginal list elements:')
_l_(61622)
_c_(61625, _n_(61623, "print", lambda: print), _n_(61624, "nums", lambda: nums))
_l_(61626)
_c_(61628, _n_(61627, "print", lambda: print), 'Powerset of the said list:')
_l_(61629)
_c_(61634, _n_(61630, "print", lambda: print), _c_(61633, _n_(61631, "powerset", lambda: powerset), _n_(61632, "nums", lambda: nums)))
_l_(61635)