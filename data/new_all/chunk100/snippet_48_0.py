# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(51250)

except ImportError:
    pass
try:
    import numpy as np
    _l_(51252)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(51254)

except ImportError:
    pass
_c_(51258, _a_(51257, _a_(51256, _n_(51255, "np", lambda: np), "random"), "seed"), 24)
_l_(51259)
df = _c_(51265, _a_(51261, _n_(51260, "pd", lambda: pd), "DataFrame"), {'A': _c_(51264, _a_(51263, _n_(51262, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(51266)
_c_(51268, _n_(51267, "print", lambda: print), 'Original array:')
_l_(51269)
_c_(51272, _n_(51270, "print", lambda: print), _n_(51271, "df", lambda: df))
_l_(51273)
_c_(51275, _n_(51274, "print", lambda: print), '\nDataframe - Gradient color:')
_l_(51276)
_c_(51280, _a_(51279, _a_(51278, _n_(51277, "df", lambda: df), "style"), "background_gradient"))
_l_(51281)