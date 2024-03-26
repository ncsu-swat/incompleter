# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113941)

except ImportError:
    pass
_c_(113944, _a_(113943, _n_(113942, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(113945)
df = _c_(113948, _a_(113947, _n_(113946, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(113949)
_c_(113951, _n_(113950, "print", lambda: print), 'Original Orders DataFrame:')
_l_(113952)
_c_(113955, _n_(113953, "print", lambda: print), _n_(113954, "df", lambda: df))
_l_(113956)
df_agg = _c_(113962, _a_(113960, _c_(113959, _a_(113958, _n_(113957, "df", lambda: df), "groupby"), ['customer_id', 'salesman_id']), "agg"), {'purch_amt': _n_(113961, "sum", lambda: sum)})
_l_(113963)
_c_(113965, _n_(113964, "print", lambda: print), "\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
_l_(113966)
_c_(113971, _n_(113967, "print", lambda: print), _c_(113970, _a_(113969, _n_(113968, "result", lambda: result), "nlargest")))
_l_(113972)