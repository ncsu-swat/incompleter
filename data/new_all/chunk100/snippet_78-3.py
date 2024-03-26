# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(120256)

except ImportError:
    pass
_c_(120259, _a_(120258, _n_(120257, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(120260)
df = _c_(120263, _a_(120262, _n_(120261, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3002, 3001, 3004, 3003, 3002, 3003, 3001], 'salesman_id': [5002, 5003, 5001, 5003, 5002, 5001, 5001, 5003, 5003, 5002, 5003, 5001]})
_l_(120264)
_c_(120266, _n_(120265, "print", lambda: print), 'Original Orders DataFrame:')
_l_(120267)
_c_(120270, _n_(120268, "print", lambda: print), _n_(120269, "df", lambda: df))
_l_(120271)
_c_(120273, _n_(120272, "print", lambda: print), "\nSplit the said data on 'salesman_id', 'customer_id' wise:")
_l_(120274)
result = _c_(120277, _a_(120276, _n_(120275, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id'])
_l_(120278)
for name, group in _n_(120279, "result", lambda: result):
    _l_(120291)

    _c_(120281, _n_(120280, "print", lambda: print), '\nGroup:')
    _l_(120282)
    _c_(120285, _n_(120283, "print", lambda: print), _n_(120284, "name", lambda: name))
    _l_(120286)
    _c_(120289, _n_(120287, "print", lambda: print), _n_(120288, "group", lambda: group))
    _l_(120290)
_c_(120293, _n_(120292, "print", lambda: print), '\nDroping last two records:')
_l_(120294)
result1 = _c_(120304, _a_(120296, _n_(120295, "df", lambda: df), "drop"), _a_(120303, _c_(120302, _a_(120300, _c_(120299, _a_(120298, _n_(120297, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id']), "tail"), _n_(120301, "n", lambda: n)), "index"), axis=0)
_l_(120305)
_c_(120308, _n_(120306, "print", lambda: print), _n_(120307, "result1", lambda: result1))
_l_(120309)