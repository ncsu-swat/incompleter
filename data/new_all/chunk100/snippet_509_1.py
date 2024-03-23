# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52542)

except ImportError:
    pass
try:
    import numpy as np
    _l_(52544)

except ImportError:
    pass
_c_(52547, _a_(52546, _n_(52545, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(52548)
df = _c_(52567, _a_(52550, _n_(52549, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, _a_(52552, _n_(52551, "np", lambda: np), "nan"), 70002, 70004, _a_(52554, _n_(52553, "np", lambda: np), "nan"), 70005, _a_(52556, _n_(52555, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(52558, _n_(52557, "np", lambda: np), "nan"), 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', _a_(52560, _n_(52559, "np", lambda: np), "nan"), '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001], 'salesman_id': [5002, 5003, 5001, _a_(52562, _n_(52561, "np", lambda: np), "nan"), 5002, 5001, 5001, _a_(52564, _n_(52563, "np", lambda: np), "nan"), 5003, 5002, 5003, _a_(52566, _n_(52565, "np", lambda: np), "nan")]})
_l_(52568)
_c_(52570, _n_(52569, "print", lambda: print), 'Original Orders DataFrame:')
_l_(52571)
_c_(52574, _n_(52572, "print", lambda: print), _n_(52573, "df", lambda: df))
_l_(52575)
_c_(52577, _n_(52576, "print", lambda: print), '\nReplace NaNs with a single constant value:')
_l_(52578)
_c_(52581, _n_(52579, "print", lambda: print), _n_(52580, "result", lambda: result))
_l_(52582)