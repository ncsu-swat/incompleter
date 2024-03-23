# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(50143)

except ImportError:
    pass
try:
    import numpy as np
    _l_(50145)

except ImportError:
    pass
_c_(50148, _a_(50147, _n_(50146, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(50149)
df = _c_(50162, _a_(50151, _n_(50150, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, _a_(50153, _n_(50152, "np", lambda: np), "nan"), 70002, 70004, _a_(50155, _n_(50154, "np", lambda: np), "nan"), 70005, '--', 70010, 70003, 70012, _a_(50157, _n_(50156, "np", lambda: np), "nan"), 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, '?', 12.43, 2480.4, 250.45, 3045.6], 'ord_date': ['?', '2012-09-10', _a_(50159, _n_(50158, "np", lambda: np), "nan"), '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, '--', 3002, 3001, 3001], 'salesman_id': [5002, 5003, '?', 5001, _a_(50161, _n_(50160, "np", lambda: np), "nan"), 5002, 5001, '?', 5003, 5002, 5003, '--']})
_l_(50163)
_c_(50165, _n_(50164, "print", lambda: print), 'Original Orders DataFrame:')
_l_(50166)
_c_(50169, _n_(50167, "print", lambda: print), _n_(50168, "df", lambda: df))
_l_(50170)
_c_(50172, _n_(50171, "print", lambda: print), '\nReplace the missing values with NaN:')
_l_(50173)
_c_(50176, _n_(50174, "print", lambda: print), _n_(50175, "result", lambda: result))
_l_(50177)