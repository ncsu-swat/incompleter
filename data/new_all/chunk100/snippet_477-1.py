# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(117974)

except ImportError:
    pass
try:
    import numpy as np
    _l_(117976)

except ImportError:
    pass
_c_(117979, _a_(117978, _n_(117977, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(117980)
_c_(117982, _n_(117981, "print", lambda: print), 'Original Orders DataFrame:')
_l_(117983)
_c_(117986, _n_(117984, "print", lambda: print), _n_(117985, "df", lambda: df))
_l_(117987)
_c_(117989, _n_(117988, "print", lambda: print), '\nReplace the missing values with NaN:')
_l_(117990)
result = _c_(117997, _a_(117992, _n_(117991, "df", lambda: df), "replace"), {'?': _a_(117994, _n_(117993, "np", lambda: np), "nan"), '--': _a_(117996, _n_(117995, "np", lambda: np), "nan")})
_l_(117998)
_c_(118001, _n_(117999, "print", lambda: print), _n_(118000, "result", lambda: result))
_l_(118002)