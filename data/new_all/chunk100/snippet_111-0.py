# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(100780)

except ImportError:
    pass
try:
    from operator import getitem
    _l_(100782)

except ImportError:
    pass

def get(d, selectors):
    _l_(100789)

    aux = _c_(100787, _n_(100783, "reduce", lambda: reduce), _n_(100784, "getitem", lambda: getitem), _n_(100785, "selectors", lambda: selectors), _n_(100786, "d", lambda: d))
    _l_(100788)
    return aux
_c_(100794, _n_(100790, "print", lambda: print), _c_(100793, _n_(100791, "get", lambda: get), _n_(100792, "users", lambda: users), ['freddy', 'name', 'last']))
_l_(100795)
_c_(100800, _n_(100796, "print", lambda: print), _c_(100799, _n_(100797, "get", lambda: get), _n_(100798, "users", lambda: users), ['freddy', 'postIds', 1]))
_l_(100801)