# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(19710)

except ImportError:
    pass

def Binary_Search(l, x):
    _l_(19721)

    i = _c_(19714, _n_(19711, "bisect_left", lambda: bisect_left), _n_(19712, "l", lambda: l), _n_(19713, "x", lambda: x))
    _l_(19715)
    if _n_(19716, "i", lambda: i):
        _l_(19720)

        aux = _n_(19717, "i", lambda: i) - 1
        _l_(19718)
        return aux
    else:
        aux = -1
        _l_(19719)
        return aux
nums = [1, 2, 3, 4, 8, 8, 10, 12]
_l_(19722)
num_position = _c_(19726, _n_(19723, "Binary_Search", lambda: Binary_Search), _n_(19724, "nums", lambda: nums), _n_(19725, "x", lambda: x))
_l_(19727)
if _n_(19728, "num_position", lambda: num_position) == -1:
    _l_(19737)

    _c_(19730, _n_(19729, "print", lambda: print), 'Not found..!')
    _l_(19731)
else:
    _c_(19735, _n_(19732, "print", lambda: print), 'Largest value smaller than ', _n_(19733, "x", lambda: x), ' is at index ', _n_(19734, "num_position", lambda: num_position))
    _l_(19736)