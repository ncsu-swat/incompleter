# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(25347)

except ImportError:
    pass
try:
    import numpy as np
    _l_(25349)

except ImportError:
    pass
_c_(25352, _a_(25351, _n_(25350, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(25353)
_c_(25355, _n_(25354, "print", lambda: print), 'Original Orders DataFrame:')
_l_(25356)
_c_(25359, _n_(25357, "print", lambda: print), _n_(25358, "df", lambda: df))
_l_(25360)
_c_(25362, _n_(25361, "print", lambda: print), '\nInterpolate the missing values using the Linear Interpolation method (purch_amt):')
_l_(25363)
_c_(25366, _a_(25365, _n_(25364, "df", lambda: df)['purch_amt'], "interpolate"), method='linear', direction='forward', inplace=True)
_l_(25367)
_c_(25370, _n_(25368, "print", lambda: print), _n_(25369, "df", lambda: df))
_l_(25371)