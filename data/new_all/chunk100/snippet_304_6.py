# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(26165)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(26167)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(26190)

    temp = (_c_(26170, _n_(26168, "set", lambda: set), _n_(26169, "sub", lambda: sub)) for sub in _n_(26171, "list_str", lambda: list_str))
    _l_(26172)
    counts = _c_(26178, _n_(26173, "Counter", lambda: Counter), _c_(26177, _a_(26175, _n_(26174, "chain", lambda: chain), "from_iterable"), _n_(26176, "temp", lambda: temp)))
    _l_(26179)
    lt_N = [_n_(26180, "chr", lambda: chr) for (chr, count) in _c_(26183, _a_(26182, _n_(26181, "counts", lambda: counts), "items")) if _n_(26184, "count", lambda: count) < _n_(26185, "N", lambda: N)]
    _l_(26186)
    aux = (_n_(26187, "gt_N", lambda: gt_N), _n_(26188, "lt_N", lambda: lt_N))
    _l_(26189)
    return aux
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
_l_(26191)
_c_(26193, _n_(26192, "print", lambda: print), 'Original list:')
_l_(26194)
_c_(26197, _n_(26195, "print", lambda: print), _n_(26196, "list_str", lambda: list_str))
_l_(26198)
N = 3
_l_(26199)
result = _c_(26203, _n_(26200, "max_aggregate", lambda: max_aggregate), _n_(26201, "list_str", lambda: list_str), _n_(26202, "N", lambda: N))
_l_(26204)
_c_(26207, _n_(26205, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(26206, "N", lambda: N))
_l_(26208)
_c_(26211, _n_(26209, "print", lambda: print), _n_(26210, "result", lambda: result)[0])
_l_(26212)
_c_(26215, _n_(26213, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(26214, "N", lambda: N))
_l_(26216)
_c_(26219, _n_(26217, "print", lambda: print), _n_(26218, "result", lambda: result)[1])
_l_(26220)