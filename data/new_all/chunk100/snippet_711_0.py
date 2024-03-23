# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(72602)

except ImportError:
    pass
try:
    import datetime
    _l_(72604)

except ImportError:
    pass
dt_array = _c_(72614, _a_(72606, _n_(72605, "np", lambda: np), "array"), [_n_(72607, "start", lambda: start) + _c_(72611, _a_(72609, _n_(72608, "datetime", lambda: datetime), "timedelta"), hours=_n_(72610, "i", lambda: i)) for i in _c_(72613, _n_(72612, "range", lambda: range), 24)])
_l_(72615)
_c_(72618, _n_(72616, "print", lambda: print), _n_(72617, "dt_array", lambda: dt_array))
_l_(72619)