# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(30910)

except ImportError:
    pass

def drop_while(nums):
    _l_(30917)

    aux = _c_(30915, _a_(30912, _n_(30911, "it", lambda: it), "dropwhile"), lambda x: _n_(30913, "x", lambda: x) < 0, _n_(30914, "nums", lambda: nums))
    _l_(30916)
    return aux
nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
_l_(30918)
_c_(30921, _n_(30919, "print", lambda: print), 'Original list: ', _n_(30920, "nums", lambda: nums))
_l_(30922)
_c_(30927, _n_(30923, "print", lambda: print), 'Drops elements from the iterable when a positive number arises \n', _c_(30926, _n_(30924, "list", lambda: list), _n_(30925, "result", lambda: result)))
_l_(30928)

def negative_num(x):
    _l_(30931)

    aux = _n_(30929, "x", lambda: x) < 0
    _l_(30930)
    return aux

def drop_while(nums):
    _l_(30938)

    aux = _c_(30936, _a_(30933, _n_(30932, "it", lambda: it), "dropwhile"), _n_(30934, "negative_num", lambda: negative_num), _n_(30935, "nums", lambda: nums))
    _l_(30937)
    return aux
nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
_l_(30939)
_c_(30942, _n_(30940, "print", lambda: print), 'Original list: ', _n_(30941, "nums", lambda: nums))
_l_(30943)
result = _c_(30946, _n_(30944, "drop_while", lambda: drop_while), _n_(30945, "nums", lambda: nums))
_l_(30947)
_c_(30952, _n_(30948, "print", lambda: print), 'Drops elements from the iterable when a positive number arises \n', _c_(30951, _n_(30949, "list", lambda: list), _n_(30950, "result", lambda: result)))
_l_(30953)