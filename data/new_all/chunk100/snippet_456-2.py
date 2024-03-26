# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(117088)

except ImportError:
    pass

def array_sum(nums_arr):
    _l_(117096)

    sum_n = 0
    _l_(117089)
    for n in _n_(117090, "nums_arr", lambda: nums_arr):
        _l_(117093)

        sum_n += _n_(117091, "n", lambda: n)
        _l_(117092)
    aux = _n_(117094, "sum_n", lambda: sum_n)
    _l_(117095)
    return aux
nums = _c_(117098, _n_(117097, "array", lambda: array), 'i', [1, 2, 3, 4, 5, -15])
_l_(117099)
_c_(117102, _n_(117100, "print", lambda: print), 'Original array:', _n_(117101, "nums", lambda: nums))
_l_(117103)
nums_arr = _c_(117109, _n_(117104, "list", lambda: list), _c_(117108, _n_(117105, "map", lambda: map), _n_(117106, "int", lambda: int), _n_(117107, "nums", lambda: nums)))
_l_(117110)
_c_(117112, _n_(117111, "print", lambda: print), 'Sum of all elements of the said array:')
_l_(117113)
_c_(117116, _n_(117114, "print", lambda: print), _n_(117115, "result", lambda: result))
_l_(117117)