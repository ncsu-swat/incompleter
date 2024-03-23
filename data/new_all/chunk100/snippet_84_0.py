# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
_l_(84416)
count_even = 0
_l_(84417)
for x in _n_(84418, "numbers", lambda: numbers):
    _l_(84423)

    if not _n_(84419, "x", lambda: x) % 2:
        _l_(84422)

        count_even += 1
        _l_(84420)
    else:
        count_odd += 1
        _l_(84421)
_c_(84426, _n_(84424, "print", lambda: print), 'Number of even numbers :', _n_(84425, "count_even", lambda: count_even))
_l_(84427)
_c_(84430, _n_(84428, "print", lambda: print), 'Number of odd numbers :', _n_(84429, "count_odd", lambda: count_odd))
_l_(84431)