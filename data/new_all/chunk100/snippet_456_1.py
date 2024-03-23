# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(48676)

except ImportError:
    pass

def array_sum(nums_arr):
    _l_(48683)

    for n in _n_(48677, "nums_arr", lambda: nums_arr):
        _l_(48680)

        sum_n += _n_(48678, "n", lambda: n)
        _l_(48679)
    aux = _n_(48681, "sum_n", lambda: sum_n)
    _l_(48682)
    return aux
nums = _c_(48685, _n_(48684, "array", lambda: array), 'i', [1, 2, 3, 4, 5, -15])
_l_(48686)
_c_(48689, _n_(48687, "print", lambda: print), 'Original array:', _n_(48688, "nums", lambda: nums))
_l_(48690)
nums_arr = _c_(48696, _n_(48691, "list", lambda: list), _c_(48695, _n_(48692, "map", lambda: map), _n_(48693, "int", lambda: int), _n_(48694, "nums", lambda: nums)))
_l_(48697)
result = _c_(48700, _n_(48698, "array_sum", lambda: array_sum), _n_(48699, "nums_arr", lambda: nums_arr))
_l_(48701)
_c_(48703, _n_(48702, "print", lambda: print), 'Sum of all elements of the said array:')
_l_(48704)
_c_(48707, _n_(48705, "print", lambda: print), _n_(48706, "result", lambda: result))
_l_(48708)