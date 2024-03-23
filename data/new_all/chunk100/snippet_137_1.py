# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(9074)

except ImportError:
    pass
try:
    import numpy as np
    _l_(9076)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(9077)
sales_tuples = _c_(9082, _n_(9078, "list", lambda: list), _c_(9081, _n_(9079, "zip", lambda: zip), *_n_(9080, "sales_arrays", lambda: sales_arrays)))
_l_(9083)
_c_(9085, _n_(9084, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(9086)
df = _c_(9094, _a_(9088, _n_(9087, "pd", lambda: pd), "DataFrame"), _c_(9092, _a_(9091, _a_(9090, _n_(9089, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(9093, "sales_index", lambda: sales_index))
_l_(9095)
_c_(9098, _n_(9096, "print", lambda: print), _n_(9097, "df", lambda: df))
_l_(9099)
_c_(9101, _n_(9100, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(9102)
positions = [1, 2, 5]
_l_(9103)
_c_(9108, _n_(9104, "print", lambda: print), _c_(9107, _a_(9106, _n_(9105, "df", lambda: df), "take"), [1, 2, 5]))
_l_(9109)
_c_(9111, _n_(9110, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(9112)
_c_(9117, _n_(9113, "print", lambda: print), _c_(9116, _a_(9115, _n_(9114, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(9118)
_c_(9120, _n_(9119, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(9121)
_c_(9126, _n_(9122, "print", lambda: print), _c_(9125, _a_(9124, _n_(9123, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(9127)