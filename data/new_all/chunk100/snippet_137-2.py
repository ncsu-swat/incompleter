# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(101987)

except ImportError:
    pass
try:
    import numpy as np
    _l_(101989)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(101990)
sales_index = _c_(101995, _a_(101993, _a_(101992, _n_(101991, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(101994, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(101996)
_c_(101998, _n_(101997, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(101999)
df = _c_(102007, _a_(102001, _n_(102000, "pd", lambda: pd), "DataFrame"), _c_(102005, _a_(102004, _a_(102003, _n_(102002, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(102006, "sales_index", lambda: sales_index))
_l_(102008)
_c_(102011, _n_(102009, "print", lambda: print), _n_(102010, "df", lambda: df))
_l_(102012)
_c_(102014, _n_(102013, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(102015)
positions = [1, 2, 5]
_l_(102016)
_c_(102021, _n_(102017, "print", lambda: print), _c_(102020, _a_(102019, _n_(102018, "df", lambda: df), "take"), [1, 2, 5]))
_l_(102022)
_c_(102024, _n_(102023, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(102025)
_c_(102030, _n_(102026, "print", lambda: print), _c_(102029, _a_(102028, _n_(102027, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(102031)
_c_(102033, _n_(102032, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(102034)
_c_(102039, _n_(102035, "print", lambda: print), _c_(102038, _a_(102037, _n_(102036, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(102040)