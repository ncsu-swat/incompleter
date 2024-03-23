# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85860)

except ImportError:
    pass
_c_(85863, _a_(85862, _n_(85861, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(85864)
df = _c_(85867, _a_(85866, _n_(85865, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['05-10-2012', '09-10-2012', '05-10-2012', '08-17-2012', '10-09-2012', '07-27-2012', '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2012', '07-08-2012', '04-25-2012'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(85868)
_c_(85870, _n_(85869, "print", lambda: print), 'Original Orders DataFrame:')
_l_(85871)
_c_(85874, _n_(85872, "print", lambda: print), _n_(85873, "df", lambda: df))
_l_(85875)
_n_(85876, "df", lambda: df)['ord_date'] = _c_(85880, _a_(85878, _n_(85877, "pd", lambda: pd), "to_datetime"), _n_(85879, "df", lambda: df)['ord_date'])
_l_(85881)
_c_(85883, _n_(85882, "print", lambda: print), '\nMonth wise purchase amount:')
_l_(85884)
_c_(85887, _n_(85885, "print", lambda: print), _n_(85886, "result", lambda: result))
_l_(85888)