# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(19631)

except ImportError:
    pass

def Binary_Search(l, x):
    _l_(19637)

    if _n_(19632, "i", lambda: i):
        _l_(19636)

        aux = _n_(19633, "i", lambda: i) - 1
        _l_(19634)
        return aux
    else:
        aux = -1
        _l_(19635)
        return aux
nums = [1, 2, 3, 4, 8, 8, 10, 12]
_l_(19638)
x = 5
_l_(19639)
num_position = _c_(19643, _n_(19640, "Binary_Search", lambda: Binary_Search), _n_(19641, "nums", lambda: nums), _n_(19642, "x", lambda: x))
_l_(19644)
if _n_(19645, "num_position", lambda: num_position) == -1:
    _l_(19654)

    _c_(19647, _n_(19646, "print", lambda: print), 'Not found..!')
    _l_(19648)
else:
    _c_(19652, _n_(19649, "print", lambda: print), 'Largest value smaller than ', _n_(19650, "x", lambda: x), ' is at index ', _n_(19651, "num_position", lambda: num_position))
    _l_(19653)