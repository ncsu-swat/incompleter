# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(109391)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(109393)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(109423)

    temp = (_c_(109396, _n_(109394, "set", lambda: set), _n_(109395, "sub", lambda: sub)) for sub in _n_(109397, "list_str", lambda: list_str))
    _l_(109398)
    counts = _c_(109404, _n_(109399, "Counter", lambda: Counter), _c_(109403, _a_(109401, _n_(109400, "chain", lambda: chain), "from_iterable"), _n_(109402, "temp", lambda: temp)))
    _l_(109405)
    gt_N = [_n_(109406, "chr", lambda: chr) for chr, count in _c_(109409, _a_(109408, _n_(109407, "counts", lambda: counts), "items")) if _n_(109410, "count", lambda: count) > _n_(109411, "N", lambda: N)]
    _l_(109412)
    lt_N = [_n_(109413, "chr", lambda: chr) for chr, count in _c_(109416, _a_(109415, _n_(109414, "counts", lambda: counts), "items")) if _n_(109417, "count", lambda: count) < _n_(109418, "N", lambda: N)]
    _l_(109419)
    aux = (_n_(109420, "gt_N", lambda: gt_N), _n_(109421, "lt_N", lambda: lt_N))
    _l_(109422)
    return aux
_c_(109425, _n_(109424, "print", lambda: print), 'Original list:')
_l_(109426)
_c_(109429, _n_(109427, "print", lambda: print), _n_(109428, "list_str", lambda: list_str))
_l_(109430)
N = 3
_l_(109431)
result = _c_(109435, _n_(109432, "max_aggregate", lambda: max_aggregate), _n_(109433, "list_str", lambda: list_str), _n_(109434, "N", lambda: N))
_l_(109436)
_c_(109439, _n_(109437, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(109438, "N", lambda: N))
_l_(109440)
_c_(109443, _n_(109441, "print", lambda: print), _n_(109442, "result", lambda: result)[0])
_l_(109444)
_c_(109447, _n_(109445, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(109446, "N", lambda: N))
_l_(109448)
_c_(109451, _n_(109449, "print", lambda: print), _n_(109450, "result", lambda: result)[1])
_l_(109452)