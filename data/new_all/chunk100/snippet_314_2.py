# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(29681)

except ImportError:
    pass

def plusMinus(nums):
    _l_(29709)

    n = _c_(29684, _n_(29682, "len", lambda: len), _n_(29683, "nums", lambda: nums))
    _l_(29685)
    n1 = n2 = n3 = 0
    _l_(29686)
    for x in _n_(29687, "nums", lambda: nums):
        _l_(29695)

        if _n_(29688, "x", lambda: x) > 0:
            _l_(29694)

            n1 += 1
            _l_(29689)
        elif _n_(29690, "x", lambda: x) < 0:
            _l_(29693)

            n2 += 1
            _l_(29691)
        else:
            n3 += 1
            _l_(29692)
    aux = (_c_(29699, _n_(29696, "round", lambda: round), _n_(29697, "n1", lambda: n1) / _n_(29698, "n", lambda: n), 2), _c_(29703, _n_(29700, "round", lambda: round), _n_(29701, "n2", lambda: n2) / _n_(29702, "n", lambda: n), 2), _c_(29707, _n_(29704, "round", lambda: round), _n_(29705, "n3", lambda: n3) / _n_(29706, "n", lambda: n), 2))
    _l_(29708)
    return aux
nums = _c_(29711, _n_(29710, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(29712)
_c_(29715, _n_(29713, "print", lambda: print), 'Original array:', _n_(29714, "nums", lambda: nums))
_l_(29716)
nums_arr = _c_(29722, _n_(29717, "list", lambda: list), _c_(29721, _n_(29718, "map", lambda: map), _n_(29719, "int", lambda: int), _n_(29720, "nums", lambda: nums)))
_l_(29723)
_c_(29725, _n_(29724, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29726)
_c_(29729, _n_(29727, "print", lambda: print), _n_(29728, "result", lambda: result))
_l_(29730)
nums = _c_(29732, _n_(29731, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(29733)
_c_(29736, _n_(29734, "print", lambda: print), '\nOriginal array:', _n_(29735, "nums", lambda: nums))
_l_(29737)
nums_arr = _c_(29743, _n_(29738, "list", lambda: list), _c_(29742, _n_(29739, "map", lambda: map), _n_(29740, "int", lambda: int), _n_(29741, "nums", lambda: nums)))
_l_(29744)
result = _c_(29747, _n_(29745, "plusMinus", lambda: plusMinus), _n_(29746, "nums_arr", lambda: nums_arr))
_l_(29748)
_c_(29750, _n_(29749, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29751)
_c_(29754, _n_(29752, "print", lambda: print), _n_(29753, "result", lambda: result))
_l_(29755)