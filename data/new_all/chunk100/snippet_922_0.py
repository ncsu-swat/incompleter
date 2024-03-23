# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(93977)

    previous_digit = 0
    _l_(93966)
    for digit in _n_(93967, "lst", lambda: lst):
        _l_(93974)

        if _n_(93968, "previous_digit", lambda: previous_digit) == 0 and _n_(93969, "digit", lambda: digit) != 0:
            _l_(93971)

            ctr += 1
            _l_(93970)
        previous_digit = _n_(93972, "digit", lambda: digit)
        _l_(93973)
    aux = _n_(93975, "ctr", lambda: ctr)
    _l_(93976)
    return aux
nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
_l_(93978)
_c_(93980, _n_(93979, "print", lambda: print), '\nOriginal list:')
_l_(93981)
_c_(93984, _n_(93982, "print", lambda: print), _n_(93983, "nums", lambda: nums))
_l_(93985)
_c_(93987, _n_(93986, "print", lambda: print), '\nNumber of groups of non-zero numbers separated by zeros of the said list:')
_l_(93988)
_c_(93993, _n_(93989, "print", lambda: print), _c_(93992, _n_(93990, "test", lambda: test), _n_(93991, "nums", lambda: nums)))
_l_(93994)