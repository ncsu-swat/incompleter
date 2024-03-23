# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(29909)

except ImportError:
    pass

def plusMinus(nums):
    _l_(29937)

    n = _c_(29912, _n_(29910, "len", lambda: len), _n_(29911, "nums", lambda: nums))
    _l_(29913)
    n1 = n2 = n3 = 0
    _l_(29914)
    for x in _n_(29915, "nums", lambda: nums):
        _l_(29923)

        if _n_(29916, "x", lambda: x) > 0:
            _l_(29922)

            n1 += 1
            _l_(29917)
        elif _n_(29918, "x", lambda: x) < 0:
            _l_(29921)

            n2 += 1
            _l_(29919)
        else:
            n3 += 1
            _l_(29920)
    aux = (_c_(29927, _n_(29924, "round", lambda: round), _n_(29925, "n1", lambda: n1) / _n_(29926, "n", lambda: n), 2), _c_(29931, _n_(29928, "round", lambda: round), _n_(29929, "n2", lambda: n2) / _n_(29930, "n", lambda: n), 2), _c_(29935, _n_(29932, "round", lambda: round), _n_(29933, "n3", lambda: n3) / _n_(29934, "n", lambda: n), 2))
    _l_(29936)
    return aux
nums = _c_(29939, _n_(29938, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(29940)
_c_(29943, _n_(29941, "print", lambda: print), 'Original array:', _n_(29942, "nums", lambda: nums))
_l_(29944)
nums_arr = _c_(29950, _n_(29945, "list", lambda: list), _c_(29949, _n_(29946, "map", lambda: map), _n_(29947, "int", lambda: int), _n_(29948, "nums", lambda: nums)))
_l_(29951)
result = _c_(29954, _n_(29952, "plusMinus", lambda: plusMinus), _n_(29953, "nums_arr", lambda: nums_arr))
_l_(29955)
_c_(29957, _n_(29956, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29958)
_c_(29961, _n_(29959, "print", lambda: print), _n_(29960, "result", lambda: result))
_l_(29962)
nums = _c_(29964, _n_(29963, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(29965)
_c_(29968, _n_(29966, "print", lambda: print), '\nOriginal array:', _n_(29967, "nums", lambda: nums))
_l_(29969)
nums_arr = _c_(29975, _n_(29970, "list", lambda: list), _c_(29974, _n_(29971, "map", lambda: map), _n_(29972, "int", lambda: int), _n_(29973, "nums", lambda: nums)))
_l_(29976)
_c_(29978, _n_(29977, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29979)
_c_(29982, _n_(29980, "print", lambda: print), _n_(29981, "result", lambda: result))
_l_(29983)