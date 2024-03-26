# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(109948)

except ImportError:
    pass

def plusMinus(nums):
    _l_(109976)

    n = _c_(109951, _n_(109949, "len", lambda: len), _n_(109950, "nums", lambda: nums))
    _l_(109952)
    n1 = n2 = n3 = 0
    _l_(109953)
    for x in _n_(109954, "nums", lambda: nums):
        _l_(109962)

        if _n_(109955, "x", lambda: x) > 0:
            _l_(109961)

            n1 += 1
            _l_(109956)
        elif _n_(109957, "x", lambda: x) < 0:
            _l_(109960)

            n2 += 1
            _l_(109958)
        else:
            n3 += 1
            _l_(109959)
    aux = (_c_(109966, _n_(109963, "round", lambda: round), _n_(109964, "n1", lambda: n1) / _n_(109965, "n", lambda: n), 2), _c_(109970, _n_(109967, "round", lambda: round), _n_(109968, "n2", lambda: n2) / _n_(109969, "n", lambda: n), 2), _c_(109974, _n_(109971, "round", lambda: round), _n_(109972, "n3", lambda: n3) / _n_(109973, "n", lambda: n), 2))
    _l_(109975)
    return aux
nums = _c_(109978, _n_(109977, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(109979)
_c_(109982, _n_(109980, "print", lambda: print), 'Original array:', _n_(109981, "nums", lambda: nums))
_l_(109983)
result = _c_(109986, _n_(109984, "plusMinus", lambda: plusMinus), _n_(109985, "nums_arr", lambda: nums_arr))
_l_(109987)
_c_(109989, _n_(109988, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(109990)
_c_(109993, _n_(109991, "print", lambda: print), _n_(109992, "result", lambda: result))
_l_(109994)
nums = _c_(109996, _n_(109995, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(109997)
_c_(110000, _n_(109998, "print", lambda: print), '\nOriginal array:', _n_(109999, "nums", lambda: nums))
_l_(110001)
nums_arr = _c_(110007, _n_(110002, "list", lambda: list), _c_(110006, _n_(110003, "map", lambda: map), _n_(110004, "int", lambda: int), _n_(110005, "nums", lambda: nums)))
_l_(110008)
result = _c_(110011, _n_(110009, "plusMinus", lambda: plusMinus), _n_(110010, "nums_arr", lambda: nums_arr))
_l_(110012)
_c_(110014, _n_(110013, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(110015)
_c_(110018, _n_(110016, "print", lambda: print), _n_(110017, "result", lambda: result))
_l_(110019)