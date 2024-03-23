# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(5705)

except ImportError:
    pass
try:
    from operator import getitem
    _l_(5707)

except ImportError:
    pass

def get(d, selectors):
    _l_(5714)

    aux = _c_(5712, _n_(5708, "reduce", lambda: reduce), _n_(5709, "getitem", lambda: getitem), _n_(5710, "selectors", lambda: selectors), _n_(5711, "d", lambda: d))
    _l_(5713)
    return aux
_c_(5719, _n_(5715, "print", lambda: print), _c_(5718, _n_(5716, "get", lambda: get), _n_(5717, "users", lambda: users), ['freddy', 'name', 'last']))
_l_(5720)
_c_(5725, _n_(5721, "print", lambda: print), _c_(5724, _n_(5722, "get", lambda: get), _n_(5723, "users", lambda: users), ['freddy', 'postIds', 1]))
_l_(5726)