# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(48645)

except ImportError:
    pass

def array_sum(nums_arr):
    _l_(48653)

    sum_n = 0
    _l_(48646)
    for n in _n_(48647, "nums_arr", lambda: nums_arr):
        _l_(48650)

        sum_n += _n_(48648, "n", lambda: n)
        _l_(48649)
    aux = _n_(48651, "sum_n", lambda: sum_n)
    _l_(48652)
    return aux
nums = _c_(48655, _n_(48654, "array", lambda: array), 'i', [1, 2, 3, 4, 5, -15])
_l_(48656)
_c_(48659, _n_(48657, "print", lambda: print), 'Original array:', _n_(48658, "nums", lambda: nums))
_l_(48660)
nums_arr = _c_(48666, _n_(48661, "list", lambda: list), _c_(48665, _n_(48662, "map", lambda: map), _n_(48663, "int", lambda: int), _n_(48664, "nums", lambda: nums)))
_l_(48667)
_c_(48669, _n_(48668, "print", lambda: print), 'Sum of all elements of the said array:')
_l_(48670)
_c_(48673, _n_(48671, "print", lambda: print), _n_(48672, "result", lambda: result))
_l_(48674)