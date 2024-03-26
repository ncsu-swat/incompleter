# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
_l_(120829)
count_even = 0
_l_(120830)
for x in _n_(120831, "numbers", lambda: numbers):
    _l_(120836)

    if not _n_(120832, "x", lambda: x) % 2:
        _l_(120835)

        count_even += 1
        _l_(120833)
    else:
        count_odd += 1
        _l_(120834)
_c_(120839, _n_(120837, "print", lambda: print), 'Number of even numbers :', _n_(120838, "count_even", lambda: count_even))
_l_(120840)
_c_(120843, _n_(120841, "print", lambda: print), 'Number of odd numbers :', _n_(120842, "count_odd", lambda: count_odd))
_l_(120844)