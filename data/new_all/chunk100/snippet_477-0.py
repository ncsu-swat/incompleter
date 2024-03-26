# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(117938)

except ImportError:
    pass
try:
    import numpy as np
    _l_(117940)

except ImportError:
    pass
_c_(117943, _a_(117942, _n_(117941, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(117944)
df = _c_(117957, _a_(117946, _n_(117945, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, _a_(117948, _n_(117947, "np", lambda: np), "nan"), 70002, 70004, _a_(117950, _n_(117949, "np", lambda: np), "nan"), 70005, '--', 70010, 70003, 70012, _a_(117952, _n_(117951, "np", lambda: np), "nan"), 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, '?', 12.43, 2480.4, 250.45, 3045.6], 'ord_date': ['?', '2012-09-10', _a_(117954, _n_(117953, "np", lambda: np), "nan"), '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, '--', 3002, 3001, 3001], 'salesman_id': [5002, 5003, '?', 5001, _a_(117956, _n_(117955, "np", lambda: np), "nan"), 5002, 5001, '?', 5003, 5002, 5003, '--']})
_l_(117958)
_c_(117960, _n_(117959, "print", lambda: print), 'Original Orders DataFrame:')
_l_(117961)
_c_(117964, _n_(117962, "print", lambda: print), _n_(117963, "df", lambda: df))
_l_(117965)
_c_(117967, _n_(117966, "print", lambda: print), '\nReplace the missing values with NaN:')
_l_(117968)
_c_(117971, _n_(117969, "print", lambda: print), _n_(117970, "result", lambda: result))
_l_(117972)