# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
_l_(84432)
count_odd = 0
_l_(84433)
for x in _n_(84434, "numbers", lambda: numbers):
    _l_(84439)

    if not _n_(84435, "x", lambda: x) % 2:
        _l_(84438)

        count_even += 1
        _l_(84436)
    else:
        count_odd += 1
        _l_(84437)
_c_(84442, _n_(84440, "print", lambda: print), 'Number of even numbers :', _n_(84441, "count_even", lambda: count_even))
_l_(84443)
_c_(84446, _n_(84444, "print", lambda: print), 'Number of odd numbers :', _n_(84445, "count_odd", lambda: count_odd))
_l_(84447)