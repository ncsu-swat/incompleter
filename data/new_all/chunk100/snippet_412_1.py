# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(40503)

except ImportError:
    pass
try:
    import numpy as np
    _l_(40505)

except ImportError:
    pass
_c_(40508, _a_(40507, _n_(40506, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(40509)
_c_(40511, _n_(40510, "print", lambda: print), 'Original Orders DataFrame:')
_l_(40512)
_c_(40515, _n_(40513, "print", lambda: print), _n_(40514, "df", lambda: df))
_l_(40516)
_c_(40518, _n_(40517, "print", lambda: print), '\nTotal number of missing values of the said DataFrame:')
_l_(40519)
result = _c_(40526, _a_(40525, _c_(40524, _a_(40523, _c_(40522, _a_(40521, _n_(40520, "df", lambda: df), "isna")), "sum")), "sum"))
_l_(40527)
_c_(40530, _n_(40528, "print", lambda: print), _n_(40529, "result", lambda: result))
_l_(40531)