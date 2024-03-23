# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(9189)

except ImportError:
    pass
try:
    import numpy as np
    _l_(9191)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(9192)
sales_index = _c_(9197, _a_(9195, _a_(9194, _n_(9193, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(9196, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(9198)
_c_(9200, _n_(9199, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(9201)
df = _c_(9209, _a_(9203, _n_(9202, "pd", lambda: pd), "DataFrame"), _c_(9207, _a_(9206, _a_(9205, _n_(9204, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(9208, "sales_index", lambda: sales_index))
_l_(9210)
_c_(9213, _n_(9211, "print", lambda: print), _n_(9212, "df", lambda: df))
_l_(9214)
_c_(9216, _n_(9215, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(9217)
positions = [1, 2, 5]
_l_(9218)
_c_(9223, _n_(9219, "print", lambda: print), _c_(9222, _a_(9221, _n_(9220, "df", lambda: df), "take"), [1, 2, 5]))
_l_(9224)
_c_(9226, _n_(9225, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(9227)
_c_(9232, _n_(9228, "print", lambda: print), _c_(9231, _a_(9230, _n_(9229, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(9233)
_c_(9235, _n_(9234, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(9236)
_c_(9241, _n_(9237, "print", lambda: print), _c_(9240, _a_(9239, _n_(9238, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(9242)