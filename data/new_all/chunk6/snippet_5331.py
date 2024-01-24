# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66494598/nameerror-name-update-is-not-defined-ponyorm
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pony.orm import *
    _l_(358239)

except ImportError:
    pass

customer = _c_(358247, _n_(358240, "update", lambda: update), (_c_(358243, _a_(358242, _n_(358241, "c", lambda: c), "set"), CustomerCode = '123') for c in _n_(358244, "Customers", lambda: Customers) if _a_(358246, _n_(358245, "c", lambda: c), "CustomerCode") == '456'))
_l_(358248)