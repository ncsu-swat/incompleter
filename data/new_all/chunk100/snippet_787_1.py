# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(79216)

except ImportError:
    pass

def Binary_Search(a, x):
    _l_(79233)

    i = _c_(79220, _n_(79217, "bisect_left", lambda: bisect_left), _n_(79218, "a", lambda: a), _n_(79219, "x", lambda: x))
    _l_(79221)
    if _n_(79222, "i", lambda: i) != _c_(79225, _n_(79223, "len", lambda: len), _n_(79224, "a", lambda: a)) and _n_(79226, "a", lambda: a)[_n_(79227, "i", lambda: i)] == _n_(79228, "x", lambda: x):
        _l_(79232)

        aux = _n_(79229, "i", lambda: i)
        _l_(79230)
        return aux
    else:
        aux = -1
        _l_(79231)
        return aux
nums = [1, 2, 3, 4, 8, 8, 10, 12]
_l_(79234)
x = 8
_l_(79235)
if _n_(79236, "num_position", lambda: num_position) == -1:
    _l_(79246)

    _c_(79239, _n_(79237, "print", lambda: print), _n_(79238, "x", lambda: x), 'is not present.')
    _l_(79240)
else:
    _c_(79244, _n_(79241, "print", lambda: print), 'First occurrence of', _n_(79242, "x", lambda: x), 'is present at index', _n_(79243, "num_position", lambda: num_position))
    _l_(79245)