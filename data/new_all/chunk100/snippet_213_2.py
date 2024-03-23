# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def tuple_max_val(nums):
    _l_(16831)

    result_min = _c_(16826, _n_(16820, "min", lambda: min), [_c_(16824, _n_(16821, "abs", lambda: abs), _n_(16822, "x", lambda: x) * _n_(16823, "y", lambda: y)) for (x, y) in _n_(16825, "nums", lambda: nums)])
    _l_(16827)
    aux = (_n_(16828, "result_max", lambda: result_max), _n_(16829, "result_min", lambda: result_min))
    _l_(16830)
    return aux
nums = [(2, 7), (2, 6), (1, 8), (4, 9)]
_l_(16832)
_c_(16834, _n_(16833, "print", lambda: print), 'The original list, tuple : ')
_l_(16835)
_c_(16838, _n_(16836, "print", lambda: print), _n_(16837, "nums", lambda: nums))
_l_(16839)
_c_(16841, _n_(16840, "print", lambda: print), '\nMaximum and minimum product from the pairs of the said tuple of list:')
_l_(16842)
_c_(16847, _n_(16843, "print", lambda: print), _c_(16846, _n_(16844, "tuple_max_val", lambda: tuple_max_val), _n_(16845, "nums", lambda: nums)))
_l_(16848)