# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(79248)

except ImportError:
    pass

def Binary_Search(a, x):
    _l_(79265)

    i = _c_(79252, _n_(79249, "bisect_left", lambda: bisect_left), _n_(79250, "a", lambda: a), _n_(79251, "x", lambda: x))
    _l_(79253)
    if _n_(79254, "i", lambda: i) != _c_(79257, _n_(79255, "len", lambda: len), _n_(79256, "a", lambda: a)) and _n_(79258, "a", lambda: a)[_n_(79259, "i", lambda: i)] == _n_(79260, "x", lambda: x):
        _l_(79264)

        aux = _n_(79261, "i", lambda: i)
        _l_(79262)
        return aux
    else:
        aux = -1
        _l_(79263)
        return aux
nums = [1, 2, 3, 4, 8, 8, 10, 12]
_l_(79266)
num_position = _c_(79270, _n_(79267, "Binary_Search", lambda: Binary_Search), _n_(79268, "nums", lambda: nums), _n_(79269, "x", lambda: x))
_l_(79271)
if _n_(79272, "num_position", lambda: num_position) == -1:
    _l_(79282)

    _c_(79275, _n_(79273, "print", lambda: print), _n_(79274, "x", lambda: x), 'is not present.')
    _l_(79276)
else:
    _c_(79280, _n_(79277, "print", lambda: print), 'First occurrence of', _n_(79278, "x", lambda: x), 'is present at index', _n_(79279, "num_position", lambda: num_position))
    _l_(79281)