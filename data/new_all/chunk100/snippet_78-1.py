# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(120159)

except ImportError:
    pass
_c_(120162, _a_(120161, _n_(120160, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(120163)
df = _c_(120166, _a_(120165, _n_(120164, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3002, 3001, 3004, 3003, 3002, 3003, 3001], 'salesman_id': [5002, 5003, 5001, 5003, 5002, 5001, 5001, 5003, 5003, 5002, 5003, 5001]})
_l_(120167)
_c_(120169, _n_(120168, "print", lambda: print), 'Original Orders DataFrame:')
_l_(120170)
_c_(120173, _n_(120171, "print", lambda: print), _n_(120172, "df", lambda: df))
_l_(120174)
_c_(120176, _n_(120175, "print", lambda: print), "\nSplit the said data on 'salesman_id', 'customer_id' wise:")
_l_(120177)
result = _c_(120180, _a_(120179, _n_(120178, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id'])
_l_(120181)
for name, group in _n_(120182, "result", lambda: result):
    _l_(120194)

    _c_(120184, _n_(120183, "print", lambda: print), '\nGroup:')
    _l_(120185)
    _c_(120188, _n_(120186, "print", lambda: print), _n_(120187, "name", lambda: name))
    _l_(120189)
    _c_(120192, _n_(120190, "print", lambda: print), _n_(120191, "group", lambda: group))
    _l_(120193)
n = 2
_l_(120195)
_c_(120197, _n_(120196, "print", lambda: print), '\nDroping last two records:')
_l_(120198)
_c_(120201, _n_(120199, "print", lambda: print), _n_(120200, "result1", lambda: result1))
_l_(120202)