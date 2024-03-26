# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(121286)

except ImportError:
    pass
try:
    import numpy as np
    _l_(121288)

except ImportError:
    pass
_c_(121292, _a_(121291, _a_(121290, _n_(121289, "np", lambda: np), "random"), "seed"), 24)
_l_(121293)
df = _c_(121306, _a_(121295, _n_(121294, "pd", lambda: pd), "concat"), [_n_(121296, "df", lambda: df), _c_(121305, _a_(121298, _n_(121297, "pd", lambda: pd), "DataFrame"), _c_(121302, _a_(121301, _a_(121300, _n_(121299, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(121304, _n_(121303, "list", lambda: list), 'BCDE'))], axis=1)
_l_(121307)
_c_(121309, _n_(121308, "print", lambda: print), 'Original array:')
_l_(121310)
_c_(121313, _n_(121311, "print", lambda: print), _n_(121312, "df", lambda: df))
_l_(121314)
_c_(121316, _n_(121315, "print", lambda: print), '\nDataframe - Gradient color:')
_l_(121317)
_c_(121321, _a_(121320, _a_(121319, _n_(121318, "df", lambda: df), "style"), "background_gradient"), subset=['C'])
_l_(121322)