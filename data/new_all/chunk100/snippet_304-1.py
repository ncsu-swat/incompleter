# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(109454)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(109456)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(109486)

    temp = (_c_(109459, _n_(109457, "set", lambda: set), _n_(109458, "sub", lambda: sub)) for sub in _n_(109460, "list_str", lambda: list_str))
    _l_(109461)
    counts = _c_(109467, _n_(109462, "Counter", lambda: Counter), _c_(109466, _a_(109464, _n_(109463, "chain", lambda: chain), "from_iterable"), _n_(109465, "temp", lambda: temp)))
    _l_(109468)
    gt_N = [_n_(109469, "chr", lambda: chr) for chr, count in _c_(109472, _a_(109471, _n_(109470, "counts", lambda: counts), "items")) if _n_(109473, "count", lambda: count) > _n_(109474, "N", lambda: N)]
    _l_(109475)
    lt_N = [_n_(109476, "chr", lambda: chr) for chr, count in _c_(109479, _a_(109478, _n_(109477, "counts", lambda: counts), "items")) if _n_(109480, "count", lambda: count) < _n_(109481, "N", lambda: N)]
    _l_(109482)
    aux = (_n_(109483, "gt_N", lambda: gt_N), _n_(109484, "lt_N", lambda: lt_N))
    _l_(109485)
    return aux
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
_l_(109487)
_c_(109489, _n_(109488, "print", lambda: print), 'Original list:')
_l_(109490)
_c_(109493, _n_(109491, "print", lambda: print), _n_(109492, "list_str", lambda: list_str))
_l_(109494)
N = 3
_l_(109495)
_c_(109498, _n_(109496, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(109497, "N", lambda: N))
_l_(109499)
_c_(109502, _n_(109500, "print", lambda: print), _n_(109501, "result", lambda: result)[0])
_l_(109503)
_c_(109506, _n_(109504, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(109505, "N", lambda: N))
_l_(109507)
_c_(109510, _n_(109508, "print", lambda: print), _n_(109509, "result", lambda: result)[1])
_l_(109511)