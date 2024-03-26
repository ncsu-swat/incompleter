# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(111791)

except ImportError:
    pass
try:
    import numpy as np
    _l_(111793)

except ImportError:
    pass
_c_(111797, _a_(111796, _a_(111795, _n_(111794, "np", lambda: np), "random"), "seed"), 24)
_l_(111798)
df = _c_(111811, _a_(111800, _n_(111799, "pd", lambda: pd), "concat"), [_n_(111801, "df", lambda: df), _c_(111810, _a_(111803, _n_(111802, "pd", lambda: pd), "DataFrame"), _c_(111807, _a_(111806, _a_(111805, _n_(111804, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(111809, _n_(111808, "list", lambda: list), 'BCDE'))], axis=1)
_l_(111812)
_a_(111814, _n_(111813, "df", lambda: df), "iloc")[0, 2] = _a_(111816, _n_(111815, "np", lambda: np), "nan")
_l_(111817)
_a_(111819, _n_(111818, "df", lambda: df), "iloc")[3, 3] = _a_(111821, _n_(111820, "np", lambda: np), "nan")
_l_(111822)
_a_(111824, _n_(111823, "df", lambda: df), "iloc")[4, 1] = _a_(111826, _n_(111825, "np", lambda: np), "nan")
_l_(111827)
_a_(111829, _n_(111828, "df", lambda: df), "iloc")[9, 4] = _a_(111831, _n_(111830, "np", lambda: np), "nan")
_l_(111832)
_c_(111834, _n_(111833, "print", lambda: print), 'Original array:')
_l_(111835)
_c_(111838, _n_(111836, "print", lambda: print), _n_(111837, "df", lambda: df))
_l_(111839)

def highlight_cols(s):
    _l_(111843)

    color = 'grey'
    _l_(111840)
    aux = 'background-color: %s' % _n_(111841, "color", lambda: color)
    _l_(111842)
    return aux
_c_(111845, _n_(111844, "print", lambda: print), '\nHighlight specific columns:')
_l_(111846)
_c_(111853, _a_(111849, _a_(111848, _n_(111847, "df", lambda: df), "style"), "applymap"), _n_(111850, "highlight_cols", lambda: highlight_cols), subset=_a_(111852, _n_(111851, "pd", lambda: pd), "IndexSlice")[:, ['B', 'C']])
_l_(111854)