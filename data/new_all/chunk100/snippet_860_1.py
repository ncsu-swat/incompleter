# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_Range_list(nums, m, n):
    _l_(84905)

    for i in _c_(84898, _n_(84895, "range", lambda: range), _n_(84896, "m", lambda: m), _n_(84897, "n", lambda: n) + 1, 1):
        _l_(84902)

        sum_range += _n_(84899, "nums", lambda: nums)[_n_(84900, "i", lambda: i)]
        _l_(84901)
    aux = _n_(84903, "sum_range", lambda: sum_range)
    _l_(84904)
    return aux
nums = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
_l_(84906)
_c_(84908, _n_(84907, "print", lambda: print), 'Original list:')
_l_(84909)
_c_(84912, _n_(84910, "print", lambda: print), _n_(84911, "nums", lambda: nums))
_l_(84913)
m = 8
_l_(84914)
n = 10
_l_(84915)
_c_(84919, _n_(84916, "print", lambda: print), 'Range:', _n_(84917, "m", lambda: m), ',', _n_(84918, "n", lambda: n))
_l_(84920)
_c_(84922, _n_(84921, "print", lambda: print), '\nSum of the specified range:')
_l_(84923)
_c_(84930, _n_(84924, "print", lambda: print), _c_(84929, _n_(84925, "sum_Range_list", lambda: sum_Range_list), _n_(84926, "nums", lambda: nums), _n_(84927, "m", lambda: m), _n_(84928, "n", lambda: n)))
_l_(84931)