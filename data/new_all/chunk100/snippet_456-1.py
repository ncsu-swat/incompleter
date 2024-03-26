# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(117060)

except ImportError:
    pass

def array_sum(nums_arr):
    _l_(117068)

    sum_n = 0
    _l_(117061)
    for n in _n_(117062, "nums_arr", lambda: nums_arr):
        _l_(117065)

        sum_n += _n_(117063, "n", lambda: n)
        _l_(117064)
    aux = _n_(117066, "sum_n", lambda: sum_n)
    _l_(117067)
    return aux
nums = _c_(117070, _n_(117069, "array", lambda: array), 'i', [1, 2, 3, 4, 5, -15])
_l_(117071)
_c_(117074, _n_(117072, "print", lambda: print), 'Original array:', _n_(117073, "nums", lambda: nums))
_l_(117075)
result = _c_(117078, _n_(117076, "array_sum", lambda: array_sum), _n_(117077, "nums_arr", lambda: nums_arr))
_l_(117079)
_c_(117081, _n_(117080, "print", lambda: print), 'Sum of all elements of the said array:')
_l_(117082)
_c_(117085, _n_(117083, "print", lambda: print), _n_(117084, "result", lambda: result))
_l_(117086)