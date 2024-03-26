# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112332)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112334)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(112335)
sales_tuples = _c_(112340, _n_(112336, "list", lambda: list), _c_(112339, _n_(112337, "zip", lambda: zip), *_n_(112338, "sales_arrays", lambda: sales_arrays)))
_l_(112341)
_c_(112343, _n_(112342, "print", lambda: print), 'Create a MultiIndex:')
_l_(112344)
sales_index = _c_(112349, _a_(112347, _a_(112346, _n_(112345, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(112348, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(112350)
_c_(112353, _n_(112351, "print", lambda: print), _n_(112352, "sales_tuples", lambda: sales_tuples))
_l_(112354)
_c_(112356, _n_(112355, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(112357)
_c_(112360, _n_(112358, "print", lambda: print), _n_(112359, "df", lambda: df))
_l_(112361)