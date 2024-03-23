# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(30817)

except ImportError:
    pass

def drop_while(nums):
    _l_(30824)

    aux = _c_(30822, _a_(30819, _n_(30818, "it", lambda: it), "dropwhile"), lambda x: _n_(30820, "x", lambda: x) < 0, _n_(30821, "nums", lambda: nums))
    _l_(30823)
    return aux
_c_(30827, _n_(30825, "print", lambda: print), 'Original list: ', _n_(30826, "nums", lambda: nums))
_l_(30828)
result = _c_(30831, _n_(30829, "drop_while", lambda: drop_while), _n_(30830, "nums", lambda: nums))
_l_(30832)
_c_(30837, _n_(30833, "print", lambda: print), 'Drops elements from the iterable when a positive number arises \n', _c_(30836, _n_(30834, "list", lambda: list), _n_(30835, "result", lambda: result)))
_l_(30838)

def negative_num(x):
    _l_(30841)

    aux = _n_(30839, "x", lambda: x) < 0
    _l_(30840)
    return aux

def drop_while(nums):
    _l_(30848)

    aux = _c_(30846, _a_(30843, _n_(30842, "it", lambda: it), "dropwhile"), _n_(30844, "negative_num", lambda: negative_num), _n_(30845, "nums", lambda: nums))
    _l_(30847)
    return aux
nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
_l_(30849)
_c_(30852, _n_(30850, "print", lambda: print), 'Original list: ', _n_(30851, "nums", lambda: nums))
_l_(30853)
result = _c_(30856, _n_(30854, "drop_while", lambda: drop_while), _n_(30855, "nums", lambda: nums))
_l_(30857)
_c_(30862, _n_(30858, "print", lambda: print), 'Drops elements from the iterable when a positive number arises \n', _c_(30861, _n_(30859, "list", lambda: list), _n_(30860, "result", lambda: result)))
_l_(30863)