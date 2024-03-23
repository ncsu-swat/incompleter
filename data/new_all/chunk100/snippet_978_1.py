# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(98058)

except ImportError:
    pass
try:
    import numpy as np
    _l_(98060)

except ImportError:
    pass
_c_(98063, _a_(98062, _n_(98061, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(98064)
df = _c_(98083, _a_(98066, _n_(98065, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, _a_(98068, _n_(98067, "np", lambda: np), "nan"), 70002, 70004, _a_(98070, _n_(98069, "np", lambda: np), "nan"), 70005, _a_(98072, _n_(98071, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(98074, _n_(98073, "np", lambda: np), "nan"), 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', _a_(98076, _n_(98075, "np", lambda: np), "nan"), '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001], 'salesman_id': [5002, 5003, 5001, _a_(98078, _n_(98077, "np", lambda: np), "nan"), 5002, 5001, 5001, _a_(98080, _n_(98079, "np", lambda: np), "nan"), 5003, 5002, 5003, _a_(98082, _n_(98081, "np", lambda: np), "nan")]})
_l_(98084)
_c_(98086, _n_(98085, "print", lambda: print), 'Original Orders DataFrame:')
_l_(98087)
_c_(98090, _n_(98088, "print", lambda: print), _n_(98089, "df", lambda: df))
_l_(98091)
_c_(98093, _n_(98092, "print", lambda: print), '\nDrop the columns where at least one element is missing:')
_l_(98094)
_c_(98097, _n_(98095, "print", lambda: print), _n_(98096, "result", lambda: result))
_l_(98098)