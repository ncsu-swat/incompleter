# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(101880)

except ImportError:
    pass
try:
    import numpy as np
    _l_(101882)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(101883)
sales_tuples = _c_(101888, _n_(101884, "list", lambda: list), _c_(101887, _n_(101885, "zip", lambda: zip), *_n_(101886, "sales_arrays", lambda: sales_arrays)))
_l_(101889)
sales_index = _c_(101894, _a_(101892, _a_(101891, _n_(101890, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(101893, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(101895)
_c_(101897, _n_(101896, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(101898)
_c_(101901, _n_(101899, "print", lambda: print), _n_(101900, "df", lambda: df))
_l_(101902)
_c_(101904, _n_(101903, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(101905)
positions = [1, 2, 5]
_l_(101906)
_c_(101911, _n_(101907, "print", lambda: print), _c_(101910, _a_(101909, _n_(101908, "df", lambda: df), "take"), [1, 2, 5]))
_l_(101912)
_c_(101914, _n_(101913, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(101915)
_c_(101920, _n_(101916, "print", lambda: print), _c_(101919, _a_(101918, _n_(101917, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(101921)
_c_(101923, _n_(101922, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(101924)
_c_(101929, _n_(101925, "print", lambda: print), _c_(101928, _a_(101927, _n_(101926, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(101930)