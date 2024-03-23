# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(52858)

except ImportError:
    pass

def sum_pairs_list(nums, n):
    _l_(52873)

    for (num2, num1) in _c_(52864, _n_(52859, "list", lambda: list), _c_(52863, _a_(52861, _n_(52860, "it", lambda: it), "combinations"), _n_(52862, "nums", lambda: nums)[::-1], 2))[::-1]:
        _l_(52872)

        if _n_(52865, "num2", lambda: num2) + _n_(52866, "num1", lambda: num1) == _n_(52867, "n", lambda: n):
            _l_(52871)

            aux = [_n_(52868, "num1", lambda: num1), _n_(52869, "num2", lambda: num2)]
            _l_(52870)
            return aux
nums = [1, 2, 3, 4, 5, 6, 7]
_l_(52874)
_c_(52878, _n_(52875, "print", lambda: print), 'Original list:', _n_(52876, "nums", lambda: nums), ': Given value:', _n_(52877, "n", lambda: n))
_l_(52879)
_c_(52886, _n_(52880, "print", lambda: print), 'Sum of pair equal to ', _n_(52881, "n", lambda: n), '=', _c_(52885, _n_(52882, "sum_pairs_list", lambda: sum_pairs_list), _n_(52883, "nums", lambda: nums), _n_(52884, "n", lambda: n)))
_l_(52887)
nums = [1, 2, -3, -4, -5, 6, -7]
_l_(52888)
n = -6
_l_(52889)
_c_(52893, _n_(52890, "print", lambda: print), 'Original list:', _n_(52891, "nums", lambda: nums), ': Given value:', _n_(52892, "n", lambda: n))
_l_(52894)
_c_(52901, _n_(52895, "print", lambda: print), 'Sum of pair equal to ', _n_(52896, "n", lambda: n), '=', _c_(52900, _n_(52897, "sum_pairs_list", lambda: sum_pairs_list), _n_(52898, "nums", lambda: nums), _n_(52899, "n", lambda: n)))
_l_(52902)