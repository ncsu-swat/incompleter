# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count_odd = 0
_l_(84448)
count_even = 0
_l_(84449)
for x in _n_(84450, "numbers", lambda: numbers):
    _l_(84455)

    if not _n_(84451, "x", lambda: x) % 2:
        _l_(84454)

        count_even += 1
        _l_(84452)
    else:
        count_odd += 1
        _l_(84453)
_c_(84458, _n_(84456, "print", lambda: print), 'Number of even numbers :', _n_(84457, "count_even", lambda: count_even))
_l_(84459)
_c_(84462, _n_(84460, "print", lambda: print), 'Number of odd numbers :', _n_(84461, "count_odd", lambda: count_odd))
_l_(84463)