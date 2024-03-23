# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35091)

except ImportError:
    pass
try:
    import numpy as np
    _l_(35093)

except ImportError:
    pass
_c_(35097, _a_(35096, _a_(35095, _n_(35094, "np", lambda: np), "random"), "seed"), 24)
_l_(35098)
df = _c_(35111, _a_(35100, _n_(35099, "pd", lambda: pd), "concat"), [_n_(35101, "df", lambda: df), _c_(35110, _a_(35103, _n_(35102, "pd", lambda: pd), "DataFrame"), _c_(35107, _a_(35106, _a_(35105, _n_(35104, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(35109, _n_(35108, "list", lambda: list), 'BCDE'))], axis=1)
_l_(35112)
_a_(35114, _n_(35113, "df", lambda: df), "iloc")[0, 2] = _a_(35116, _n_(35115, "np", lambda: np), "nan")
_l_(35117)
_a_(35119, _n_(35118, "df", lambda: df), "iloc")[3, 3] = _a_(35121, _n_(35120, "np", lambda: np), "nan")
_l_(35122)
_a_(35124, _n_(35123, "df", lambda: df), "iloc")[4, 1] = _a_(35126, _n_(35125, "np", lambda: np), "nan")
_l_(35127)
_a_(35129, _n_(35128, "df", lambda: df), "iloc")[9, 4] = _a_(35131, _n_(35130, "np", lambda: np), "nan")
_l_(35132)
_c_(35134, _n_(35133, "print", lambda: print), 'Original array:')
_l_(35135)
_c_(35138, _n_(35136, "print", lambda: print), _n_(35137, "df", lambda: df))
_l_(35139)

def highlight_cols(s):
    _l_(35143)

    color = 'grey'
    _l_(35140)
    aux = 'background-color: %s' % _n_(35141, "color", lambda: color)
    _l_(35142)
    return aux
_c_(35145, _n_(35144, "print", lambda: print), '\nHighlight specific columns:')
_l_(35146)
_c_(35153, _a_(35149, _a_(35148, _n_(35147, "df", lambda: df), "style"), "applymap"), _n_(35150, "highlight_cols", lambda: highlight_cols), subset=_a_(35152, _n_(35151, "pd", lambda: pd), "IndexSlice")[:, ['B', 'C']])
_l_(35154)