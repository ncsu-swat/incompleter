# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(25933)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(25935)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(25958)

    temp = (_c_(25938, _n_(25936, "set", lambda: set), _n_(25937, "sub", lambda: sub)) for sub in _n_(25939, "list_str", lambda: list_str))
    _l_(25940)
    counts = _c_(25946, _n_(25941, "Counter", lambda: Counter), _c_(25945, _a_(25943, _n_(25942, "chain", lambda: chain), "from_iterable"), _n_(25944, "temp", lambda: temp)))
    _l_(25947)
    gt_N = [_n_(25948, "chr", lambda: chr) for (chr, count) in _c_(25951, _a_(25950, _n_(25949, "counts", lambda: counts), "items")) if _n_(25952, "count", lambda: count) > _n_(25953, "N", lambda: N)]
    _l_(25954)
    aux = (_n_(25955, "gt_N", lambda: gt_N), _n_(25956, "lt_N", lambda: lt_N))
    _l_(25957)
    return aux
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
_l_(25959)
_c_(25961, _n_(25960, "print", lambda: print), 'Original list:')
_l_(25962)
_c_(25965, _n_(25963, "print", lambda: print), _n_(25964, "list_str", lambda: list_str))
_l_(25966)
N = 3
_l_(25967)
result = _c_(25971, _n_(25968, "max_aggregate", lambda: max_aggregate), _n_(25969, "list_str", lambda: list_str), _n_(25970, "N", lambda: N))
_l_(25972)
_c_(25975, _n_(25973, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(25974, "N", lambda: N))
_l_(25976)
_c_(25979, _n_(25977, "print", lambda: print), _n_(25978, "result", lambda: result)[0])
_l_(25980)
_c_(25983, _n_(25981, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(25982, "N", lambda: N))
_l_(25984)
_c_(25987, _n_(25985, "print", lambda: print), _n_(25986, "result", lambda: result)[1])
_l_(25988)