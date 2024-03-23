# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(8866)

except ImportError:
    pass
try:
    import numpy as np
    _l_(8868)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(8870)

except ImportError:
    pass
_c_(8874, _a_(8873, _a_(8872, _n_(8871, "np", lambda: np), "random"), "seed"), 24)
_l_(8875)
df = _c_(8881, _a_(8877, _n_(8876, "pd", lambda: pd), "DataFrame"), {'A': _c_(8880, _a_(8879, _n_(8878, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(8882)
_c_(8884, _n_(8883, "print", lambda: print), 'Original array:')
_l_(8885)
_c_(8888, _n_(8886, "print", lambda: print), _n_(8887, "df", lambda: df))
_l_(8889)
_c_(8891, _n_(8890, "print", lambda: print), '\nDataframe - Heatmap style:')
_l_(8892)
cm = _c_(8895, _a_(8894, _n_(8893, "sns", lambda: sns), "light_palette"), 'red', as_cmap=True)
_l_(8896)
_c_(8900, _a_(8899, _a_(8898, _n_(8897, "df", lambda: df), "style"), "background_gradient"), cmap='viridis')
_l_(8901)