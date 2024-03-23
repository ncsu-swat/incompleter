# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94211)

except ImportError:
    pass
try:
    import numpy as np
    _l_(94213)

except ImportError:
    pass
_c_(94217, _a_(94216, _a_(94215, _n_(94214, "np", lambda: np), "random"), "seed"), 24)
_l_(94218)
df = _c_(94224, _a_(94220, _n_(94219, "pd", lambda: pd), "DataFrame"), {'A': _c_(94223, _a_(94222, _n_(94221, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(94225)
_c_(94227, _n_(94226, "print", lambda: print), 'Original array:')
_l_(94228)
_c_(94231, _n_(94229, "print", lambda: print), _n_(94230, "df", lambda: df))
_l_(94232)
_c_(94234, _n_(94233, "print", lambda: print), '\nDataframe - Gradient color:')
_l_(94235)
_c_(94239, _a_(94238, _a_(94237, _n_(94236, "df", lambda: df), "style"), "background_gradient"), subset=['C'])
_l_(94240)