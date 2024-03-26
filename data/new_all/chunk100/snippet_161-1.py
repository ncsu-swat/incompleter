# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(102996)

except ImportError:
    pass
nums = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
_l_(102997)
_c_(102999, _n_(102998, "print", lambda: print), 'Original list:')
_l_(103000)
_c_(103003, _n_(103001, "print", lambda: print), _n_(103002, "nums", lambda: nums))
_l_(103004)

def get_avg(x):
    _l_(103016)

    x = [_n_(103005, "i", lambda: i) for i in _n_(103006, "x", lambda: x) if _n_(103007, "i", lambda: i) is not None]
    _l_(103008)
    aux = _c_(103011, _n_(103009, "sum", lambda: sum), _n_(103010, "x", lambda: x), 0.0) / _c_(103014, _n_(103012, "len", lambda: len), _n_(103013, "x", lambda: x))
    _l_(103015)
    return aux
_c_(103018, _n_(103017, "print", lambda: print), '\nAverage of n-th elements in the said list of lists with different lengths:')
_l_(103019)
_c_(103024, _n_(103020, "print", lambda: print), _c_(103023, _n_(103021, "list", lambda: list), _n_(103022, "result", lambda: result)))
_l_(103025)