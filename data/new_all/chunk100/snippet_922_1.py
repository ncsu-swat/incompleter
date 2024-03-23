# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(94005)

    previous_digit = 0
    _l_(93995)
    ctr = 0
    _l_(93996)
    for digit in _n_(93997, "lst", lambda: lst):
        _l_(94002)

        if _n_(93998, "previous_digit", lambda: previous_digit) == 0 and _n_(93999, "digit", lambda: digit) != 0:
            _l_(94001)

            ctr += 1
            _l_(94000)
    aux = _n_(94003, "ctr", lambda: ctr)
    _l_(94004)
    return aux
nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
_l_(94006)
_c_(94008, _n_(94007, "print", lambda: print), '\nOriginal list:')
_l_(94009)
_c_(94012, _n_(94010, "print", lambda: print), _n_(94011, "nums", lambda: nums))
_l_(94013)
_c_(94015, _n_(94014, "print", lambda: print), '\nNumber of groups of non-zero numbers separated by zeros of the said list:')
_l_(94016)
_c_(94021, _n_(94017, "print", lambda: print), _c_(94020, _n_(94018, "test", lambda: test), _n_(94019, "nums", lambda: nums)))
_l_(94022)