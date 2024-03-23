# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_Range_list(nums, m, n):
    _l_(84869)

    sum_range = 0
    _l_(84858)
    for i in _c_(84862, _n_(84859, "range", lambda: range), _n_(84860, "m", lambda: m), _n_(84861, "n", lambda: n) + 1, 1):
        _l_(84866)

        sum_range += _n_(84863, "nums", lambda: nums)[_n_(84864, "i", lambda: i)]
        _l_(84865)
    aux = _n_(84867, "sum_range", lambda: sum_range)
    _l_(84868)
    return aux
_c_(84871, _n_(84870, "print", lambda: print), 'Original list:')
_l_(84872)
_c_(84875, _n_(84873, "print", lambda: print), _n_(84874, "nums", lambda: nums))
_l_(84876)
m = 8
_l_(84877)
n = 10
_l_(84878)
_c_(84882, _n_(84879, "print", lambda: print), 'Range:', _n_(84880, "m", lambda: m), ',', _n_(84881, "n", lambda: n))
_l_(84883)
_c_(84885, _n_(84884, "print", lambda: print), '\nSum of the specified range:')
_l_(84886)
_c_(84893, _n_(84887, "print", lambda: print), _c_(84892, _n_(84888, "sum_Range_list", lambda: sum_Range_list), _n_(84889, "nums", lambda: nums), _n_(84890, "m", lambda: m), _n_(84891, "n", lambda: n)))
_l_(84894)