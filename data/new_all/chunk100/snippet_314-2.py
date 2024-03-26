# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(110098)

except ImportError:
    pass

def plusMinus(nums):
    _l_(110126)

    n = _c_(110101, _n_(110099, "len", lambda: len), _n_(110100, "nums", lambda: nums))
    _l_(110102)
    n1 = n2 = n3 = 0
    _l_(110103)
    for x in _n_(110104, "nums", lambda: nums):
        _l_(110112)

        if _n_(110105, "x", lambda: x) > 0:
            _l_(110111)

            n1 += 1
            _l_(110106)
        elif _n_(110107, "x", lambda: x) < 0:
            _l_(110110)

            n2 += 1
            _l_(110108)
        else:
            n3 += 1
            _l_(110109)
    aux = (_c_(110116, _n_(110113, "round", lambda: round), _n_(110114, "n1", lambda: n1) / _n_(110115, "n", lambda: n), 2), _c_(110120, _n_(110117, "round", lambda: round), _n_(110118, "n2", lambda: n2) / _n_(110119, "n", lambda: n), 2), _c_(110124, _n_(110121, "round", lambda: round), _n_(110122, "n3", lambda: n3) / _n_(110123, "n", lambda: n), 2))
    _l_(110125)
    return aux
nums = _c_(110128, _n_(110127, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(110129)
_c_(110132, _n_(110130, "print", lambda: print), 'Original array:', _n_(110131, "nums", lambda: nums))
_l_(110133)
nums_arr = _c_(110139, _n_(110134, "list", lambda: list), _c_(110138, _n_(110135, "map", lambda: map), _n_(110136, "int", lambda: int), _n_(110137, "nums", lambda: nums)))
_l_(110140)
_c_(110142, _n_(110141, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(110143)
_c_(110146, _n_(110144, "print", lambda: print), _n_(110145, "result", lambda: result))
_l_(110147)
nums = _c_(110149, _n_(110148, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(110150)
_c_(110153, _n_(110151, "print", lambda: print), '\nOriginal array:', _n_(110152, "nums", lambda: nums))
_l_(110154)
nums_arr = _c_(110160, _n_(110155, "list", lambda: list), _c_(110159, _n_(110156, "map", lambda: map), _n_(110157, "int", lambda: int), _n_(110158, "nums", lambda: nums)))
_l_(110161)
result = _c_(110164, _n_(110162, "plusMinus", lambda: plusMinus), _n_(110163, "nums_arr", lambda: nums_arr))
_l_(110165)
_c_(110167, _n_(110166, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(110168)
_c_(110171, _n_(110169, "print", lambda: print), _n_(110170, "result", lambda: result))
_l_(110172)