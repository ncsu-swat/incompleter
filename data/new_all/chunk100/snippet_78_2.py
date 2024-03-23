# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(79529)

except ImportError:
    pass
_c_(79532, _a_(79531, _n_(79530, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(79533)
df = _c_(79536, _a_(79535, _n_(79534, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3002, 3001, 3004, 3003, 3002, 3003, 3001], 'salesman_id': [5002, 5003, 5001, 5003, 5002, 5001, 5001, 5003, 5003, 5002, 5003, 5001]})
_l_(79537)
_c_(79539, _n_(79538, "print", lambda: print), 'Original Orders DataFrame:')
_l_(79540)
_c_(79543, _n_(79541, "print", lambda: print), _n_(79542, "df", lambda: df))
_l_(79544)
_c_(79546, _n_(79545, "print", lambda: print), "\nSplit the said data on 'salesman_id', 'customer_id' wise:")
_l_(79547)
result = _c_(79550, _a_(79549, _n_(79548, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id'])
_l_(79551)
for (name, group) in _n_(79552, "result", lambda: result):
    _l_(79564)

    _c_(79554, _n_(79553, "print", lambda: print), '\nGroup:')
    _l_(79555)
    _c_(79558, _n_(79556, "print", lambda: print), _n_(79557, "name", lambda: name))
    _l_(79559)
    _c_(79562, _n_(79560, "print", lambda: print), _n_(79561, "group", lambda: group))
    _l_(79563)
_c_(79566, _n_(79565, "print", lambda: print), '\nDroping last two records:')
_l_(79567)
result1 = _c_(79577, _a_(79569, _n_(79568, "df", lambda: df), "drop"), _a_(79576, _c_(79575, _a_(79573, _c_(79572, _a_(79571, _n_(79570, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id']), "tail"), _n_(79574, "n", lambda: n)), "index"), axis=0)
_l_(79578)
_c_(79581, _n_(79579, "print", lambda: print), _n_(79580, "result1", lambda: result1))
_l_(79582)