# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35807)

except ImportError:
    pass
try:
    import numpy as np
    _l_(35809)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(35810)
sales_tuples = _c_(35815, _n_(35811, "list", lambda: list), _c_(35814, _n_(35812, "zip", lambda: zip), *_n_(35813, "sales_arrays", lambda: sales_arrays)))
_l_(35816)
_c_(35818, _n_(35817, "print", lambda: print), 'Create a MultiIndex:')
_l_(35819)
sales_index = _c_(35824, _a_(35822, _a_(35821, _n_(35820, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(35823, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(35825)
_c_(35828, _n_(35826, "print", lambda: print), _n_(35827, "sales_tuples", lambda: sales_tuples))
_l_(35829)
_c_(35831, _n_(35830, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(35832)
_c_(35835, _n_(35833, "print", lambda: print), _n_(35834, "df", lambda: df))
_l_(35836)