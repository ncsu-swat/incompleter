# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(10994)

except ImportError:
    pass
nums = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
_l_(10995)
_c_(10997, _n_(10996, "print", lambda: print), 'Original list:')
_l_(10998)
_c_(11001, _n_(10999, "print", lambda: print), _n_(11000, "nums", lambda: nums))
_l_(11002)

def get_avg(x):
    _l_(11010)

    aux = _c_(11005, _n_(11003, "sum", lambda: sum), _n_(11004, "x", lambda: x), 0.0) / _c_(11008, _n_(11006, "len", lambda: len), _n_(11007, "x", lambda: x))
    _l_(11009)
    return aux
result = _c_(11017, _n_(11011, "map", lambda: map), _n_(11012, "get_avg", lambda: get_avg), _c_(11016, _a_(11014, _n_(11013, "it", lambda: it), "zip_longest"), *_n_(11015, "nums", lambda: nums)))
_l_(11018)
_c_(11020, _n_(11019, "print", lambda: print), '\nAverage of n-th elements in the said list of lists with different lengths:')
_l_(11021)
_c_(11026, _n_(11022, "print", lambda: print), _c_(11025, _n_(11023, "list", lambda: list), _n_(11024, "result", lambda: result)))
_l_(11027)