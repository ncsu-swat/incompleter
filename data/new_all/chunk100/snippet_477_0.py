# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(50113)

except ImportError:
    pass
try:
    import numpy as np
    _l_(50115)

except ImportError:
    pass
_c_(50118, _a_(50117, _n_(50116, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(50119)
_c_(50121, _n_(50120, "print", lambda: print), 'Original Orders DataFrame:')
_l_(50122)
_c_(50125, _n_(50123, "print", lambda: print), _n_(50124, "df", lambda: df))
_l_(50126)
_c_(50128, _n_(50127, "print", lambda: print), '\nReplace the missing values with NaN:')
_l_(50129)
result = _c_(50136, _a_(50131, _n_(50130, "df", lambda: df), "replace"), {'?': _a_(50133, _n_(50132, "np", lambda: np), "nan"), '--': _a_(50135, _n_(50134, "np", lambda: np), "nan")})
_l_(50137)
_c_(50140, _n_(50138, "print", lambda: print), _n_(50139, "result", lambda: result))
_l_(50141)