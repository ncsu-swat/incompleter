# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(79584)

except ImportError:
    pass
_c_(79587, _a_(79586, _n_(79585, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(79588)
df = _c_(79591, _a_(79590, _n_(79589, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3002, 3001, 3004, 3003, 3002, 3003, 3001], 'salesman_id': [5002, 5003, 5001, 5003, 5002, 5001, 5001, 5003, 5003, 5002, 5003, 5001]})
_l_(79592)
_c_(79594, _n_(79593, "print", lambda: print), 'Original Orders DataFrame:')
_l_(79595)
_c_(79598, _n_(79596, "print", lambda: print), _n_(79597, "df", lambda: df))
_l_(79599)
_c_(79601, _n_(79600, "print", lambda: print), "\nSplit the said data on 'salesman_id', 'customer_id' wise:")
_l_(79602)
result = _c_(79605, _a_(79604, _n_(79603, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id'])
_l_(79606)
for (name, group) in _n_(79607, "result", lambda: result):
    _l_(79619)

    _c_(79609, _n_(79608, "print", lambda: print), '\nGroup:')
    _l_(79610)
    _c_(79613, _n_(79611, "print", lambda: print), _n_(79612, "name", lambda: name))
    _l_(79614)
    _c_(79617, _n_(79615, "print", lambda: print), _n_(79616, "group", lambda: group))
    _l_(79618)
n = 2
_l_(79620)
_c_(79622, _n_(79621, "print", lambda: print), '\nDroping last two records:')
_l_(79623)
_c_(79626, _n_(79624, "print", lambda: print), _n_(79625, "result1", lambda: result1))
_l_(79627)