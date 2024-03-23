# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(40443)

except ImportError:
    pass
try:
    import numpy as np
    _l_(40445)

except ImportError:
    pass
_c_(40448, _a_(40447, _n_(40446, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(40449)
df = _c_(40486, _a_(40451, _n_(40450, "pd", lambda: pd), "DataFrame"), {'ord_no': [_a_(40453, _n_(40452, "np", lambda: np), "nan"), _a_(40455, _n_(40454, "np", lambda: np), "nan"), 70002, _a_(40457, _n_(40456, "np", lambda: np), "nan"), _a_(40459, _n_(40458, "np", lambda: np), "nan"), 70005, _a_(40461, _n_(40460, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(40463, _n_(40462, "np", lambda: np), "nan"), _a_(40465, _n_(40464, "np", lambda: np), "nan")], 'purch_amt': [_a_(40467, _n_(40466, "np", lambda: np), "nan"), 270.65, 65.26, _a_(40469, _n_(40468, "np", lambda: np), "nan"), 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, _a_(40471, _n_(40470, "np", lambda: np), "nan")], 'ord_date': [_a_(40473, _n_(40472, "np", lambda: np), "nan"), '2012-09-10', _a_(40475, _n_(40474, "np", lambda: np), "nan"), _a_(40477, _n_(40476, "np", lambda: np), "nan"), '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', _a_(40479, _n_(40478, "np", lambda: np), "nan")], 'customer_id': [_a_(40481, _n_(40480, "np", lambda: np), "nan"), 3001, 3001, _a_(40483, _n_(40482, "np", lambda: np), "nan"), 3002, 3001, 3001, 3004, 3003, 3002, 3001, _a_(40485, _n_(40484, "np", lambda: np), "nan")]})
_l_(40487)
_c_(40489, _n_(40488, "print", lambda: print), 'Original Orders DataFrame:')
_l_(40490)
_c_(40493, _n_(40491, "print", lambda: print), _n_(40492, "df", lambda: df))
_l_(40494)
_c_(40496, _n_(40495, "print", lambda: print), '\nTotal number of missing values of the said DataFrame:')
_l_(40497)
_c_(40500, _n_(40498, "print", lambda: print), _n_(40499, "result", lambda: result))
_l_(40501)