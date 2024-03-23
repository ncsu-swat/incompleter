# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(83126)

except ImportError:
    pass
try:
    import numpy as np
    _l_(83128)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(83129)
sales_tuples = _c_(83134, _n_(83130, "list", lambda: list), _c_(83133, _n_(83131, "zip", lambda: zip), *_n_(83132, "sales_arrays", lambda: sales_arrays)))
_l_(83135)
_c_(83137, _n_(83136, "print", lambda: print), 'Create a MultiIndex:')
_l_(83138)
_c_(83141, _n_(83139, "print", lambda: print), _n_(83140, "sales_tuples", lambda: sales_tuples))
_l_(83142)
_c_(83144, _n_(83143, "print", lambda: print), '\nConstruct a series using the said MultiIndex levels: ')
_l_(83145)
s = _c_(83153, _a_(83147, _n_(83146, "pd", lambda: pd), "Series"), _c_(83151, _a_(83150, _a_(83149, _n_(83148, "np", lambda: np), "random"), "randn"), 8), index=_n_(83152, "sales_index", lambda: sales_index))
_l_(83154)
_c_(83157, _n_(83155, "print", lambda: print), _n_(83156, "s", lambda: s))
_l_(83158)