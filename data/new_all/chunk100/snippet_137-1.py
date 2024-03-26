# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(101932)

except ImportError:
    pass
try:
    import numpy as np
    _l_(101934)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(101935)
sales_tuples = _c_(101940, _n_(101936, "list", lambda: list), _c_(101939, _n_(101937, "zip", lambda: zip), *_n_(101938, "sales_arrays", lambda: sales_arrays)))
_l_(101941)
_c_(101943, _n_(101942, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(101944)
df = _c_(101952, _a_(101946, _n_(101945, "pd", lambda: pd), "DataFrame"), _c_(101950, _a_(101949, _a_(101948, _n_(101947, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(101951, "sales_index", lambda: sales_index))
_l_(101953)
_c_(101956, _n_(101954, "print", lambda: print), _n_(101955, "df", lambda: df))
_l_(101957)
_c_(101959, _n_(101958, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(101960)
positions = [1, 2, 5]
_l_(101961)
_c_(101966, _n_(101962, "print", lambda: print), _c_(101965, _a_(101964, _n_(101963, "df", lambda: df), "take"), [1, 2, 5]))
_l_(101967)
_c_(101969, _n_(101968, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(101970)
_c_(101975, _n_(101971, "print", lambda: print), _c_(101974, _a_(101973, _n_(101972, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(101976)
_c_(101978, _n_(101977, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(101979)
_c_(101984, _n_(101980, "print", lambda: print), _c_(101983, _a_(101982, _n_(101981, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(101985)