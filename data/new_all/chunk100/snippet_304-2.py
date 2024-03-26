# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(109513)

except ImportError:
    pass
try:
    from itertools import chain
    _l_(109515)

except ImportError:
    pass

def max_aggregate(list_str, N):
    _l_(109545)

    temp = (_c_(109518, _n_(109516, "set", lambda: set), _n_(109517, "sub", lambda: sub)) for sub in _n_(109519, "list_str", lambda: list_str))
    _l_(109520)
    counts = _c_(109526, _n_(109521, "Counter", lambda: Counter), _c_(109525, _a_(109523, _n_(109522, "chain", lambda: chain), "from_iterable"), _n_(109524, "temp", lambda: temp)))
    _l_(109527)
    gt_N = [_n_(109528, "chr", lambda: chr) for chr, count in _c_(109531, _a_(109530, _n_(109529, "counts", lambda: counts), "items")) if _n_(109532, "count", lambda: count) > _n_(109533, "N", lambda: N)]
    _l_(109534)
    lt_N = [_n_(109535, "chr", lambda: chr) for chr, count in _c_(109538, _a_(109537, _n_(109536, "counts", lambda: counts), "items")) if _n_(109539, "count", lambda: count) < _n_(109540, "N", lambda: N)]
    _l_(109541)
    aux = (_n_(109542, "gt_N", lambda: gt_N), _n_(109543, "lt_N", lambda: lt_N))
    _l_(109544)
    return aux
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
_l_(109546)
_c_(109548, _n_(109547, "print", lambda: print), 'Original list:')
_l_(109549)
_c_(109552, _n_(109550, "print", lambda: print), _n_(109551, "list_str", lambda: list_str))
_l_(109553)
result = _c_(109557, _n_(109554, "max_aggregate", lambda: max_aggregate), _n_(109555, "list_str", lambda: list_str), _n_(109556, "N", lambda: N))
_l_(109558)
_c_(109561, _n_(109559, "print", lambda: print), '\nCharacters of the said list of strings which occur more than:', _n_(109560, "N", lambda: N))
_l_(109562)
_c_(109565, _n_(109563, "print", lambda: print), _n_(109564, "result", lambda: result)[0])
_l_(109566)
_c_(109569, _n_(109567, "print", lambda: print), '\nCharacters of the said list of strings which occur less than:', _n_(109568, "N", lambda: N))
_l_(109570)
_c_(109573, _n_(109571, "print", lambda: print), _n_(109572, "result", lambda: result)[1])
_l_(109574)