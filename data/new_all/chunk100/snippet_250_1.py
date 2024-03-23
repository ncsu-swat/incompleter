# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(19656)

except ImportError:
    pass

def Binary_Search(l, x):
    _l_(19667)

    i = _c_(19660, _n_(19657, "bisect_left", lambda: bisect_left), _n_(19658, "l", lambda: l), _n_(19659, "x", lambda: x))
    _l_(19661)
    if _n_(19662, "i", lambda: i):
        _l_(19666)

        aux = _n_(19663, "i", lambda: i) - 1
        _l_(19664)
        return aux
    else:
        aux = -1
        _l_(19665)
        return aux
nums = [1, 2, 3, 4, 8, 8, 10, 12]
_l_(19668)
x = 5
_l_(19669)
if _n_(19670, "num_position", lambda: num_position) == -1:
    _l_(19679)

    _c_(19672, _n_(19671, "print", lambda: print), 'Not found..!')
    _l_(19673)
else:
    _c_(19677, _n_(19674, "print", lambda: print), 'Largest value smaller than ', _n_(19675, "x", lambda: x), ' is at index ', _n_(19676, "num_position", lambda: num_position))
    _l_(19678)