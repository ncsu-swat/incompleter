# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(102958)

except ImportError:
    pass
_c_(102960, _n_(102959, "print", lambda: print), 'Original list:')
_l_(102961)
_c_(102964, _n_(102962, "print", lambda: print), _n_(102963, "nums", lambda: nums))
_l_(102965)

def get_avg(x):
    _l_(102977)

    x = [_n_(102966, "i", lambda: i) for i in _n_(102967, "x", lambda: x) if _n_(102968, "i", lambda: i) is not None]
    _l_(102969)
    aux = _c_(102972, _n_(102970, "sum", lambda: sum), _n_(102971, "x", lambda: x), 0.0) / _c_(102975, _n_(102973, "len", lambda: len), _n_(102974, "x", lambda: x))
    _l_(102976)
    return aux
result = _c_(102984, _n_(102978, "map", lambda: map), _n_(102979, "get_avg", lambda: get_avg), _c_(102983, _a_(102981, _n_(102980, "it", lambda: it), "zip_longest"), *_n_(102982, "nums", lambda: nums)))
_l_(102985)
_c_(102987, _n_(102986, "print", lambda: print), '\nAverage of n-th elements in the said list of lists with different lengths:')
_l_(102988)
_c_(102993, _n_(102989, "print", lambda: print), _c_(102992, _n_(102990, "list", lambda: list), _n_(102991, "result", lambda: result)))
_l_(102994)