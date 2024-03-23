# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import zip_longest, chain, tee
    _l_(10593)

except ImportError:
    pass

def replace2copy(lst):
    _l_(10610)

    (lst1, lst2) = _c_(10598, _n_(10594, "tee", lambda: tee), _c_(10597, _n_(10595, "iter", lambda: iter), _n_(10596, "lst", lambda: lst)), 2)
    _l_(10599)
    aux = _c_(10608, _n_(10600, "list", lambda: list), _c_(10607, _a_(10602, _n_(10601, "chain", lambda: chain), "from_iterable"), _c_(10606, _n_(10603, "zip_longest", lambda: zip_longest), _n_(10604, "lst", lambda: lst)[1::2], _n_(10605, "lst", lambda: lst)[::2])))
    _l_(10609)
    return aux
_c_(10615, _n_(10611, "print", lambda: print), _c_(10614, _n_(10612, "replace2copy", lambda: replace2copy), _n_(10613, "n", lambda: n)))
_l_(10616)