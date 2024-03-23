# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(94035)

    previous_digit = 0
    _l_(94023)
    ctr = 0
    _l_(94024)
    for digit in _n_(94025, "lst", lambda: lst):
        _l_(94032)

        if _n_(94026, "previous_digit", lambda: previous_digit) == 0 and _n_(94027, "digit", lambda: digit) != 0:
            _l_(94029)

            ctr += 1
            _l_(94028)
        previous_digit = _n_(94030, "digit", lambda: digit)
        _l_(94031)
    aux = _n_(94033, "ctr", lambda: ctr)
    _l_(94034)
    return aux
_c_(94037, _n_(94036, "print", lambda: print), '\nOriginal list:')
_l_(94038)
_c_(94041, _n_(94039, "print", lambda: print), _n_(94040, "nums", lambda: nums))
_l_(94042)
_c_(94044, _n_(94043, "print", lambda: print), '\nNumber of groups of non-zero numbers separated by zeros of the said list:')
_l_(94045)
_c_(94050, _n_(94046, "print", lambda: print), _c_(94049, _n_(94047, "test", lambda: test), _n_(94048, "nums", lambda: nums)))
_l_(94051)