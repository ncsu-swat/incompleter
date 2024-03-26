# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(106584)

except ImportError:
    pass
try:
    import numpy as np
    _l_(106586)

except ImportError:
    pass
_c_(106589, _a_(106588, _n_(106587, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(106590)
df = _c_(106621, _a_(106592, _n_(106591, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, _a_(106594, _n_(106593, "np", lambda: np), "nan"), 70002, 70004, _a_(106596, _n_(106595, "np", lambda: np), "nan"), 70005, _a_(106598, _n_(106597, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(106600, _n_(106599, "np", lambda: np), "nan"), 70013], 'purch_amt': [150.5, _a_(106602, _n_(106601, "np", lambda: np), "nan"), 65.26, 110.5, 948.5, _a_(106604, _n_(106603, "np", lambda: np), "nan"), 5760, 1983.43, _a_(106606, _n_(106605, "np", lambda: np), "nan"), 250.45, 75.29, 3045.6], 'sale_amt': [10.5, 20.65, _a_(106608, _n_(106607, "np", lambda: np), "nan"), 11.5, 98.5, _a_(106610, _n_(106609, "np", lambda: np), "nan"), 57, 19.43, _a_(106612, _n_(106611, "np", lambda: np), "nan"), 25.45, 75.29, 35.6], 'ord_date': ['2012-10-05', '2012-09-10', _a_(106614, _n_(106613, "np", lambda: np), "nan"), '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001], 'salesman_id': [5002, 5003, 5001, _a_(106616, _n_(106615, "np", lambda: np), "nan"), 5002, 5001, 5001, _a_(106618, _n_(106617, "np", lambda: np), "nan"), 5003, 5002, 5003, _a_(106620, _n_(106619, "np", lambda: np), "nan")]})
_l_(106622)
_c_(106624, _n_(106623, "print", lambda: print), 'Original Orders DataFrame:')
_l_(106625)
_c_(106628, _n_(106626, "print", lambda: print), _n_(106627, "df", lambda: df))
_l_(106629)
_c_(106631, _n_(106630, "print", lambda: print), '\nReplace the missing values with the most frequent values present in each column:')
_l_(106632)
_c_(106635, _n_(106633, "print", lambda: print), _n_(106634, "result", lambda: result))
_l_(106636)