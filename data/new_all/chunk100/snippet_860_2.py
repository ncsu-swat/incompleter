# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_Range_list(nums, m, n):
    _l_(84943)

    sum_range = 0
    _l_(84932)
    for i in _c_(84936, _n_(84933, "range", lambda: range), _n_(84934, "m", lambda: m), _n_(84935, "n", lambda: n) + 1, 1):
        _l_(84940)

        sum_range += _n_(84937, "nums", lambda: nums)[_n_(84938, "i", lambda: i)]
        _l_(84939)
    aux = _n_(84941, "sum_range", lambda: sum_range)
    _l_(84942)
    return aux
nums = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
_l_(84944)
_c_(84946, _n_(84945, "print", lambda: print), 'Original list:')
_l_(84947)
_c_(84950, _n_(84948, "print", lambda: print), _n_(84949, "nums", lambda: nums))
_l_(84951)
n = 10
_l_(84952)
_c_(84956, _n_(84953, "print", lambda: print), 'Range:', _n_(84954, "m", lambda: m), ',', _n_(84955, "n", lambda: n))
_l_(84957)
_c_(84959, _n_(84958, "print", lambda: print), '\nSum of the specified range:')
_l_(84960)
_c_(84967, _n_(84961, "print", lambda: print), _c_(84966, _n_(84962, "sum_Range_list", lambda: sum_Range_list), _n_(84963, "nums", lambda: nums), _n_(84964, "m", lambda: m), _n_(84965, "n", lambda: n)))
_l_(84968)