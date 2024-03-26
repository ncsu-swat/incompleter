# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112402)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112404)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(112405)
sales_tuples = _c_(112410, _n_(112406, "list", lambda: list), _c_(112409, _n_(112407, "zip", lambda: zip), *_n_(112408, "sales_arrays", lambda: sales_arrays)))
_l_(112411)
_c_(112413, _n_(112412, "print", lambda: print), 'Create a MultiIndex:')
_l_(112414)
_c_(112417, _n_(112415, "print", lambda: print), _n_(112416, "sales_tuples", lambda: sales_tuples))
_l_(112418)
_c_(112420, _n_(112419, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(112421)
df = _c_(112429, _a_(112423, _n_(112422, "pd", lambda: pd), "DataFrame"), _c_(112427, _a_(112426, _a_(112425, _n_(112424, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(112428, "sales_index", lambda: sales_index))
_l_(112430)
_c_(112433, _n_(112431, "print", lambda: print), _n_(112432, "df", lambda: df))
_l_(112434)