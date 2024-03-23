# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain
    _l_(25613)

except ImportError:
    pass

def sum_of_digits(nums):
    _l_(25626)

    aux = _c_(25624, _n_(25614, "sum", lambda: sum), (_c_(25617, _n_(25615, "int", lambda: int), _n_(25616, "y", lambda: y)) for y in _c_(25623, _n_(25618, "chain", lambda: chain), *[_c_(25621, _n_(25619, "str", lambda: str), _n_(25620, "x", lambda: x)) for x in _n_(25622, "nums", lambda: nums)])))
    _l_(25625)
    return aux
nums = [10, 2, 56]
_l_(25627)
_c_(25629, _n_(25628, "print", lambda: print), 'Original tuple: ')
_l_(25630)
_c_(25633, _n_(25631, "print", lambda: print), _n_(25632, "nums", lambda: nums))
_l_(25634)
_c_(25636, _n_(25635, "print", lambda: print), 'Sum of digits of each number of the said list of integers:')
_l_(25637)
_c_(25642, _n_(25638, "print", lambda: print), _c_(25641, _n_(25639, "sum_of_digits", lambda: sum_of_digits), _n_(25640, "nums", lambda: nums)))
_l_(25643)
_c_(25645, _n_(25644, "print", lambda: print), '\nOriginal tuple: ')
_l_(25646)
_c_(25649, _n_(25647, "print", lambda: print), _n_(25648, "nums", lambda: nums))
_l_(25650)
_c_(25652, _n_(25651, "print", lambda: print), 'Sum of digits of each number of the said list of integers:')
_l_(25653)
_c_(25658, _n_(25654, "print", lambda: print), _c_(25657, _n_(25655, "sum_of_digits", lambda: sum_of_digits), _n_(25656, "nums", lambda: nums)))
_l_(25659)