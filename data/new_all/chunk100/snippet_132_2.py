# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(8903)

except ImportError:
    pass
try:
    import numpy as np
    _l_(8905)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(8907)

except ImportError:
    pass
_c_(8911, _a_(8910, _a_(8909, _n_(8908, "np", lambda: np), "random"), "seed"), 24)
_l_(8912)
df = _c_(8925, _a_(8914, _n_(8913, "pd", lambda: pd), "concat"), [_n_(8915, "df", lambda: df), _c_(8924, _a_(8917, _n_(8916, "pd", lambda: pd), "DataFrame"), _c_(8921, _a_(8920, _a_(8919, _n_(8918, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(8923, _n_(8922, "list", lambda: list), 'BCDE'))], axis=1)
_l_(8926)
_c_(8928, _n_(8927, "print", lambda: print), 'Original array:')
_l_(8929)
_c_(8932, _n_(8930, "print", lambda: print), _n_(8931, "df", lambda: df))
_l_(8933)
_c_(8935, _n_(8934, "print", lambda: print), '\nDataframe - Heatmap style:')
_l_(8936)
cm = _c_(8939, _a_(8938, _n_(8937, "sns", lambda: sns), "light_palette"), 'red', as_cmap=True)
_l_(8940)
_c_(8944, _a_(8943, _a_(8942, _n_(8941, "df", lambda: df), "style"), "background_gradient"), cmap='viridis')
_l_(8945)