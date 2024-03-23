# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(30955)

except ImportError:
    pass

def drop_while(nums):
    _l_(30962)

    aux = _c_(30960, _a_(30957, _n_(30956, "it", lambda: it), "dropwhile"), lambda x: _n_(30958, "x", lambda: x) < 0, _n_(30959, "nums", lambda: nums))
    _l_(30961)
    return aux
nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
_l_(30963)
_c_(30966, _n_(30964, "print", lambda: print), 'Original list: ', _n_(30965, "nums", lambda: nums))
_l_(30967)
result = _c_(30970, _n_(30968, "drop_while", lambda: drop_while), _n_(30969, "nums", lambda: nums))
_l_(30971)
_c_(30976, _n_(30972, "print", lambda: print), 'Drops elements from the iterable when a positive number arises \n', _c_(30975, _n_(30973, "list", lambda: list), _n_(30974, "result", lambda: result)))
_l_(30977)

def negative_num(x):
    _l_(30980)

    aux = _n_(30978, "x", lambda: x) < 0
    _l_(30979)
    return aux

def drop_while(nums):
    _l_(30987)

    aux = _c_(30985, _a_(30982, _n_(30981, "it", lambda: it), "dropwhile"), _n_(30983, "negative_num", lambda: negative_num), _n_(30984, "nums", lambda: nums))
    _l_(30986)
    return aux
_c_(30990, _n_(30988, "print", lambda: print), 'Original list: ', _n_(30989, "nums", lambda: nums))
_l_(30991)
result = _c_(30994, _n_(30992, "drop_while", lambda: drop_while), _n_(30993, "nums", lambda: nums))
_l_(30995)
_c_(31000, _n_(30996, "print", lambda: print), 'Drops elements from the iterable when a positive number arises \n', _c_(30999, _n_(30997, "list", lambda: list), _n_(30998, "result", lambda: result)))
_l_(31001)