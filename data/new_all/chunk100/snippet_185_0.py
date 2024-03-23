# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(14628)

except ImportError:
    pass
try:
    import numpy as np
    _l_(14630)

except ImportError:
    pass
_c_(14634, _a_(14633, _a_(14632, _n_(14631, "np", lambda: np), "random"), "seed"), 24)
_l_(14635)
df = _c_(14648, _a_(14637, _n_(14636, "pd", lambda: pd), "concat"), [_n_(14638, "df", lambda: df), _c_(14647, _a_(14640, _n_(14639, "pd", lambda: pd), "DataFrame"), _c_(14644, _a_(14643, _a_(14642, _n_(14641, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(14646, _n_(14645, "list", lambda: list), 'BCDE'))], axis=1)
_l_(14649)
_a_(14651, _n_(14650, "df", lambda: df), "iloc")[0, 2] = _a_(14653, _n_(14652, "np", lambda: np), "nan")
_l_(14654)
_a_(14656, _n_(14655, "df", lambda: df), "iloc")[3, 3] = _a_(14658, _n_(14657, "np", lambda: np), "nan")
_l_(14659)
_a_(14661, _n_(14660, "df", lambda: df), "iloc")[4, 1] = _a_(14663, _n_(14662, "np", lambda: np), "nan")
_l_(14664)
_a_(14666, _n_(14665, "df", lambda: df), "iloc")[9, 4] = _a_(14668, _n_(14667, "np", lambda: np), "nan")
_l_(14669)
_c_(14671, _n_(14670, "print", lambda: print), 'Original array:')
_l_(14672)
_c_(14675, _n_(14673, "print", lambda: print), _n_(14674, "df", lambda: df))
_l_(14676)

def color_negative_red(val):
    _l_(14681)

    color = 'red' if _n_(14677, "val", lambda: val) < 0 else 'black'
    _l_(14678)
    aux = 'color: %s' % _n_(14679, "color", lambda: color)
    _l_(14680)
    return aux
_c_(14683, _n_(14682, "print", lambda: print), '\nNegative numbers red and positive numbers black:')
_l_(14684)
_c_(14688, _a_(14687, _a_(14686, _n_(14685, "df", lambda: df), "style"), "highlight_null"), null_color='red')
_l_(14689)