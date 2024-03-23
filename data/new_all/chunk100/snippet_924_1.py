# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94109)

except ImportError:
    pass
_c_(94112, _a_(94111, _n_(94110, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(94113)
df = _c_(94116, _a_(94115, _n_(94114, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(94117)
_c_(94119, _n_(94118, "print", lambda: print), 'Original Orders DataFrame:')
_l_(94120)
_c_(94123, _n_(94121, "print", lambda: print), _n_(94122, "df", lambda: df))
_l_(94124)
_c_(94126, _n_(94125, "print", lambda: print), "\nGroup on 'customer_id' and display the list of order dates in group wise:")
_l_(94127)
_c_(94130, _n_(94128, "print", lambda: print), _n_(94129, "result", lambda: result))
_l_(94131)