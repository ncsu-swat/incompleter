# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(10956)

except ImportError:
    pass
_c_(10958, _n_(10957, "print", lambda: print), 'Original list:')
_l_(10959)
_c_(10962, _n_(10960, "print", lambda: print), _n_(10961, "nums", lambda: nums))
_l_(10963)

def get_avg(x):
    _l_(10975)

    x = [_n_(10964, "i", lambda: i) for i in _n_(10965, "x", lambda: x) if _n_(10966, "i", lambda: i) is not None]
    _l_(10967)
    aux = _c_(10970, _n_(10968, "sum", lambda: sum), _n_(10969, "x", lambda: x), 0.0) / _c_(10973, _n_(10971, "len", lambda: len), _n_(10972, "x", lambda: x))
    _l_(10974)
    return aux
result = _c_(10982, _n_(10976, "map", lambda: map), _n_(10977, "get_avg", lambda: get_avg), _c_(10981, _a_(10979, _n_(10978, "it", lambda: it), "zip_longest"), *_n_(10980, "nums", lambda: nums)))
_l_(10983)
_c_(10985, _n_(10984, "print", lambda: print), '\nAverage of n-th elements in the said list of lists with different lengths:')
_l_(10986)
_c_(10991, _n_(10987, "print", lambda: print), _c_(10990, _n_(10988, "list", lambda: list), _n_(10989, "result", lambda: result)))
_l_(10992)