# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(102042)

except ImportError:
    pass
try:
    import numpy as np
    _l_(102044)

except ImportError:
    pass
sales_tuples = _c_(102049, _n_(102045, "list", lambda: list), _c_(102048, _n_(102046, "zip", lambda: zip), *_n_(102047, "sales_arrays", lambda: sales_arrays)))
_l_(102050)
sales_index = _c_(102055, _a_(102053, _a_(102052, _n_(102051, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(102054, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(102056)
_c_(102058, _n_(102057, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(102059)
df = _c_(102067, _a_(102061, _n_(102060, "pd", lambda: pd), "DataFrame"), _c_(102065, _a_(102064, _a_(102063, _n_(102062, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(102066, "sales_index", lambda: sales_index))
_l_(102068)
_c_(102071, _n_(102069, "print", lambda: print), _n_(102070, "df", lambda: df))
_l_(102072)
_c_(102074, _n_(102073, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(102075)
positions = [1, 2, 5]
_l_(102076)
_c_(102081, _n_(102077, "print", lambda: print), _c_(102080, _a_(102079, _n_(102078, "df", lambda: df), "take"), [1, 2, 5]))
_l_(102082)
_c_(102084, _n_(102083, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(102085)
_c_(102090, _n_(102086, "print", lambda: print), _c_(102089, _a_(102088, _n_(102087, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(102091)
_c_(102093, _n_(102092, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(102094)
_c_(102099, _n_(102095, "print", lambda: print), _c_(102098, _a_(102097, _n_(102096, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(102100)