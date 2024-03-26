# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
_l_(120845)
count_odd = 0
_l_(120846)
for x in _n_(120847, "numbers", lambda: numbers):
    _l_(120852)

    if not _n_(120848, "x", lambda: x) % 2:
        _l_(120851)

        count_even += 1
        _l_(120849)
    else:
        count_odd += 1
        _l_(120850)
_c_(120855, _n_(120853, "print", lambda: print), 'Number of even numbers :', _n_(120854, "count_even", lambda: count_even))
_l_(120856)
_c_(120859, _n_(120857, "print", lambda: print), 'Number of odd numbers :', _n_(120858, "count_odd", lambda: count_odd))
_l_(120860)