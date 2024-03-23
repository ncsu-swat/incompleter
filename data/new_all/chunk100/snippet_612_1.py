# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(64610)

except ImportError:
    pass
try:
    import numpy as np
    _l_(64612)

except ImportError:
    pass
_c_(64615, _a_(64614, _n_(64613, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(64616)
df = _c_(64647, _a_(64618, _n_(64617, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, _a_(64620, _n_(64619, "np", lambda: np), "nan"), 70002, 70004, _a_(64622, _n_(64621, "np", lambda: np), "nan"), 70005, _a_(64624, _n_(64623, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(64626, _n_(64625, "np", lambda: np), "nan"), 70013], 'purch_amt': [150.5, _a_(64628, _n_(64627, "np", lambda: np), "nan"), 65.26, 110.5, 948.5, _a_(64630, _n_(64629, "np", lambda: np), "nan"), 5760, 1983.43, _a_(64632, _n_(64631, "np", lambda: np), "nan"), 250.45, 75.29, 3045.6], 'sale_amt': [10.5, 20.65, _a_(64634, _n_(64633, "np", lambda: np), "nan"), 11.5, 98.5, _a_(64636, _n_(64635, "np", lambda: np), "nan"), 57, 19.43, _a_(64638, _n_(64637, "np", lambda: np), "nan"), 25.45, 75.29, 35.6], 'ord_date': ['2012-10-05', '2012-09-10', _a_(64640, _n_(64639, "np", lambda: np), "nan"), '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001], 'salesman_id': [5002, 5003, 5001, _a_(64642, _n_(64641, "np", lambda: np), "nan"), 5002, 5001, 5001, _a_(64644, _n_(64643, "np", lambda: np), "nan"), 5003, 5002, 5003, _a_(64646, _n_(64645, "np", lambda: np), "nan")]})
_l_(64648)
_c_(64650, _n_(64649, "print", lambda: print), 'Original Orders DataFrame:')
_l_(64651)
_c_(64654, _n_(64652, "print", lambda: print), _n_(64653, "df", lambda: df))
_l_(64655)
_c_(64657, _n_(64656, "print", lambda: print), '\nMissing values in purch_amt column:')
_l_(64658)
_c_(64661, _n_(64659, "print", lambda: print), _n_(64660, "result", lambda: result))
_l_(64662)