# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(110021)

except ImportError:
    pass

def plusMinus(nums):
    _l_(110049)

    n = _c_(110024, _n_(110022, "len", lambda: len), _n_(110023, "nums", lambda: nums))
    _l_(110025)
    n1 = n2 = n3 = 0
    _l_(110026)
    for x in _n_(110027, "nums", lambda: nums):
        _l_(110035)

        if _n_(110028, "x", lambda: x) > 0:
            _l_(110034)

            n1 += 1
            _l_(110029)
        elif _n_(110030, "x", lambda: x) < 0:
            _l_(110033)

            n2 += 1
            _l_(110031)
        else:
            n3 += 1
            _l_(110032)
    aux = (_c_(110039, _n_(110036, "round", lambda: round), _n_(110037, "n1", lambda: n1) / _n_(110038, "n", lambda: n), 2), _c_(110043, _n_(110040, "round", lambda: round), _n_(110041, "n2", lambda: n2) / _n_(110042, "n", lambda: n), 2), _c_(110047, _n_(110044, "round", lambda: round), _n_(110045, "n3", lambda: n3) / _n_(110046, "n", lambda: n), 2))
    _l_(110048)
    return aux
_c_(110052, _n_(110050, "print", lambda: print), 'Original array:', _n_(110051, "nums", lambda: nums))
_l_(110053)
nums_arr = _c_(110059, _n_(110054, "list", lambda: list), _c_(110058, _n_(110055, "map", lambda: map), _n_(110056, "int", lambda: int), _n_(110057, "nums", lambda: nums)))
_l_(110060)
result = _c_(110063, _n_(110061, "plusMinus", lambda: plusMinus), _n_(110062, "nums_arr", lambda: nums_arr))
_l_(110064)
_c_(110066, _n_(110065, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(110067)
_c_(110070, _n_(110068, "print", lambda: print), _n_(110069, "result", lambda: result))
_l_(110071)
nums = _c_(110073, _n_(110072, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(110074)
_c_(110077, _n_(110075, "print", lambda: print), '\nOriginal array:', _n_(110076, "nums", lambda: nums))
_l_(110078)
nums_arr = _c_(110084, _n_(110079, "list", lambda: list), _c_(110083, _n_(110080, "map", lambda: map), _n_(110081, "int", lambda: int), _n_(110082, "nums", lambda: nums)))
_l_(110085)
result = _c_(110088, _n_(110086, "plusMinus", lambda: plusMinus), _n_(110087, "nums_arr", lambda: nums_arr))
_l_(110089)
_c_(110091, _n_(110090, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(110092)
_c_(110095, _n_(110093, "print", lambda: print), _n_(110094, "result", lambda: result))
_l_(110096)