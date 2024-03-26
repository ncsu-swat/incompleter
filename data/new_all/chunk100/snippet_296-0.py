# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(109018)

except ImportError:
    pass
try:
    import numpy as np
    _l_(109020)

except ImportError:
    pass
_c_(109023, _a_(109022, _n_(109021, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(109024)
_c_(109026, _n_(109025, "print", lambda: print), 'Original Orders DataFrame:')
_l_(109027)
_c_(109030, _n_(109028, "print", lambda: print), _n_(109029, "df", lambda: df))
_l_(109031)
_c_(109033, _n_(109032, "print", lambda: print), '\nInterpolate the missing values using the Linear Interpolation method (purch_amt):')
_l_(109034)
_c_(109037, _a_(109036, _n_(109035, "df", lambda: df)['purch_amt'], "interpolate"), method='linear', direction='forward', inplace=True)
_l_(109038)
_c_(109041, _n_(109039, "print", lambda: print), _n_(109040, "df", lambda: df))
_l_(109042)