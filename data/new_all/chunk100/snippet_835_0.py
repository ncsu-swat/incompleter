# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(83092)

except ImportError:
    pass
try:
    import numpy as np
    _l_(83094)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(83095)
_c_(83097, _n_(83096, "print", lambda: print), 'Create a MultiIndex:')
_l_(83098)
sales_index = _c_(83103, _a_(83101, _a_(83100, _n_(83099, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(83102, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(83104)
_c_(83107, _n_(83105, "print", lambda: print), _n_(83106, "sales_tuples", lambda: sales_tuples))
_l_(83108)
_c_(83110, _n_(83109, "print", lambda: print), '\nConstruct a series using the said MultiIndex levels: ')
_l_(83111)
s = _c_(83119, _a_(83113, _n_(83112, "pd", lambda: pd), "Series"), _c_(83117, _a_(83116, _a_(83115, _n_(83114, "np", lambda: np), "random"), "randn"), 8), index=_n_(83118, "sales_index", lambda: sales_index))
_l_(83120)
_c_(83123, _n_(83121, "print", lambda: print), _n_(83122, "s", lambda: s))
_l_(83124)