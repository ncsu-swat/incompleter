# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(79045)

except ImportError:
    pass
try:
    import numpy as np
    _l_(79047)

except ImportError:
    pass
_c_(79051, _a_(79050, _a_(79049, _n_(79048, "np", lambda: np), "random"), "seed"), 24)
_l_(79052)
df = _c_(79058, _a_(79054, _n_(79053, "pd", lambda: pd), "DataFrame"), {'A': _c_(79057, _a_(79056, _n_(79055, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(79059)
_a_(79061, _n_(79060, "df", lambda: df), "iloc")[0, 2] = _a_(79063, _n_(79062, "np", lambda: np), "nan")
_l_(79064)
_a_(79066, _n_(79065, "df", lambda: df), "iloc")[3, 3] = _a_(79068, _n_(79067, "np", lambda: np), "nan")
_l_(79069)
_a_(79071, _n_(79070, "df", lambda: df), "iloc")[4, 1] = _a_(79073, _n_(79072, "np", lambda: np), "nan")
_l_(79074)
_a_(79076, _n_(79075, "df", lambda: df), "iloc")[9, 4] = _a_(79078, _n_(79077, "np", lambda: np), "nan")
_l_(79079)
_c_(79081, _n_(79080, "print", lambda: print), 'Original array:')
_l_(79082)
_c_(79085, _n_(79083, "print", lambda: print), _n_(79084, "df", lambda: df))
_l_(79086)

def highlight_max(s):
    _l_(79095)

    """
    highlight the maximum in a Series green.
    """
    is_max = _n_(79087, "s", lambda: s) == _c_(79090, _a_(79089, _n_(79088, "s", lambda: s), "max"))
    _l_(79091)
    aux = ['background-color: green' if _n_(79092, "v", lambda: v) else '' for v in _n_(79093, "is_max", lambda: is_max)]
    _l_(79094)
    return aux
_c_(79097, _n_(79096, "print", lambda: print), '\nHighlight the maximum value in last two columns:')
_l_(79098)
_c_(79105, _a_(79101, _a_(79100, _n_(79099, "df", lambda: df), "style"), "apply"), _n_(79102, "highlight_max", lambda: highlight_max), subset=_a_(79104, _n_(79103, "pd", lambda: pd), "IndexSlice")[:, ['D', 'E']])
_l_(79106)