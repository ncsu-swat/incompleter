# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(78242)

except ImportError:
    pass
try:
    import numpy as np
    _l_(78244)

except ImportError:
    pass
num_state = _c_(78248, _a_(78247, _a_(78246, _n_(78245, "np", lambda: np), "random"), "RandomState"), 100)
_l_(78249)
num_series = _c_(78255, _a_(78251, _n_(78250, "pd", lambda: pd), "Series"), _c_(78254, _a_(78253, _n_(78252, "num_state", lambda: num_state), "normal"), 10, 4, 20))
_l_(78256)
_c_(78258, _n_(78257, "print", lambda: print), 'Original Series:')
_l_(78259)
_c_(78262, _n_(78260, "print", lambda: print), _n_(78261, "num_series", lambda: num_series))
_l_(78263)
_c_(78265, _n_(78264, "print", lambda: print), '\nMinimum, 25th percentile, median, 75th, and maximum of a given series:')
_l_(78266)
_c_(78269, _n_(78267, "print", lambda: print), _n_(78268, "result", lambda: result))
_l_(78270)