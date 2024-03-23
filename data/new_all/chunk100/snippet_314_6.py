# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import array
    _l_(29985)

except ImportError:
    pass

def plusMinus(nums):
    _l_(30013)

    n = _c_(29988, _n_(29986, "len", lambda: len), _n_(29987, "nums", lambda: nums))
    _l_(29989)
    n1 = n2 = n3 = 0
    _l_(29990)
    for x in _n_(29991, "nums", lambda: nums):
        _l_(29999)

        if _n_(29992, "x", lambda: x) > 0:
            _l_(29998)

            n1 += 1
            _l_(29993)
        elif _n_(29994, "x", lambda: x) < 0:
            _l_(29997)

            n2 += 1
            _l_(29995)
        else:
            n3 += 1
            _l_(29996)
    aux = (_c_(30003, _n_(30000, "round", lambda: round), _n_(30001, "n1", lambda: n1) / _n_(30002, "n", lambda: n), 2), _c_(30007, _n_(30004, "round", lambda: round), _n_(30005, "n2", lambda: n2) / _n_(30006, "n", lambda: n), 2), _c_(30011, _n_(30008, "round", lambda: round), _n_(30009, "n3", lambda: n3) / _n_(30010, "n", lambda: n), 2))
    _l_(30012)
    return aux
nums = _c_(30015, _n_(30014, "array", lambda: array), 'i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
_l_(30016)
_c_(30019, _n_(30017, "print", lambda: print), 'Original array:', _n_(30018, "nums", lambda: nums))
_l_(30020)
result = _c_(30023, _n_(30021, "plusMinus", lambda: plusMinus), _n_(30022, "nums_arr", lambda: nums_arr))
_l_(30024)
_c_(30026, _n_(30025, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(30027)
_c_(30030, _n_(30028, "print", lambda: print), _n_(30029, "result", lambda: result))
_l_(30031)
nums = _c_(30033, _n_(30032, "array", lambda: array), 'i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
_l_(30034)
_c_(30037, _n_(30035, "print", lambda: print), '\nOriginal array:', _n_(30036, "nums", lambda: nums))
_l_(30038)
nums_arr = _c_(30044, _n_(30039, "list", lambda: list), _c_(30043, _n_(30040, "map", lambda: map), _n_(30041, "int", lambda: int), _n_(30042, "nums", lambda: nums)))
_l_(30045)
result = _c_(30048, _n_(30046, "plusMinus", lambda: plusMinus), _n_(30047, "nums_arr", lambda: nums_arr))
_l_(30049)
_c_(30051, _n_(30050, "print", lambda: print), 'Ratio of positive numbers, negative numbers and zeroes:')
_l_(30052)
_c_(30055, _n_(30053, "print", lambda: print), _n_(30054, "result", lambda: result))
_l_(30056)