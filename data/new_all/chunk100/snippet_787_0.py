# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(79180)

except ImportError:
    pass

def Binary_Search(a, x):
    _l_(79197)

    i = _c_(79184, _n_(79181, "bisect_left", lambda: bisect_left), _n_(79182, "a", lambda: a), _n_(79183, "x", lambda: x))
    _l_(79185)
    if _n_(79186, "i", lambda: i) != _c_(79189, _n_(79187, "len", lambda: len), _n_(79188, "a", lambda: a)) and _n_(79190, "a", lambda: a)[_n_(79191, "i", lambda: i)] == _n_(79192, "x", lambda: x):
        _l_(79196)

        aux = _n_(79193, "i", lambda: i)
        _l_(79194)
        return aux
    else:
        aux = -1
        _l_(79195)
        return aux
x = 8
_l_(79198)
num_position = _c_(79202, _n_(79199, "Binary_Search", lambda: Binary_Search), _n_(79200, "nums", lambda: nums), _n_(79201, "x", lambda: x))
_l_(79203)
if _n_(79204, "num_position", lambda: num_position) == -1:
    _l_(79214)

    _c_(79207, _n_(79205, "print", lambda: print), _n_(79206, "x", lambda: x), 'is not present.')
    _l_(79208)
else:
    _c_(79212, _n_(79209, "print", lambda: print), 'First occurrence of', _n_(79210, "x", lambda: x), 'is present at index', _n_(79211, "num_position", lambda: num_position))
    _l_(79213)