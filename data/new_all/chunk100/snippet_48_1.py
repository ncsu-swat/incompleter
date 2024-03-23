# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(51283)

except ImportError:
    pass
try:
    import numpy as np
    _l_(51285)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(51287)

except ImportError:
    pass
_c_(51291, _a_(51290, _a_(51289, _n_(51288, "np", lambda: np), "random"), "seed"), 24)
_l_(51292)
df = _c_(51305, _a_(51294, _n_(51293, "pd", lambda: pd), "concat"), [_n_(51295, "df", lambda: df), _c_(51304, _a_(51297, _n_(51296, "pd", lambda: pd), "DataFrame"), _c_(51301, _a_(51300, _a_(51299, _n_(51298, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(51303, _n_(51302, "list", lambda: list), 'BCDE'))], axis=1)
_l_(51306)
_c_(51308, _n_(51307, "print", lambda: print), 'Original array:')
_l_(51309)
_c_(51312, _n_(51310, "print", lambda: print), _n_(51311, "df", lambda: df))
_l_(51313)
_c_(51315, _n_(51314, "print", lambda: print), '\nDataframe - Gradient color:')
_l_(51316)
_c_(51320, _a_(51319, _a_(51318, _n_(51317, "df", lambda: df), "style"), "background_gradient"))
_l_(51321)