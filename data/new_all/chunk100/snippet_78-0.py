# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(120107)

except ImportError:
    pass
_c_(120110, _a_(120109, _n_(120108, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(120111)
df = _c_(120114, _a_(120113, _n_(120112, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3002, 3001, 3004, 3003, 3002, 3003, 3001], 'salesman_id': [5002, 5003, 5001, 5003, 5002, 5001, 5001, 5003, 5003, 5002, 5003, 5001]})
_l_(120115)
_c_(120117, _n_(120116, "print", lambda: print), 'Original Orders DataFrame:')
_l_(120118)
_c_(120121, _n_(120119, "print", lambda: print), _n_(120120, "df", lambda: df))
_l_(120122)
_c_(120124, _n_(120123, "print", lambda: print), "\nSplit the said data on 'salesman_id', 'customer_id' wise:")
_l_(120125)
for name, group in _n_(120126, "result", lambda: result):
    _l_(120138)

    _c_(120128, _n_(120127, "print", lambda: print), '\nGroup:')
    _l_(120129)
    _c_(120132, _n_(120130, "print", lambda: print), _n_(120131, "name", lambda: name))
    _l_(120133)
    _c_(120136, _n_(120134, "print", lambda: print), _n_(120135, "group", lambda: group))
    _l_(120137)
n = 2
_l_(120139)
_c_(120141, _n_(120140, "print", lambda: print), '\nDroping last two records:')
_l_(120142)
result1 = _c_(120152, _a_(120144, _n_(120143, "df", lambda: df), "drop"), _a_(120151, _c_(120150, _a_(120148, _c_(120147, _a_(120146, _n_(120145, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id']), "tail"), _n_(120149, "n", lambda: n)), "index"), axis=0)
_l_(120153)
_c_(120156, _n_(120154, "print", lambda: print), _n_(120155, "result1", lambda: result1))
_l_(120157)