# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(79284)

except ImportError:
    pass

def Binary_Search(a, x):
    _l_(79296)

    if _n_(79285, "i", lambda: i) != _c_(79288, _n_(79286, "len", lambda: len), _n_(79287, "a", lambda: a)) and _n_(79289, "a", lambda: a)[_n_(79290, "i", lambda: i)] == _n_(79291, "x", lambda: x):
        _l_(79295)

        aux = _n_(79292, "i", lambda: i)
        _l_(79293)
        return aux
    else:
        aux = -1
        _l_(79294)
        return aux
nums = [1, 2, 3, 4, 8, 8, 10, 12]
_l_(79297)
x = 8
_l_(79298)
num_position = _c_(79302, _n_(79299, "Binary_Search", lambda: Binary_Search), _n_(79300, "nums", lambda: nums), _n_(79301, "x", lambda: x))
_l_(79303)
if _n_(79304, "num_position", lambda: num_position) == -1:
    _l_(79314)

    _c_(79307, _n_(79305, "print", lambda: print), _n_(79306, "x", lambda: x), 'is not present.')
    _l_(79308)
else:
    _c_(79312, _n_(79309, "print", lambda: print), 'First occurrence of', _n_(79310, "x", lambda: x), 'is present at index', _n_(79311, "num_position", lambda: num_position))
    _l_(79313)