# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(52812)

except ImportError:
    pass

def sum_pairs_list(nums, n):
    _l_(52827)

    for (num2, num1) in _c_(52818, _n_(52813, "list", lambda: list), _c_(52817, _a_(52815, _n_(52814, "it", lambda: it), "combinations"), _n_(52816, "nums", lambda: nums)[::-1], 2))[::-1]:
        _l_(52826)

        if _n_(52819, "num2", lambda: num2) + _n_(52820, "num1", lambda: num1) == _n_(52821, "n", lambda: n):
            _l_(52825)

            aux = [_n_(52822, "num1", lambda: num1), _n_(52823, "num2", lambda: num2)]
            _l_(52824)
            return aux
n = 10
_l_(52828)
_c_(52832, _n_(52829, "print", lambda: print), 'Original list:', _n_(52830, "nums", lambda: nums), ': Given value:', _n_(52831, "n", lambda: n))
_l_(52833)
_c_(52840, _n_(52834, "print", lambda: print), 'Sum of pair equal to ', _n_(52835, "n", lambda: n), '=', _c_(52839, _n_(52836, "sum_pairs_list", lambda: sum_pairs_list), _n_(52837, "nums", lambda: nums), _n_(52838, "n", lambda: n)))
_l_(52841)
nums = [1, 2, -3, -4, -5, 6, -7]
_l_(52842)
n = -6
_l_(52843)
_c_(52847, _n_(52844, "print", lambda: print), 'Original list:', _n_(52845, "nums", lambda: nums), ': Given value:', _n_(52846, "n", lambda: n))
_l_(52848)
_c_(52855, _n_(52849, "print", lambda: print), 'Sum of pair equal to ', _n_(52850, "n", lambda: n), '=', _c_(52854, _n_(52851, "sum_pairs_list", lambda: sum_pairs_list), _n_(52852, "nums", lambda: nums), _n_(52853, "n", lambda: n)))
_l_(52856)