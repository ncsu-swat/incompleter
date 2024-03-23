# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(79371)

except ImportError:
    pass
try:
    import numpy as np
    _l_(79373)

except ImportError:
    pass
_c_(79376, _a_(79375, _n_(79374, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(79377)
df = _c_(79408, _a_(79379, _n_(79378, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, _a_(79381, _n_(79380, "np", lambda: np), "nan"), 70002, 70004, _a_(79383, _n_(79382, "np", lambda: np), "nan"), 70005, _a_(79385, _n_(79384, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(79387, _n_(79386, "np", lambda: np), "nan"), 70013], 'purch_amt': [150.5, _a_(79389, _n_(79388, "np", lambda: np), "nan"), 65.26, 110.5, 948.5, _a_(79391, _n_(79390, "np", lambda: np), "nan"), 5760, 1983.43, _a_(79393, _n_(79392, "np", lambda: np), "nan"), 250.45, 75.29, 3045.6], 'sale_amt': [10.5, 20.65, _a_(79395, _n_(79394, "np", lambda: np), "nan"), 11.5, 98.5, _a_(79397, _n_(79396, "np", lambda: np), "nan"), 57, 19.43, _a_(79399, _n_(79398, "np", lambda: np), "nan"), 25.45, 75.29, 35.6], 'ord_date': ['2012-10-05', '2012-09-10', _a_(79401, _n_(79400, "np", lambda: np), "nan"), '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001], 'salesman_id': [5002, 5003, 5001, _a_(79403, _n_(79402, "np", lambda: np), "nan"), 5002, 5001, 5001, _a_(79405, _n_(79404, "np", lambda: np), "nan"), 5003, 5002, 5003, _a_(79407, _n_(79406, "np", lambda: np), "nan")]})
_l_(79409)
_c_(79411, _n_(79410, "print", lambda: print), 'Original Orders DataFrame:')
_l_(79412)
_c_(79415, _n_(79413, "print", lambda: print), _n_(79414, "df", lambda: df))
_l_(79416)
_c_(79418, _n_(79417, "print", lambda: print), '\nMissing values in purch_amt column:')
_l_(79419)
_c_(79422, _n_(79420, "print", lambda: print), _n_(79421, "result", lambda: result))
_l_(79423)