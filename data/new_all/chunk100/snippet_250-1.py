# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(106980)

except ImportError:
    pass

def Binary_Search(l, x):
    _l_(106991)

    i = _c_(106984, _n_(106981, "bisect_left", lambda: bisect_left), _n_(106982, "l", lambda: l), _n_(106983, "x", lambda: x))
    _l_(106985)
    if _n_(106986, "i", lambda: i):
        _l_(106990)

        aux = _n_(106987, "i", lambda: i) - 1
        _l_(106988)
        return aux
    else:
        aux = -1
        _l_(106989)
        return aux
nums = [1, 2, 3, 4, 8, 8, 10, 12]
_l_(106992)
x = 5
_l_(106993)
if _n_(106994, "num_position", lambda: num_position) == -1:
    _l_(107003)

    _c_(106996, _n_(106995, "print", lambda: print), 'Not found..!')
    _l_(106997)
else:
    _c_(107001, _n_(106998, "print", lambda: print), 'Largest value smaller than ', _n_(106999, "x", lambda: x), ' is at index ', _n_(107000, "num_position", lambda: num_position))
    _l_(107002)