# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def tuple_max_val(nums):
    _l_(16803)

    result_max = _c_(16790, _n_(16784, "max", lambda: max), [_c_(16788, _n_(16785, "abs", lambda: abs), _n_(16786, "x", lambda: x) * _n_(16787, "y", lambda: y)) for (x, y) in _n_(16789, "nums", lambda: nums)])
    _l_(16791)
    result_min = _c_(16798, _n_(16792, "min", lambda: min), [_c_(16796, _n_(16793, "abs", lambda: abs), _n_(16794, "x", lambda: x) * _n_(16795, "y", lambda: y)) for (x, y) in _n_(16797, "nums", lambda: nums)])
    _l_(16799)
    aux = (_n_(16800, "result_max", lambda: result_max), _n_(16801, "result_min", lambda: result_min))
    _l_(16802)
    return aux
_c_(16805, _n_(16804, "print", lambda: print), 'The original list, tuple : ')
_l_(16806)
_c_(16809, _n_(16807, "print", lambda: print), _n_(16808, "nums", lambda: nums))
_l_(16810)
_c_(16812, _n_(16811, "print", lambda: print), '\nMaximum and minimum product from the pairs of the said tuple of list:')
_l_(16813)
_c_(16818, _n_(16814, "print", lambda: print), _c_(16817, _n_(16815, "tuple_max_val", lambda: tuple_max_val), _n_(16816, "nums", lambda: nums)))
_l_(16819)