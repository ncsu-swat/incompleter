# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(98465)

except ImportError:
    pass
_c_(98468, _a_(98467, _n_(98466, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(98469)
orders_data = _c_(98472, _a_(98471, _n_(98470, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(98473)
_c_(98475, _n_(98474, "print", lambda: print), 'Original Orders DataFrame:')
_l_(98476)
_c_(98479, _n_(98477, "print", lambda: print), _n_(98478, "orders_data", lambda: orders_data))
_l_(98480)
_c_(98482, _n_(98481, "print", lambda: print), '\nMean, min, and max values of purchase amount (purch_amt) group by customer id  (customer_id).')
_l_(98483)
_c_(98486, _n_(98484, "print", lambda: print), _n_(98485, "result", lambda: result))
_l_(98487)