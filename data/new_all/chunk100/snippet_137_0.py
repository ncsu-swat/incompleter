# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(9014)

except ImportError:
    pass
try:
    import numpy as np
    _l_(9016)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(9017)
sales_tuples = _c_(9022, _n_(9018, "list", lambda: list), _c_(9021, _n_(9019, "zip", lambda: zip), *_n_(9020, "sales_arrays", lambda: sales_arrays)))
_l_(9023)
sales_index = _c_(9028, _a_(9026, _a_(9025, _n_(9024, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(9027, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(9029)
_c_(9031, _n_(9030, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(9032)
df = _c_(9040, _a_(9034, _n_(9033, "pd", lambda: pd), "DataFrame"), _c_(9038, _a_(9037, _a_(9036, _n_(9035, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(9039, "sales_index", lambda: sales_index))
_l_(9041)
_c_(9044, _n_(9042, "print", lambda: print), _n_(9043, "df", lambda: df))
_l_(9045)
_c_(9047, _n_(9046, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(9048)
_c_(9053, _n_(9049, "print", lambda: print), _c_(9052, _a_(9051, _n_(9050, "df", lambda: df), "take"), [1, 2, 5]))
_l_(9054)
_c_(9056, _n_(9055, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(9057)
_c_(9062, _n_(9058, "print", lambda: print), _c_(9061, _a_(9060, _n_(9059, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(9063)
_c_(9065, _n_(9064, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(9066)
_c_(9071, _n_(9067, "print", lambda: print), _c_(9070, _a_(9069, _n_(9068, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(9072)