# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(70796)

except ImportError:
    pass
try:
    from operator import getitem
    _l_(70798)

except ImportError:
    pass

def test(d, selectors):
    _l_(70805)

    aux = _c_(70803, _n_(70799, "reduce", lambda: reduce), _n_(70800, "getitem", lambda: getitem), _n_(70801, "selectors", lambda: selectors), _n_(70802, "d", lambda: d))
    _l_(70804)
    return aux
_c_(70810, _n_(70806, "print", lambda: print), _c_(70809, _n_(70807, "test", lambda: test), _n_(70808, "users", lambda: users), ['Carla ', 'name', 'last']))
_l_(70811)
_c_(70816, _n_(70812, "print", lambda: print), _c_(70815, _n_(70813, "test", lambda: test), _n_(70814, "users", lambda: users), ['Carla ', 'postIds', 1]))
_l_(70817)