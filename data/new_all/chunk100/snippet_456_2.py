# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(48710)

except ImportError:
    pass

def array_sum(nums_arr):
    _l_(48718)

    sum_n = 0
    _l_(48711)
    for n in _n_(48712, "nums_arr", lambda: nums_arr):
        _l_(48715)

        sum_n += _n_(48713, "n", lambda: n)
        _l_(48714)
    aux = _n_(48716, "sum_n", lambda: sum_n)
    _l_(48717)
    return aux
_c_(48721, _n_(48719, "print", lambda: print), 'Original array:', _n_(48720, "nums", lambda: nums))
_l_(48722)
nums_arr = _c_(48728, _n_(48723, "list", lambda: list), _c_(48727, _n_(48724, "map", lambda: map), _n_(48725, "int", lambda: int), _n_(48726, "nums", lambda: nums)))
_l_(48729)
result = _c_(48732, _n_(48730, "array_sum", lambda: array_sum), _n_(48731, "nums_arr", lambda: nums_arr))
_l_(48733)
_c_(48735, _n_(48734, "print", lambda: print), 'Sum of all elements of the said array:')
_l_(48736)
_c_(48739, _n_(48737, "print", lambda: print), _n_(48738, "result", lambda: result))
_l_(48740)