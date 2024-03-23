# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(94063)

    ctr = 0
    _l_(94052)
    for digit in _n_(94053, "lst", lambda: lst):
        _l_(94060)

        if _n_(94054, "previous_digit", lambda: previous_digit) == 0 and _n_(94055, "digit", lambda: digit) != 0:
            _l_(94057)

            ctr += 1
            _l_(94056)
        previous_digit = _n_(94058, "digit", lambda: digit)
        _l_(94059)
    aux = _n_(94061, "ctr", lambda: ctr)
    _l_(94062)
    return aux
nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
_l_(94064)
_c_(94066, _n_(94065, "print", lambda: print), '\nOriginal list:')
_l_(94067)
_c_(94070, _n_(94068, "print", lambda: print), _n_(94069, "nums", lambda: nums))
_l_(94071)
_c_(94073, _n_(94072, "print", lambda: print), '\nNumber of groups of non-zero numbers separated by zeros of the said list:')
_l_(94074)
_c_(94079, _n_(94075, "print", lambda: print), _c_(94078, _n_(94076, "test", lambda: test), _n_(94077, "nums", lambda: nums)))
_l_(94080)