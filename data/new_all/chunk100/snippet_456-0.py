# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(117028)

except ImportError:
    pass

def array_sum(nums_arr):
    _l_(117036)

    sum_n = 0
    _l_(117029)
    for n in _n_(117030, "nums_arr", lambda: nums_arr):
        _l_(117033)

        sum_n += _n_(117031, "n", lambda: n)
        _l_(117032)
    aux = _n_(117034, "sum_n", lambda: sum_n)
    _l_(117035)
    return aux
_c_(117039, _n_(117037, "print", lambda: print), 'Original array:', _n_(117038, "nums", lambda: nums))
_l_(117040)
nums_arr = _c_(117046, _n_(117041, "list", lambda: list), _c_(117045, _n_(117042, "map", lambda: map), _n_(117043, "int", lambda: int), _n_(117044, "nums", lambda: nums)))
_l_(117047)
result = _c_(117050, _n_(117048, "array_sum", lambda: array_sum), _n_(117049, "nums_arr", lambda: nums_arr))
_l_(117051)
_c_(117053, _n_(117052, "print", lambda: print), 'Sum of all elements of the said array:')
_l_(117054)
_c_(117057, _n_(117055, "print", lambda: print), _n_(117056, "result", lambda: result))
_l_(117058)