# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_Range_list(nums, m, n):
    _l_(84980)

    sum_range = 0
    _l_(84969)
    for i in _c_(84973, _n_(84970, "range", lambda: range), _n_(84971, "m", lambda: m), _n_(84972, "n", lambda: n) + 1, 1):
        _l_(84977)

        sum_range += _n_(84974, "nums", lambda: nums)[_n_(84975, "i", lambda: i)]
        _l_(84976)
    aux = _n_(84978, "sum_range", lambda: sum_range)
    _l_(84979)
    return aux
nums = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
_l_(84981)
_c_(84983, _n_(84982, "print", lambda: print), 'Original list:')
_l_(84984)
_c_(84987, _n_(84985, "print", lambda: print), _n_(84986, "nums", lambda: nums))
_l_(84988)
m = 8
_l_(84989)
_c_(84993, _n_(84990, "print", lambda: print), 'Range:', _n_(84991, "m", lambda: m), ',', _n_(84992, "n", lambda: n))
_l_(84994)
_c_(84996, _n_(84995, "print", lambda: print), '\nSum of the specified range:')
_l_(84997)
_c_(85004, _n_(84998, "print", lambda: print), _c_(85003, _n_(84999, "sum_Range_list", lambda: sum_Range_list), _n_(85000, "nums", lambda: nums), _n_(85001, "m", lambda: m), _n_(85002, "n", lambda: n)))
_l_(85005)