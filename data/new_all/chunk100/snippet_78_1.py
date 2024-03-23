# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(79477)

except ImportError:
    pass
_c_(79480, _a_(79479, _n_(79478, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(79481)
df = _c_(79484, _a_(79483, _n_(79482, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3002, 3001, 3004, 3003, 3002, 3003, 3001], 'salesman_id': [5002, 5003, 5001, 5003, 5002, 5001, 5001, 5003, 5003, 5002, 5003, 5001]})
_l_(79485)
_c_(79487, _n_(79486, "print", lambda: print), 'Original Orders DataFrame:')
_l_(79488)
_c_(79491, _n_(79489, "print", lambda: print), _n_(79490, "df", lambda: df))
_l_(79492)
_c_(79494, _n_(79493, "print", lambda: print), "\nSplit the said data on 'salesman_id', 'customer_id' wise:")
_l_(79495)
for (name, group) in _n_(79496, "result", lambda: result):
    _l_(79508)

    _c_(79498, _n_(79497, "print", lambda: print), '\nGroup:')
    _l_(79499)
    _c_(79502, _n_(79500, "print", lambda: print), _n_(79501, "name", lambda: name))
    _l_(79503)
    _c_(79506, _n_(79504, "print", lambda: print), _n_(79505, "group", lambda: group))
    _l_(79507)
n = 2
_l_(79509)
_c_(79511, _n_(79510, "print", lambda: print), '\nDroping last two records:')
_l_(79512)
result1 = _c_(79522, _a_(79514, _n_(79513, "df", lambda: df), "drop"), _a_(79521, _c_(79520, _a_(79518, _c_(79517, _a_(79516, _n_(79515, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id']), "tail"), _n_(79519, "n", lambda: n)), "index"), axis=0)
_l_(79523)
_c_(79526, _n_(79524, "print", lambda: print), _n_(79525, "result1", lambda: result1))
_l_(79527)