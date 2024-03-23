# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(25807)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(25809)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(25839)

    temp = (_c_(25812, _n_(25810, "set", lambda: set), _n_(25811, "sub", lambda: sub)) for sub in _n_(25813, "list_str", lambda: list_str))
    _l_(25814)
    counts = _c_(25820, _n_(25815, "Counter", lambda: Counter), _c_(25819, _a_(25817, _n_(25816, "chain", lambda: chain), "from_iterable"), _n_(25818, "temp", lambda: temp)))
    _l_(25821)
    gt_N = [_n_(25822, "chr", lambda: chr) for (chr, count) in _c_(25825, _a_(25824, _n_(25823, "counts", lambda: counts), "items")) if _n_(25826, "count", lambda: count) > _n_(25827, "N", lambda: N)]
    _l_(25828)
    lt_N = [_n_(25829, "chr", lambda: chr) for (chr, count) in _c_(25832, _a_(25831, _n_(25830, "counts", lambda: counts), "items")) if _n_(25833, "count", lambda: count) < _n_(25834, "N", lambda: N)]
    _l_(25835)
    aux = (_n_(25836, "gt_N", lambda: gt_N), _n_(25837, "lt_N", lambda: lt_N))
    _l_(25838)
    return aux
_c_(25841, _n_(25840, "print", lambda: print), 'Original list:')
_l_(25842)
_c_(25845, _n_(25843, "print", lambda: print), _n_(25844, "list_str", lambda: list_str))
_l_(25846)
N = 3
_l_(25847)
result = _c_(25851, _n_(25848, "max_aggregate", lambda: max_aggregate), _n_(25849, "list_str", lambda: list_str), _n_(25850, "N", lambda: N))
_l_(25852)
_c_(25855, _n_(25853, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(25854, "N", lambda: N))
_l_(25856)
_c_(25859, _n_(25857, "print", lambda: print), _n_(25858, "result", lambda: result)[0])
_l_(25860)
_c_(25863, _n_(25861, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(25862, "N", lambda: N))
_l_(25864)
_c_(25867, _n_(25865, "print", lambda: print), _n_(25866, "result", lambda: result)[1])
_l_(25868)