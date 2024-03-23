# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(25870)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(25872)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(25902)

    temp = (_c_(25875, _n_(25873, "set", lambda: set), _n_(25874, "sub", lambda: sub)) for sub in _n_(25876, "list_str", lambda: list_str))
    _l_(25877)
    counts = _c_(25883, _n_(25878, "Counter", lambda: Counter), _c_(25882, _a_(25880, _n_(25879, "chain", lambda: chain), "from_iterable"), _n_(25881, "temp", lambda: temp)))
    _l_(25884)
    gt_N = [_n_(25885, "chr", lambda: chr) for (chr, count) in _c_(25888, _a_(25887, _n_(25886, "counts", lambda: counts), "items")) if _n_(25889, "count", lambda: count) > _n_(25890, "N", lambda: N)]
    _l_(25891)
    lt_N = [_n_(25892, "chr", lambda: chr) for (chr, count) in _c_(25895, _a_(25894, _n_(25893, "counts", lambda: counts), "items")) if _n_(25896, "count", lambda: count) < _n_(25897, "N", lambda: N)]
    _l_(25898)
    aux = (_n_(25899, "gt_N", lambda: gt_N), _n_(25900, "lt_N", lambda: lt_N))
    _l_(25901)
    return aux
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
_l_(25903)
_c_(25905, _n_(25904, "print", lambda: print), 'Original list:')
_l_(25906)
_c_(25909, _n_(25907, "print", lambda: print), _n_(25908, "list_str", lambda: list_str))
_l_(25910)
result = _c_(25914, _n_(25911, "max_aggregate", lambda: max_aggregate), _n_(25912, "list_str", lambda: list_str), _n_(25913, "N", lambda: N))
_l_(25915)
_c_(25918, _n_(25916, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(25917, "N", lambda: N))
_l_(25919)
_c_(25922, _n_(25920, "print", lambda: print), _n_(25921, "result", lambda: result)[0])
_l_(25923)
_c_(25926, _n_(25924, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(25925, "N", lambda: N))
_l_(25927)
_c_(25930, _n_(25928, "print", lambda: print), _n_(25929, "result", lambda: result)[1])
_l_(25931)