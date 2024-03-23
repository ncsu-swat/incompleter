# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87664)

except ImportError:
    pass
try:
    import numpy as np
    _l_(87666)

except ImportError:
    pass
_c_(87669, _a_(87668, _n_(87667, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(87670)
_c_(87672, _n_(87671, "print", lambda: print), 'Original Orders DataFrame:')
_l_(87673)
_c_(87676, _n_(87674, "print", lambda: print), _n_(87675, "df", lambda: df))
_l_(87677)
_c_(87679, _n_(87678, "print", lambda: print), '\nDrop those rows in which specific columns have missing values:')
_l_(87680)
result = _c_(87683, _a_(87682, _n_(87681, "df", lambda: df), "dropna"), subset=['ord_no', 'customer_id'])
_l_(87684)
_c_(87687, _n_(87685, "print", lambda: print), _n_(87686, "result", lambda: result))
_l_(87688)