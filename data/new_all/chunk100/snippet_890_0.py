# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87604)

except ImportError:
    pass
try:
    import numpy as np
    _l_(87606)

except ImportError:
    pass
_c_(87609, _a_(87608, _n_(87607, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(87610)
df = _c_(87647, _a_(87612, _n_(87611, "pd", lambda: pd), "DataFrame"), {'ord_no': [_a_(87614, _n_(87613, "np", lambda: np), "nan"), _a_(87616, _n_(87615, "np", lambda: np), "nan"), 70002, _a_(87618, _n_(87617, "np", lambda: np), "nan"), _a_(87620, _n_(87619, "np", lambda: np), "nan"), 70005, _a_(87622, _n_(87621, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(87624, _n_(87623, "np", lambda: np), "nan"), _a_(87626, _n_(87625, "np", lambda: np), "nan")], 'purch_amt': [_a_(87628, _n_(87627, "np", lambda: np), "nan"), 270.65, 65.26, _a_(87630, _n_(87629, "np", lambda: np), "nan"), 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, _a_(87632, _n_(87631, "np", lambda: np), "nan")], 'ord_date': [_a_(87634, _n_(87633, "np", lambda: np), "nan"), '2012-09-10', _a_(87636, _n_(87635, "np", lambda: np), "nan"), _a_(87638, _n_(87637, "np", lambda: np), "nan"), '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', _a_(87640, _n_(87639, "np", lambda: np), "nan")], 'customer_id': [_a_(87642, _n_(87641, "np", lambda: np), "nan"), 3001, 3001, _a_(87644, _n_(87643, "np", lambda: np), "nan"), 3002, 3001, 3001, 3004, 3003, 3002, 3001, _a_(87646, _n_(87645, "np", lambda: np), "nan")]})
_l_(87648)
_c_(87650, _n_(87649, "print", lambda: print), 'Original Orders DataFrame:')
_l_(87651)
_c_(87654, _n_(87652, "print", lambda: print), _n_(87653, "df", lambda: df))
_l_(87655)
_c_(87657, _n_(87656, "print", lambda: print), '\nDrop those rows in which specific columns have missing values:')
_l_(87658)
_c_(87661, _n_(87659, "print", lambda: print), _n_(87660, "result", lambda: result))
_l_(87662)