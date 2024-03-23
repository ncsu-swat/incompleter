# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(48742)

except ImportError:
    pass

def array_sum(nums_arr):
    _l_(48750)

    sum_n = 0
    _l_(48743)
    for n in _n_(48744, "nums_arr", lambda: nums_arr):
        _l_(48747)

        sum_n += _n_(48745, "n", lambda: n)
        _l_(48746)
    aux = _n_(48748, "sum_n", lambda: sum_n)
    _l_(48749)
    return aux
nums = _c_(48752, _n_(48751, "array", lambda: array), 'i', [1, 2, 3, 4, 5, -15])
_l_(48753)
_c_(48756, _n_(48754, "print", lambda: print), 'Original array:', _n_(48755, "nums", lambda: nums))
_l_(48757)
result = _c_(48760, _n_(48758, "array_sum", lambda: array_sum), _n_(48759, "nums_arr", lambda: nums_arr))
_l_(48761)
_c_(48763, _n_(48762, "print", lambda: print), 'Sum of all elements of the said array:')
_l_(48764)
_c_(48767, _n_(48765, "print", lambda: print), _n_(48766, "result", lambda: result))
_l_(48768)