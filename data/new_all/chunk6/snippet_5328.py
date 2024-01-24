# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66494598/nameerror-name-update-is-not-defined-ponyorm
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pony.orm import *
    _l_(342794)

except ImportError:
    pass

customer = _c_(342802, _n_(342795, "update", lambda: update), (_c_(342798, _a_(342797, _n_(342796, "c", lambda: c), "set"), CustomerCode = '123') for c in _n_(342799, "Customers", lambda: Customers) if _a_(342801, _n_(342800, "c", lambda: c), "CustomerCode") == '456'))
_l_(342803)