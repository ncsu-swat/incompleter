# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(29604)

except ImportError:
    pass

def plusMinus(nums):
    _l_(29632)

    n = _c_(29607, _n_(29605, "len", lambda: len), _n_(29606, "nums", lambda: nums))
    _l_(29608)
    n1 = n2 = n3 = 0
    _l_(29609)
    for x in _n_(29610, "nums", lambda: nums):
        _l_(29618)

        if _n_(29611, "x", lambda: x) > 0:
            _l_(29617)

            n1 += 1
            _l_(29612)
        elif _n_(29613, "x", lambda: x) < 0:
            _l_(29616)

            n2 += 1
            _l_(29614)
        else:
            n3 += 1
            _l_(29615)
    aux = (_c_(29622, _n_(29619, "round", lambda: round), _n_(29620, "n1", lambda: n1) / _n_(29621, "n", lambda: n), 2), _c_(29626, _n_(29623, "round", lambda: round), _n_(29624, "n2", lambda: n2) / _n_(29625, "n", lambda: n), 2), _c_(29630, _n_(29627, "round", lambda: round), _n_(29628, "n3", lambda: n3) / _n_(29629, "n", lambda: n), 2))
    _l_(29631)
    return aux
nums = _c_(29634, _n_(29633, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(29635)
_c_(29638, _n_(29636, "print", lambda: print), 'Original array:', _n_(29637, "nums", lambda: nums))
_l_(29639)
nums_arr = _c_(29645, _n_(29640, "list", lambda: list), _c_(29644, _n_(29641, "map", lambda: map), _n_(29642, "int", lambda: int), _n_(29643, "nums", lambda: nums)))
_l_(29646)
result = _c_(29649, _n_(29647, "plusMinus", lambda: plusMinus), _n_(29648, "nums_arr", lambda: nums_arr))
_l_(29650)
_c_(29652, _n_(29651, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29653)
_c_(29656, _n_(29654, "print", lambda: print), _n_(29655, "result", lambda: result))
_l_(29657)
_c_(29660, _n_(29658, "print", lambda: print), '\nOriginal array:', _n_(29659, "nums", lambda: nums))
_l_(29661)
nums_arr = _c_(29667, _n_(29662, "list", lambda: list), _c_(29666, _n_(29663, "map", lambda: map), _n_(29664, "int", lambda: int), _n_(29665, "nums", lambda: nums)))
_l_(29668)
result = _c_(29671, _n_(29669, "plusMinus", lambda: plusMinus), _n_(29670, "nums_arr", lambda: nums_arr))
_l_(29672)
_c_(29674, _n_(29673, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29675)
_c_(29678, _n_(29676, "print", lambda: print), _n_(29677, "result", lambda: result))
_l_(29679)