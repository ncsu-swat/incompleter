# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(78272)

except ImportError:
    pass
try:
    import numpy as np
    _l_(78274)

except ImportError:
    pass
num_series = _c_(78280, _a_(78276, _n_(78275, "pd", lambda: pd), "Series"), _c_(78279, _a_(78278, _n_(78277, "num_state", lambda: num_state), "normal"), 10, 4, 20))
_l_(78281)
_c_(78283, _n_(78282, "print", lambda: print), 'Original Series:')
_l_(78284)
_c_(78287, _n_(78285, "print", lambda: print), _n_(78286, "num_series", lambda: num_series))
_l_(78288)
result = _c_(78292, _a_(78290, _n_(78289, "np", lambda: np), "percentile"), _n_(78291, "num_series", lambda: num_series), q=[0, 25, 50, 75, 100])
_l_(78293)
_c_(78295, _n_(78294, "print", lambda: print), '\nMinimum, 25th percentile, median, 75th, and maximum of a given series:')
_l_(78296)
_c_(78299, _n_(78297, "print", lambda: print), _n_(78298, "result", lambda: result))
_l_(78300)