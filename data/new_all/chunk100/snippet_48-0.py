# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(118043)

except ImportError:
    pass
try:
    import numpy as np
    _l_(118045)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(118047)

except ImportError:
    pass
_c_(118051, _a_(118050, _a_(118049, _n_(118048, "np", lambda: np), "random"), "seed"), 24)
_l_(118052)
df = _c_(118065, _a_(118054, _n_(118053, "pd", lambda: pd), "concat"), [_n_(118055, "df", lambda: df), _c_(118064, _a_(118057, _n_(118056, "pd", lambda: pd), "DataFrame"), _c_(118061, _a_(118060, _a_(118059, _n_(118058, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(118063, _n_(118062, "list", lambda: list), 'BCDE'))], axis=1)
_l_(118066)
_c_(118068, _n_(118067, "print", lambda: print), 'Original array:')
_l_(118069)
_c_(118072, _n_(118070, "print", lambda: print), _n_(118071, "df", lambda: df))
_l_(118073)
_c_(118075, _n_(118074, "print", lambda: print), '\nDataframe - Gradient color:')
_l_(118076)
_c_(118080, _a_(118079, _a_(118078, _n_(118077, "df", lambda: df), "style"), "background_gradient"))
_l_(118081)