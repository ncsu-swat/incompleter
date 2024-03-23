# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(88057)

except ImportError:
    pass
_c_(88060, _a_(88059, _n_(88058, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(88061)
df = _c_(88064, _a_(88063, _n_(88062, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['05-10-2012', '09-10-2012', '05-10-2012', '08-17-2012', '10-09-2012', '07-27-2012', '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2012', '07-08-2012', '04-25-2012'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(88065)
_c_(88067, _n_(88066, "print", lambda: print), 'Original Orders DataFrame:')
_l_(88068)
_c_(88071, _n_(88069, "print", lambda: print), _n_(88070, "df", lambda: df))
_l_(88072)
_n_(88073, "df", lambda: df)['ord_date'] = _c_(88077, _a_(88075, _n_(88074, "pd", lambda: pd), "to_datetime"), _n_(88076, "df", lambda: df)['ord_date'])
_l_(88078)
_c_(88080, _n_(88079, "print", lambda: print), '\nQuartly purchase amount:')
_l_(88081)
_c_(88084, _n_(88082, "print", lambda: print), _n_(88083, "result", lambda: result))
_l_(88085)