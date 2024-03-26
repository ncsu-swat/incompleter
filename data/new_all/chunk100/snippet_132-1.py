# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(101802)

except ImportError:
    pass
try:
    import numpy as np
    _l_(101804)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(101806)

except ImportError:
    pass
_c_(101810, _a_(101809, _a_(101808, _n_(101807, "np", lambda: np), "random"), "seed"), 24)
_l_(101811)
df = _c_(101824, _a_(101813, _n_(101812, "pd", lambda: pd), "concat"), [_n_(101814, "df", lambda: df), _c_(101823, _a_(101816, _n_(101815, "pd", lambda: pd), "DataFrame"), _c_(101820, _a_(101819, _a_(101818, _n_(101817, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(101822, _n_(101821, "list", lambda: list), 'BCDE'))], axis=1)
_l_(101825)
_c_(101827, _n_(101826, "print", lambda: print), 'Original array:')
_l_(101828)
_c_(101831, _n_(101829, "print", lambda: print), _n_(101830, "df", lambda: df))
_l_(101832)
_c_(101834, _n_(101833, "print", lambda: print), '\nDataframe - Heatmap style:')
_l_(101835)
cm = _c_(101838, _a_(101837, _n_(101836, "sns", lambda: sns), "light_palette"), 'red', as_cmap=True)
_l_(101839)
_c_(101843, _a_(101842, _a_(101841, _n_(101840, "df", lambda: df), "style"), "background_gradient"), cmap='viridis')
_l_(101844)