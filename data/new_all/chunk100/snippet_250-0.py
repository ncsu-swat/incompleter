# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bisect import bisect_left
    _l_(106951)

except ImportError:
    pass

def Binary_Search(l, x):
    _l_(106962)

    i = _c_(106955, _n_(106952, "bisect_left", lambda: bisect_left), _n_(106953, "l", lambda: l), _n_(106954, "x", lambda: x))
    _l_(106956)
    if _n_(106957, "i", lambda: i):
        _l_(106961)

        aux = _n_(106958, "i", lambda: i) - 1
        _l_(106959)
        return aux
    else:
        aux = -1
        _l_(106960)
        return aux
x = 5
_l_(106963)
num_position = _c_(106967, _n_(106964, "Binary_Search", lambda: Binary_Search), _n_(106965, "nums", lambda: nums), _n_(106966, "x", lambda: x))
_l_(106968)
if _n_(106969, "num_position", lambda: num_position) == -1:
    _l_(106978)

    _c_(106971, _n_(106970, "print", lambda: print), 'Not found..!')
    _l_(106972)
else:
    _c_(106976, _n_(106973, "print", lambda: print), 'Largest value smaller than ', _n_(106974, "x", lambda: x), ' is at index ', _n_(106975, "num_position", lambda: num_position))
    _l_(106977)