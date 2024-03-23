# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(29757)

except ImportError:
    pass

def plusMinus(nums):
    _l_(29784)

    n = _c_(29760, _n_(29758, "len", lambda: len), _n_(29759, "nums", lambda: nums))
    _l_(29761)
    for x in _n_(29762, "nums", lambda: nums):
        _l_(29770)

        if _n_(29763, "x", lambda: x) > 0:
            _l_(29769)

            n1 += 1
            _l_(29764)
        elif _n_(29765, "x", lambda: x) < 0:
            _l_(29768)

            n2 += 1
            _l_(29766)
        else:
            n3 += 1
            _l_(29767)
    aux = (_c_(29774, _n_(29771, "round", lambda: round), _n_(29772, "n1", lambda: n1) / _n_(29773, "n", lambda: n), 2), _c_(29778, _n_(29775, "round", lambda: round), _n_(29776, "n2", lambda: n2) / _n_(29777, "n", lambda: n), 2), _c_(29782, _n_(29779, "round", lambda: round), _n_(29780, "n3", lambda: n3) / _n_(29781, "n", lambda: n), 2))
    _l_(29783)
    return aux
nums = _c_(29786, _n_(29785, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(29787)
_c_(29790, _n_(29788, "print", lambda: print), 'Original array:', _n_(29789, "nums", lambda: nums))
_l_(29791)
nums_arr = _c_(29797, _n_(29792, "list", lambda: list), _c_(29796, _n_(29793, "map", lambda: map), _n_(29794, "int", lambda: int), _n_(29795, "nums", lambda: nums)))
_l_(29798)
result = _c_(29801, _n_(29799, "plusMinus", lambda: plusMinus), _n_(29800, "nums_arr", lambda: nums_arr))
_l_(29802)
_c_(29804, _n_(29803, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29805)
_c_(29808, _n_(29806, "print", lambda: print), _n_(29807, "result", lambda: result))
_l_(29809)
nums = _c_(29811, _n_(29810, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(29812)
_c_(29815, _n_(29813, "print", lambda: print), '\nOriginal array:', _n_(29814, "nums", lambda: nums))
_l_(29816)
nums_arr = _c_(29822, _n_(29817, "list", lambda: list), _c_(29821, _n_(29818, "map", lambda: map), _n_(29819, "int", lambda: int), _n_(29820, "nums", lambda: nums)))
_l_(29823)
result = _c_(29826, _n_(29824, "plusMinus", lambda: plusMinus), _n_(29825, "nums_arr", lambda: nums_arr))
_l_(29827)
_c_(29829, _n_(29828, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29830)
_c_(29833, _n_(29831, "print", lambda: print), _n_(29832, "result", lambda: result))
_l_(29834)