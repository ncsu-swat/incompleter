# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(26106)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(26108)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(26133)

    counts = _c_(26114, _n_(26109, "Counter", lambda: Counter), _c_(26113, _a_(26111, _n_(26110, "chain", lambda: chain), "from_iterable"), _n_(26112, "temp", lambda: temp)))
    _l_(26115)
    gt_N = [_n_(26116, "chr", lambda: chr) for (chr, count) in _c_(26119, _a_(26118, _n_(26117, "counts", lambda: counts), "items")) if _n_(26120, "count", lambda: count) > _n_(26121, "N", lambda: N)]
    _l_(26122)
    lt_N = [_n_(26123, "chr", lambda: chr) for (chr, count) in _c_(26126, _a_(26125, _n_(26124, "counts", lambda: counts), "items")) if _n_(26127, "count", lambda: count) < _n_(26128, "N", lambda: N)]
    _l_(26129)
    aux = (_n_(26130, "gt_N", lambda: gt_N), _n_(26131, "lt_N", lambda: lt_N))
    _l_(26132)
    return aux
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
_l_(26134)
_c_(26136, _n_(26135, "print", lambda: print), 'Original list:')
_l_(26137)
_c_(26140, _n_(26138, "print", lambda: print), _n_(26139, "list_str", lambda: list_str))
_l_(26141)
N = 3
_l_(26142)
result = _c_(26146, _n_(26143, "max_aggregate", lambda: max_aggregate), _n_(26144, "list_str", lambda: list_str), _n_(26145, "N", lambda: N))
_l_(26147)
_c_(26150, _n_(26148, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(26149, "N", lambda: N))
_l_(26151)
_c_(26154, _n_(26152, "print", lambda: print), _n_(26153, "result", lambda: result)[0])
_l_(26155)
_c_(26158, _n_(26156, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(26157, "N", lambda: N))
_l_(26159)
_c_(26162, _n_(26160, "print", lambda: print), _n_(26161, "result", lambda: result)[1])
_l_(26163)