# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(29836)

except ImportError:
    pass

def plusMinus(nums):
    _l_(29864)

    n = _c_(29839, _n_(29837, "len", lambda: len), _n_(29838, "nums", lambda: nums))
    _l_(29840)
    n1 = n2 = n3 = 0
    _l_(29841)
    for x in _n_(29842, "nums", lambda: nums):
        _l_(29850)

        if _n_(29843, "x", lambda: x) > 0:
            _l_(29849)

            n1 += 1
            _l_(29844)
        elif _n_(29845, "x", lambda: x) < 0:
            _l_(29848)

            n2 += 1
            _l_(29846)
        else:
            n3 += 1
            _l_(29847)
    aux = (_c_(29854, _n_(29851, "round", lambda: round), _n_(29852, "n1", lambda: n1) / _n_(29853, "n", lambda: n), 2), _c_(29858, _n_(29855, "round", lambda: round), _n_(29856, "n2", lambda: n2) / _n_(29857, "n", lambda: n), 2), _c_(29862, _n_(29859, "round", lambda: round), _n_(29860, "n3", lambda: n3) / _n_(29861, "n", lambda: n), 2))
    _l_(29863)
    return aux
nums = _c_(29866, _n_(29865, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(29867)
_c_(29870, _n_(29868, "print", lambda: print), 'Original array:', _n_(29869, "nums", lambda: nums))
_l_(29871)
nums_arr = _c_(29877, _n_(29872, "list", lambda: list), _c_(29876, _n_(29873, "map", lambda: map), _n_(29874, "int", lambda: int), _n_(29875, "nums", lambda: nums)))
_l_(29878)
result = _c_(29881, _n_(29879, "plusMinus", lambda: plusMinus), _n_(29880, "nums_arr", lambda: nums_arr))
_l_(29882)
_c_(29884, _n_(29883, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29885)
_c_(29888, _n_(29886, "print", lambda: print), _n_(29887, "result", lambda: result))
_l_(29889)
nums = _c_(29891, _n_(29890, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(29892)
_c_(29895, _n_(29893, "print", lambda: print), '\nOriginal array:', _n_(29894, "nums", lambda: nums))
_l_(29896)
result = _c_(29899, _n_(29897, "plusMinus", lambda: plusMinus), _n_(29898, "nums_arr", lambda: nums_arr))
_l_(29900)
_c_(29902, _n_(29901, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(29903)
_c_(29906, _n_(29904, "print", lambda: print), _n_(29905, "result", lambda: result))
_l_(29907)