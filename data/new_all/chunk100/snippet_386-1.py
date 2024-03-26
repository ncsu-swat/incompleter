# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113974)

except ImportError:
    pass
_c_(113977, _a_(113976, _n_(113975, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(113978)
df = _c_(113981, _a_(113980, _n_(113979, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(113982)
_c_(113984, _n_(113983, "print", lambda: print), 'Original Orders DataFrame:')
_l_(113985)
_c_(113988, _n_(113986, "print", lambda: print), _n_(113987, "df", lambda: df))
_l_(113989)
result = _c_(113992, _a_(113991, _n_(113990, "df_agg", lambda: df_agg)['purch_amt'], "groupby"), level=0, group_keys=False)
_l_(113993)
_c_(113995, _n_(113994, "print", lambda: print), "\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
_l_(113996)
_c_(114001, _n_(113997, "print", lambda: print), _c_(114000, _a_(113999, _n_(113998, "result", lambda: result), "nlargest")))
_l_(114002)