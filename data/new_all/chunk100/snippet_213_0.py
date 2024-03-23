# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def tuple_max_val(nums):
    _l_(16766)

    result_max = _c_(16761, _n_(16755, "max", lambda: max), [_c_(16759, _n_(16756, "abs", lambda: abs), _n_(16757, "x", lambda: x) * _n_(16758, "y", lambda: y)) for (x, y) in _n_(16760, "nums", lambda: nums)])
    _l_(16762)
    aux = (_n_(16763, "result_max", lambda: result_max), _n_(16764, "result_min", lambda: result_min))
    _l_(16765)
    return aux
nums = [(2, 7), (2, 6), (1, 8), (4, 9)]
_l_(16767)
_c_(16769, _n_(16768, "print", lambda: print), 'The original list, tuple : ')
_l_(16770)
_c_(16773, _n_(16771, "print", lambda: print), _n_(16772, "nums", lambda: nums))
_l_(16774)
_c_(16776, _n_(16775, "print", lambda: print), '\nMaximum and minimum product from the pairs of the said tuple of list:')
_l_(16777)
_c_(16782, _n_(16778, "print", lambda: print), _c_(16781, _n_(16779, "tuple_max_val", lambda: tuple_max_val), _n_(16780, "nums", lambda: nums)))
_l_(16783)