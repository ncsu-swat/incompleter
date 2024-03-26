# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(107985)

except ImportError:
    pass
_c_(107988, _a_(107987, _n_(107986, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(107989)
df = _c_(107992, _a_(107991, _n_(107990, "pd", lambda: pd), "DataFrame"), {'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['05-10-2012', '09-10-2012', '05-10-2013', '08-17-2013', '10-09-2013', '07-27-2014', '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2014', '07-08-2012', '04-25-2012'], 'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005], 'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})
_l_(107993)
_c_(107995, _n_(107994, "print", lambda: print), 'Original Orders DataFrame:')
_l_(107996)
_c_(107999, _n_(107997, "print", lambda: print), _n_(107998, "df", lambda: df))
_l_(108000)
_n_(108001, "df", lambda: df)['ord_date'] = _c_(108005, _a_(108003, _n_(108002, "pd", lambda: pd), "to_datetime"), _n_(108004, "df", lambda: df)['ord_date'])
_l_(108006)
_c_(108008, _n_(108007, "print", lambda: print), '\nYear wise Month wise purchase amount:')
_l_(108009)
_c_(108012, _n_(108010, "print", lambda: print), _n_(108011, "result", lambda: result))
_l_(108013)