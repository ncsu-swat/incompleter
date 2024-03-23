# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(19577)

except ImportError:
    pass
try:
    import numpy as np
    _l_(19579)

except ImportError:
    pass
_c_(19582, _a_(19581, _n_(19580, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(19583)
df = _c_(19614, _a_(19585, _n_(19584, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, _a_(19587, _n_(19586, "np", lambda: np), "nan"), 70002, 70004, _a_(19589, _n_(19588, "np", lambda: np), "nan"), 70005, _a_(19591, _n_(19590, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(19593, _n_(19592, "np", lambda: np), "nan"), 70013], 'purch_amt': [150.5, _a_(19595, _n_(19594, "np", lambda: np), "nan"), 65.26, 110.5, 948.5, _a_(19597, _n_(19596, "np", lambda: np), "nan"), 5760, 1983.43, _a_(19599, _n_(19598, "np", lambda: np), "nan"), 250.45, 75.29, 3045.6], 'sale_amt': [10.5, 20.65, _a_(19601, _n_(19600, "np", lambda: np), "nan"), 11.5, 98.5, _a_(19603, _n_(19602, "np", lambda: np), "nan"), 57, 19.43, _a_(19605, _n_(19604, "np", lambda: np), "nan"), 25.45, 75.29, 35.6], 'ord_date': ['2012-10-05', '2012-09-10', _a_(19607, _n_(19606, "np", lambda: np), "nan"), '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001], 'salesman_id': [5002, 5003, 5001, _a_(19609, _n_(19608, "np", lambda: np), "nan"), 5002, 5001, 5001, _a_(19611, _n_(19610, "np", lambda: np), "nan"), 5003, 5002, 5003, _a_(19613, _n_(19612, "np", lambda: np), "nan")]})
_l_(19615)
_c_(19617, _n_(19616, "print", lambda: print), 'Original Orders DataFrame:')
_l_(19618)
_c_(19621, _n_(19619, "print", lambda: print), _n_(19620, "df", lambda: df))
_l_(19622)
_c_(19624, _n_(19623, "print", lambda: print), '\nReplace the missing values with the most frequent values present in each column:')
_l_(19625)
_c_(19628, _n_(19626, "print", lambda: print), _n_(19627, "result", lambda: result))
_l_(19629)