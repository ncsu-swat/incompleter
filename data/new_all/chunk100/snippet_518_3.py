# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(52950)

except ImportError:
    pass

def sum_pairs_list(nums, n):
    _l_(52965)

    for (num2, num1) in _c_(52956, _n_(52951, "list", lambda: list), _c_(52955, _a_(52953, _n_(52952, "it", lambda: it), "combinations"), _n_(52954, "nums", lambda: nums)[::-1], 2))[::-1]:
        _l_(52964)

        if _n_(52957, "num2", lambda: num2) + _n_(52958, "num1", lambda: num1) == _n_(52959, "n", lambda: n):
            _l_(52963)

            aux = [_n_(52960, "num1", lambda: num1), _n_(52961, "num2", lambda: num2)]
            _l_(52962)
            return aux
nums = [1, 2, 3, 4, 5, 6, 7]
_l_(52966)
n = 10
_l_(52967)
_c_(52971, _n_(52968, "print", lambda: print), 'Original list:', _n_(52969, "nums", lambda: nums), ': Given value:', _n_(52970, "n", lambda: n))
_l_(52972)
_c_(52979, _n_(52973, "print", lambda: print), 'Sum of pair equal to ', _n_(52974, "n", lambda: n), '=', _c_(52978, _n_(52975, "sum_pairs_list", lambda: sum_pairs_list), _n_(52976, "nums", lambda: nums), _n_(52977, "n", lambda: n)))
_l_(52980)
nums = [1, 2, -3, -4, -5, 6, -7]
_l_(52981)
_c_(52985, _n_(52982, "print", lambda: print), 'Original list:', _n_(52983, "nums", lambda: nums), ': Given value:', _n_(52984, "n", lambda: n))
_l_(52986)
_c_(52993, _n_(52987, "print", lambda: print), 'Sum of pair equal to ', _n_(52988, "n", lambda: n), '=', _c_(52992, _n_(52989, "sum_pairs_list", lambda: sum_pairs_list), _n_(52990, "nums", lambda: nums), _n_(52991, "n", lambda: n)))
_l_(52994)