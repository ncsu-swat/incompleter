# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(120902)

except ImportError:
    pass
_c_(120905, _a_(120904, _n_(120903, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(120906)
df = _c_(120909, _a_(120908, _n_(120907, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['05-10-2012', '09-10-2012', '05-10-2012', '08-17-2012', '10-09-2012', '07-27-2012', '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2012', '07-08-2012', '04-25-2012'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(120910)
_c_(120912, _n_(120911, "print", lambda: print), 'Original Orders DataFrame:')
_l_(120913)
_c_(120916, _n_(120914, "print", lambda: print), _n_(120915, "df", lambda: df))
_l_(120917)
_n_(120918, "df", lambda: df)['ord_date'] = _c_(120922, _a_(120920, _n_(120919, "pd", lambda: pd), "to_datetime"), _n_(120921, "df", lambda: df)['ord_date'])
_l_(120923)
_c_(120925, _n_(120924, "print", lambda: print), '\nMonth wise purchase amount:')
_l_(120926)
_c_(120929, _n_(120927, "print", lambda: print), _n_(120928, "result", lambda: result))
_l_(120930)