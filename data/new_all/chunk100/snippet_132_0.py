# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(8819)

except ImportError:
    pass
try:
    import numpy as np
    _l_(8821)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(8823)

except ImportError:
    pass
_c_(8827, _a_(8826, _a_(8825, _n_(8824, "np", lambda: np), "random"), "seed"), 24)
_l_(8828)
df = _c_(8834, _a_(8830, _n_(8829, "pd", lambda: pd), "DataFrame"), {'A': _c_(8833, _a_(8832, _n_(8831, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(8835)
df = _c_(8848, _a_(8837, _n_(8836, "pd", lambda: pd), "concat"), [_n_(8838, "df", lambda: df), _c_(8847, _a_(8840, _n_(8839, "pd", lambda: pd), "DataFrame"), _c_(8844, _a_(8843, _a_(8842, _n_(8841, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(8846, _n_(8845, "list", lambda: list), 'BCDE'))], axis=1)
_l_(8849)
_c_(8851, _n_(8850, "print", lambda: print), 'Original array:')
_l_(8852)
_c_(8855, _n_(8853, "print", lambda: print), _n_(8854, "df", lambda: df))
_l_(8856)
_c_(8858, _n_(8857, "print", lambda: print), '\nDataframe - Heatmap style:')
_l_(8859)
_c_(8863, _a_(8862, _a_(8861, _n_(8860, "df", lambda: df), "style"), "background_gradient"), cmap='viridis')
_l_(8864)