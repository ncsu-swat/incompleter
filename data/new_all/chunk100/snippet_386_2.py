# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(38622)

except ImportError:
    pass
_c_(38625, _a_(38624, _n_(38623, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(38626)
df = _c_(38629, _a_(38628, _n_(38627, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(38630)
_c_(38632, _n_(38631, "print", lambda: print), 'Original Orders DataFrame:')
_l_(38633)
_c_(38636, _n_(38634, "print", lambda: print), _n_(38635, "df", lambda: df))
_l_(38637)
df_agg = _c_(38643, _a_(38641, _c_(38640, _a_(38639, _n_(38638, "df", lambda: df), "groupby"), ['customer_id', 'salesman_id']), "agg"), {'purch_amt': _n_(38642, "sum", lambda: sum)})
_l_(38644)
_c_(38646, _n_(38645, "print", lambda: print), "\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
_l_(38647)
_c_(38652, _n_(38648, "print", lambda: print), _c_(38651, _a_(38650, _n_(38649, "result", lambda: result), "nlargest")))
_l_(38653)