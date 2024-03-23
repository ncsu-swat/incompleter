# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(22076)

except ImportError:
    pass
_c_(22079, _a_(22078, _n_(22077, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(22080)
df = _c_(22083, _a_(22082, _n_(22081, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['05-10-2012', '09-10-2012', '05-10-2013', '08-17-2013', '10-09-2013', '07-27-2014', '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2014', '07-08-2012', '04-25-2012'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(22084)
_c_(22086, _n_(22085, "print", lambda: print), 'Original Orders DataFrame:')
_l_(22087)
_c_(22090, _n_(22088, "print", lambda: print), _n_(22089, "df", lambda: df))
_l_(22091)
_n_(22092, "df", lambda: df)['ord_date'] = _c_(22096, _a_(22094, _n_(22093, "pd", lambda: pd), "to_datetime"), _n_(22095, "df", lambda: df)['ord_date'])
_l_(22097)
_c_(22099, _n_(22098, "print", lambda: print), '\nYear wise Month wise purchase amount:')
_l_(22100)
_c_(22103, _n_(22101, "print", lambda: print), _n_(22102, "result", lambda: result))
_l_(22104)