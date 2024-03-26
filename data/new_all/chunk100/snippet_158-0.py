# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import zip_longest, chain, tee
    _l_(102723)

except ImportError:
    pass

def replace2copy(lst):
    _l_(102740)

    lst1, lst2 = _c_(102728, _n_(102724, "tee", lambda: tee), _c_(102727, _n_(102725, "iter", lambda: iter), _n_(102726, "lst", lambda: lst)), 2)
    _l_(102729)
    aux = _c_(102738, _n_(102730, "list", lambda: list), _c_(102737, _a_(102732, _n_(102731, "chain", lambda: chain), "from_iterable"), _c_(102736, _n_(102733, "zip_longest", lambda: zip_longest), _n_(102734, "lst", lambda: lst)[1::2], _n_(102735, "lst", lambda: lst)[::2])))
    _l_(102739)
    return aux
_c_(102745, _n_(102741, "print", lambda: print), _c_(102744, _n_(102742, "replace2copy", lambda: replace2copy), _n_(102743, "n", lambda: n)))
_l_(102746)