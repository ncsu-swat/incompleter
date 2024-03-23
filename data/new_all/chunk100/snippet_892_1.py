# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87826)

except ImportError:
    pass
try:
    import numpy as np
    _l_(87828)

except ImportError:
    pass
try:
    import datetime
    _l_(87830)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(87832)

except ImportError:
    pass
time_series = _c_(87840, _a_(87834, _n_(87833, "pd", lambda: pd), "Series"), _c_(87838, _a_(87837, _a_(87836, _n_(87835, "np", lambda: np), "random"), "randn"), 4), _n_(87839, "dates", lambda: dates))
_l_(87841)
_c_(87844, _n_(87842, "print", lambda: print), _n_(87843, "time_series", lambda: time_series))
_l_(87845)