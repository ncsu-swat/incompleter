# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(9129)

except ImportError:
    pass
try:
    import numpy as np
    _l_(9131)

except ImportError:
    pass
sales_tuples = _c_(9136, _n_(9132, "list", lambda: list), _c_(9135, _n_(9133, "zip", lambda: zip), *_n_(9134, "sales_arrays", lambda: sales_arrays)))
_l_(9137)
sales_index = _c_(9142, _a_(9140, _a_(9139, _n_(9138, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(9141, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(9143)
_c_(9145, _n_(9144, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(9146)
df = _c_(9154, _a_(9148, _n_(9147, "pd", lambda: pd), "DataFrame"), _c_(9152, _a_(9151, _a_(9150, _n_(9149, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(9153, "sales_index", lambda: sales_index))
_l_(9155)
_c_(9158, _n_(9156, "print", lambda: print), _n_(9157, "df", lambda: df))
_l_(9159)
_c_(9161, _n_(9160, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(9162)
positions = [1, 2, 5]
_l_(9163)
_c_(9168, _n_(9164, "print", lambda: print), _c_(9167, _a_(9166, _n_(9165, "df", lambda: df), "take"), [1, 2, 5]))
_l_(9169)
_c_(9171, _n_(9170, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(9172)
_c_(9177, _n_(9173, "print", lambda: print), _c_(9176, _a_(9175, _n_(9174, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(9178)
_c_(9180, _n_(9179, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(9181)
_c_(9186, _n_(9182, "print", lambda: print), _c_(9185, _a_(9184, _n_(9183, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(9187)