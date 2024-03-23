# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(30058)

except ImportError:
    pass

def plusMinus(nums):
    _l_(30082)

    n1 = n2 = n3 = 0
    _l_(30059)
    for x in _n_(30060, "nums", lambda: nums):
        _l_(30068)

        if _n_(30061, "x", lambda: x) > 0:
            _l_(30067)

            n1 += 1
            _l_(30062)
        elif _n_(30063, "x", lambda: x) < 0:
            _l_(30066)

            n2 += 1
            _l_(30064)
        else:
            n3 += 1
            _l_(30065)
    aux = (_c_(30072, _n_(30069, "round", lambda: round), _n_(30070, "n1", lambda: n1) / _n_(30071, "n", lambda: n), 2), _c_(30076, _n_(30073, "round", lambda: round), _n_(30074, "n2", lambda: n2) / _n_(30075, "n", lambda: n), 2), _c_(30080, _n_(30077, "round", lambda: round), _n_(30078, "n3", lambda: n3) / _n_(30079, "n", lambda: n), 2))
    _l_(30081)
    return aux
nums = _c_(30084, _n_(30083, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(30085)
_c_(30088, _n_(30086, "print", lambda: print), 'Original array:', _n_(30087, "nums", lambda: nums))
_l_(30089)
nums_arr = _c_(30095, _n_(30090, "list", lambda: list), _c_(30094, _n_(30091, "map", lambda: map), _n_(30092, "int", lambda: int), _n_(30093, "nums", lambda: nums)))
_l_(30096)
result = _c_(30099, _n_(30097, "plusMinus", lambda: plusMinus), _n_(30098, "nums_arr", lambda: nums_arr))
_l_(30100)
_c_(30102, _n_(30101, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(30103)
_c_(30106, _n_(30104, "print", lambda: print), _n_(30105, "result", lambda: result))
_l_(30107)
nums = _c_(30109, _n_(30108, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(30110)
_c_(30113, _n_(30111, "print", lambda: print), '\nOriginal array:', _n_(30112, "nums", lambda: nums))
_l_(30114)
nums_arr = _c_(30120, _n_(30115, "list", lambda: list), _c_(30119, _n_(30116, "map", lambda: map), _n_(30117, "int", lambda: int), _n_(30118, "nums", lambda: nums)))
_l_(30121)
result = _c_(30124, _n_(30122, "plusMinus", lambda: plusMinus), _n_(30123, "nums_arr", lambda: nums_arr))
_l_(30125)
_c_(30127, _n_(30126, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(30128)
_c_(30131, _n_(30129, "print", lambda: print), _n_(30130, "result", lambda: result))
_l_(30132)