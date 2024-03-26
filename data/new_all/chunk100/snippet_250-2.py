# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(107005)

except ImportError:
    pass

def Binary_Search(l, x):
    _l_(107016)

    i = _c_(107009, _n_(107006, "bisect_left", lambda: bisect_left), _n_(107007, "l", lambda: l), _n_(107008, "x", lambda: x))
    _l_(107010)
    if _n_(107011, "i", lambda: i):
        _l_(107015)

        aux = _n_(107012, "i", lambda: i) - 1
        _l_(107013)
        return aux
    else:
        aux = -1
        _l_(107014)
        return aux
nums = [1, 2, 3, 4, 8, 8, 10, 12]
_l_(107017)
num_position = _c_(107021, _n_(107018, "Binary_Search", lambda: Binary_Search), _n_(107019, "nums", lambda: nums), _n_(107020, "x", lambda: x))
_l_(107022)
if _n_(107023, "num_position", lambda: num_position) == -1:
    _l_(107032)

    _c_(107025, _n_(107024, "print", lambda: print), 'Not found..!')
    _l_(107026)
else:
    _c_(107030, _n_(107027, "print", lambda: print), 'Largest value smaller than ', _n_(107028, "x", lambda: x), ' is at index ', _n_(107029, "num_position", lambda: num_position))
    _l_(107031)