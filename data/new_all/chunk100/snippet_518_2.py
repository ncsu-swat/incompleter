# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(52904)

except ImportError:
    pass

def sum_pairs_list(nums, n):
    _l_(52919)

    for (num2, num1) in _c_(52910, _n_(52905, "list", lambda: list), _c_(52909, _a_(52907, _n_(52906, "it", lambda: it), "combinations"), _n_(52908, "nums", lambda: nums)[::-1], 2))[::-1]:
        _l_(52918)

        if _n_(52911, "num2", lambda: num2) + _n_(52912, "num1", lambda: num1) == _n_(52913, "n", lambda: n):
            _l_(52917)

            aux = [_n_(52914, "num1", lambda: num1), _n_(52915, "num2", lambda: num2)]
            _l_(52916)
            return aux
nums = [1, 2, 3, 4, 5, 6, 7]
_l_(52920)
n = 10
_l_(52921)
_c_(52925, _n_(52922, "print", lambda: print), 'Original list:', _n_(52923, "nums", lambda: nums), ': Given value:', _n_(52924, "n", lambda: n))
_l_(52926)
_c_(52933, _n_(52927, "print", lambda: print), 'Sum of pair equal to ', _n_(52928, "n", lambda: n), '=', _c_(52932, _n_(52929, "sum_pairs_list", lambda: sum_pairs_list), _n_(52930, "nums", lambda: nums), _n_(52931, "n", lambda: n)))
_l_(52934)
n = -6
_l_(52935)
_c_(52939, _n_(52936, "print", lambda: print), 'Original list:', _n_(52937, "nums", lambda: nums), ': Given value:', _n_(52938, "n", lambda: n))
_l_(52940)
_c_(52947, _n_(52941, "print", lambda: print), 'Sum of pair equal to ', _n_(52942, "n", lambda: n), '=', _c_(52946, _n_(52943, "sum_pairs_list", lambda: sum_pairs_list), _n_(52944, "nums", lambda: nums), _n_(52945, "n", lambda: n)))
_l_(52948)