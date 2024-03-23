# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(78302)

except ImportError:
    pass
try:
    import numpy as np
    _l_(78304)

except ImportError:
    pass
num_state = _c_(78308, _a_(78307, _a_(78306, _n_(78305, "np", lambda: np), "random"), "RandomState"), 100)
_l_(78309)
_c_(78311, _n_(78310, "print", lambda: print), 'Original Series:')
_l_(78312)
_c_(78315, _n_(78313, "print", lambda: print), _n_(78314, "num_series", lambda: num_series))
_l_(78316)
result = _c_(78320, _a_(78318, _n_(78317, "np", lambda: np), "percentile"), _n_(78319, "num_series", lambda: num_series), q=[0, 25, 50, 75, 100])
_l_(78321)
_c_(78323, _n_(78322, "print", lambda: print), '\nMinimum, 25th percentile, median, 75th, and maximum of a given series:')
_l_(78324)
_c_(78327, _n_(78325, "print", lambda: print), _n_(78326, "result", lambda: result))
_l_(78328)