# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(19681)

except ImportError:
    pass

def Binary_Search(l, x):
    _l_(19692)

    i = _c_(19685, _n_(19682, "bisect_left", lambda: bisect_left), _n_(19683, "l", lambda: l), _n_(19684, "x", lambda: x))
    _l_(19686)
    if _n_(19687, "i", lambda: i):
        _l_(19691)

        aux = _n_(19688, "i", lambda: i) - 1
        _l_(19689)
        return aux
    else:
        aux = -1
        _l_(19690)
        return aux
x = 5
_l_(19693)
num_position = _c_(19697, _n_(19694, "Binary_Search", lambda: Binary_Search), _n_(19695, "nums", lambda: nums), _n_(19696, "x", lambda: x))
_l_(19698)
if _n_(19699, "num_position", lambda: num_position) == -1:
    _l_(19708)

    _c_(19701, _n_(19700, "print", lambda: print), 'Not found..!')
    _l_(19702)
else:
    _c_(19706, _n_(19703, "print", lambda: print), 'Largest value smaller than ', _n_(19704, "x", lambda: x), ' is at index ', _n_(19705, "num_position", lambda: num_position))
    _l_(19707)