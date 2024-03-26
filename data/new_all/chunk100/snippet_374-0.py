# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113065)

except ImportError:
    pass
try:
    import numpy as np
    _l_(113067)

except ImportError:
    pass
_c_(113071, _a_(113070, _a_(113069, _n_(113068, "np", lambda: np), "random"), "seed"), 24)
_l_(113072)
df = _c_(113085, _a_(113074, _n_(113073, "pd", lambda: pd), "concat"), [_n_(113075, "df", lambda: df), _c_(113084, _a_(113077, _n_(113076, "pd", lambda: pd), "DataFrame"), _c_(113081, _a_(113080, _a_(113079, _n_(113078, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(113083, _n_(113082, "list", lambda: list), 'BCDE'))], axis=1)
_l_(113086)
_a_(113088, _n_(113087, "df", lambda: df), "iloc")[0, 2] = _a_(113090, _n_(113089, "np", lambda: np), "nan")
_l_(113091)
_a_(113093, _n_(113092, "df", lambda: df), "iloc")[3, 3] = _a_(113095, _n_(113094, "np", lambda: np), "nan")
_l_(113096)
_a_(113098, _n_(113097, "df", lambda: df), "iloc")[4, 1] = _a_(113100, _n_(113099, "np", lambda: np), "nan")
_l_(113101)
_a_(113103, _n_(113102, "df", lambda: df), "iloc")[9, 4] = _a_(113105, _n_(113104, "np", lambda: np), "nan")
_l_(113106)
_c_(113108, _n_(113107, "print", lambda: print), 'Original array:')
_l_(113109)
_c_(113112, _n_(113110, "print", lambda: print), _n_(113111, "df", lambda: df))
_l_(113113)
_c_(113115, _n_(113114, "print", lambda: print), '\nBackground:black - fontcolor:yelow')
_l_(113116)
_c_(113120, _a_(113119, _a_(113118, _n_(113117, "df", lambda: df), "style"), "set_properties"), **{'background-color': 'black', 'color': 'yellow'})
_l_(113121)