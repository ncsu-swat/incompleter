# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain, combinations
    _l_(61475)

except ImportError:
    pass

def powerset(iterable):
    _l_(61495)

    s = _c_(61478, _n_(61476, "list", lambda: list), _n_(61477, "iterable", lambda: iterable))
    _l_(61479)
    aux = _c_(61493, _n_(61480, "list", lambda: list), _c_(61492, _a_(61482, _n_(61481, "chain", lambda: chain), "from_iterable"), (_c_(61486, _n_(61483, "combinations", lambda: combinations), _n_(61484, "s", lambda: s), _n_(61485, "r", lambda: r)) for r in _c_(61491, _n_(61487, "range", lambda: range), _c_(61490, _n_(61488, "len", lambda: len), _n_(61489, "s", lambda: s)) + 1))))
    _l_(61494)
    return aux
_c_(61497, _n_(61496, "print", lambda: print), 'Original list elements:')
_l_(61498)
_c_(61501, _n_(61499, "print", lambda: print), _n_(61500, "nums", lambda: nums))
_l_(61502)
_c_(61504, _n_(61503, "print", lambda: print), 'Powerset of the said list:')
_l_(61505)
_c_(61510, _n_(61506, "print", lambda: print), _c_(61509, _n_(61507, "powerset", lambda: powerset), _n_(61508, "nums", lambda: nums)))
_l_(61511)
nums = [1, 2, 3, 4]
_l_(61512)
_c_(61514, _n_(61513, "print", lambda: print), '\nOriginal list elements:')
_l_(61515)
_c_(61518, _n_(61516, "print", lambda: print), _n_(61517, "nums", lambda: nums))
_l_(61519)
_c_(61521, _n_(61520, "print", lambda: print), 'Powerset of the said list:')
_l_(61522)
_c_(61527, _n_(61523, "print", lambda: print), _c_(61526, _n_(61524, "powerset", lambda: powerset), _n_(61525, "nums", lambda: nums)))
_l_(61528)