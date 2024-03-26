# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112298)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112300)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(112301)
_c_(112303, _n_(112302, "print", lambda: print), 'Create a MultiIndex:')
_l_(112304)
sales_index = _c_(112309, _a_(112307, _a_(112306, _n_(112305, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(112308, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(112310)
_c_(112313, _n_(112311, "print", lambda: print), _n_(112312, "sales_tuples", lambda: sales_tuples))
_l_(112314)
_c_(112316, _n_(112315, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(112317)
df = _c_(112325, _a_(112319, _n_(112318, "pd", lambda: pd), "DataFrame"), _c_(112323, _a_(112322, _a_(112321, _n_(112320, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(112324, "sales_index", lambda: sales_index))
_l_(112326)
_c_(112329, _n_(112327, "print", lambda: print), _n_(112328, "df", lambda: df))
_l_(112330)