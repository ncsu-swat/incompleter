# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(30865)

except ImportError:
    pass

def drop_while(nums):
    _l_(30872)

    aux = _c_(30870, _a_(30867, _n_(30866, "it", lambda: it), "dropwhile"), lambda x: _n_(30868, "x", lambda: x) < 0, _n_(30869, "nums", lambda: nums))
    _l_(30871)
    return aux
nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
_l_(30873)
_c_(30876, _n_(30874, "print", lambda: print), 'Original list: ', _n_(30875, "nums", lambda: nums))
_l_(30877)
result = _c_(30880, _n_(30878, "drop_while", lambda: drop_while), _n_(30879, "nums", lambda: nums))
_l_(30881)
_c_(30886, _n_(30882, "print", lambda: print), 'Drops elements from the iterable when a positive number arises \n', _c_(30885, _n_(30883, "list", lambda: list), _n_(30884, "result", lambda: result)))
_l_(30887)

def negative_num(x):
    _l_(30890)

    aux = _n_(30888, "x", lambda: x) < 0
    _l_(30889)
    return aux

def drop_while(nums):
    _l_(30897)

    aux = _c_(30895, _a_(30892, _n_(30891, "it", lambda: it), "dropwhile"), _n_(30893, "negative_num", lambda: negative_num), _n_(30894, "nums", lambda: nums))
    _l_(30896)
    return aux
nums = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
_l_(30898)
_c_(30901, _n_(30899, "print", lambda: print), 'Original list: ', _n_(30900, "nums", lambda: nums))
_l_(30902)
_c_(30907, _n_(30903, "print", lambda: print), 'Drops elements from the iterable when a positive number arises \n', _c_(30906, _n_(30904, "list", lambda: list), _n_(30905, "result", lambda: result)))
_l_(30908)