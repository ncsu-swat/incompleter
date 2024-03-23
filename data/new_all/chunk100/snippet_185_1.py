# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(14691)

except ImportError:
    pass
try:
    import numpy as np
    _l_(14693)

except ImportError:
    pass
_c_(14697, _a_(14696, _a_(14695, _n_(14694, "np", lambda: np), "random"), "seed"), 24)
_l_(14698)
df = _c_(14704, _a_(14700, _n_(14699, "pd", lambda: pd), "DataFrame"), {'A': _c_(14703, _a_(14702, _n_(14701, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(14705)
_a_(14707, _n_(14706, "df", lambda: df), "iloc")[0, 2] = _a_(14709, _n_(14708, "np", lambda: np), "nan")
_l_(14710)
_a_(14712, _n_(14711, "df", lambda: df), "iloc")[3, 3] = _a_(14714, _n_(14713, "np", lambda: np), "nan")
_l_(14715)
_a_(14717, _n_(14716, "df", lambda: df), "iloc")[4, 1] = _a_(14719, _n_(14718, "np", lambda: np), "nan")
_l_(14720)
_a_(14722, _n_(14721, "df", lambda: df), "iloc")[9, 4] = _a_(14724, _n_(14723, "np", lambda: np), "nan")
_l_(14725)
_c_(14727, _n_(14726, "print", lambda: print), 'Original array:')
_l_(14728)
_c_(14731, _n_(14729, "print", lambda: print), _n_(14730, "df", lambda: df))
_l_(14732)

def color_negative_red(val):
    _l_(14737)

    color = 'red' if _n_(14733, "val", lambda: val) < 0 else 'black'
    _l_(14734)
    aux = 'color: %s' % _n_(14735, "color", lambda: color)
    _l_(14736)
    return aux
_c_(14739, _n_(14738, "print", lambda: print), '\nNegative numbers red and positive numbers black:')
_l_(14740)
_c_(14744, _a_(14743, _a_(14742, _n_(14741, "df", lambda: df), "style"), "highlight_null"), null_color='red')
_l_(14745)