# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count_odd = 0
_l_(120813)
count_even = 0
_l_(120814)
for x in _n_(120815, "numbers", lambda: numbers):
    _l_(120820)

    if not _n_(120816, "x", lambda: x) % 2:
        _l_(120819)

        count_even += 1
        _l_(120817)
    else:
        count_odd += 1
        _l_(120818)
_c_(120823, _n_(120821, "print", lambda: print), 'Number of even numbers :', _n_(120822, "count_even", lambda: count_even))
_l_(120824)
_c_(120827, _n_(120825, "print", lambda: print), 'Number of odd numbers :', _n_(120826, "count_odd", lambda: count_odd))
_l_(120828)