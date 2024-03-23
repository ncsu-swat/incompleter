# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(26049)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(26051)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(26074)

    temp = (_c_(26054, _n_(26052, "set", lambda: set), _n_(26053, "sub", lambda: sub)) for sub in _n_(26055, "list_str", lambda: list_str))
    _l_(26056)
    gt_N = [_n_(26057, "chr", lambda: chr) for (chr, count) in _c_(26060, _a_(26059, _n_(26058, "counts", lambda: counts), "items")) if _n_(26061, "count", lambda: count) > _n_(26062, "N", lambda: N)]
    _l_(26063)
    lt_N = [_n_(26064, "chr", lambda: chr) for (chr, count) in _c_(26067, _a_(26066, _n_(26065, "counts", lambda: counts), "items")) if _n_(26068, "count", lambda: count) < _n_(26069, "N", lambda: N)]
    _l_(26070)
    aux = (_n_(26071, "gt_N", lambda: gt_N), _n_(26072, "lt_N", lambda: lt_N))
    _l_(26073)
    return aux
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
_l_(26075)
_c_(26077, _n_(26076, "print", lambda: print), 'Original list:')
_l_(26078)
_c_(26081, _n_(26079, "print", lambda: print), _n_(26080, "list_str", lambda: list_str))
_l_(26082)
N = 3
_l_(26083)
result = _c_(26087, _n_(26084, "max_aggregate", lambda: max_aggregate), _n_(26085, "list_str", lambda: list_str), _n_(26086, "N", lambda: N))
_l_(26088)
_c_(26091, _n_(26089, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(26090, "N", lambda: N))
_l_(26092)
_c_(26095, _n_(26093, "print", lambda: print), _n_(26094, "result", lambda: result)[0])
_l_(26096)
_c_(26099, _n_(26097, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(26098, "N", lambda: N))
_l_(26100)
_c_(26103, _n_(26101, "print", lambda: print), _n_(26102, "result", lambda: result)[1])
_l_(26104)