# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(25990)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(25992)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(26022)

    temp = (_c_(25995, _n_(25993, "set", lambda: set), _n_(25994, "sub", lambda: sub)) for sub in _n_(25996, "list_str", lambda: list_str))
    _l_(25997)
    counts = _c_(26003, _n_(25998, "Counter", lambda: Counter), _c_(26002, _a_(26000, _n_(25999, "chain", lambda: chain), "from_iterable"), _n_(26001, "temp", lambda: temp)))
    _l_(26004)
    gt_N = [_n_(26005, "chr", lambda: chr) for (chr, count) in _c_(26008, _a_(26007, _n_(26006, "counts", lambda: counts), "items")) if _n_(26009, "count", lambda: count) > _n_(26010, "N", lambda: N)]
    _l_(26011)
    lt_N = [_n_(26012, "chr", lambda: chr) for (chr, count) in _c_(26015, _a_(26014, _n_(26013, "counts", lambda: counts), "items")) if _n_(26016, "count", lambda: count) < _n_(26017, "N", lambda: N)]
    _l_(26018)
    aux = (_n_(26019, "gt_N", lambda: gt_N), _n_(26020, "lt_N", lambda: lt_N))
    _l_(26021)
    return aux
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
_l_(26023)
_c_(26025, _n_(26024, "print", lambda: print), 'Original list:')
_l_(26026)
_c_(26029, _n_(26027, "print", lambda: print), _n_(26028, "list_str", lambda: list_str))
_l_(26030)
N = 3
_l_(26031)
_c_(26034, _n_(26032, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(26033, "N", lambda: N))
_l_(26035)
_c_(26038, _n_(26036, "print", lambda: print), _n_(26037, "result", lambda: result)[0])
_l_(26039)
_c_(26042, _n_(26040, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(26041, "N", lambda: N))
_l_(26043)
_c_(26046, _n_(26044, "print", lambda: print), _n_(26045, "result", lambda: result)[1])
_l_(26047)