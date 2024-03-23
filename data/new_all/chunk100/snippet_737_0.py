# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(74232)

except ImportError:
    pass
try:
    import numpy as np
    _l_(74234)

except ImportError:
    pass
_c_(74238, _a_(74237, _a_(74236, _n_(74235, "np", lambda: np), "random"), "seed"), 24)
_l_(74239)
df = _c_(74252, _a_(74241, _n_(74240, "pd", lambda: pd), "concat"), [_n_(74242, "df", lambda: df), _c_(74251, _a_(74244, _n_(74243, "pd", lambda: pd), "DataFrame"), _c_(74248, _a_(74247, _a_(74246, _n_(74245, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(74250, _n_(74249, "list", lambda: list), 'BCDE'))], axis=1)
_l_(74253)
_a_(74255, _n_(74254, "df", lambda: df), "iloc")[0, 2] = _a_(74257, _n_(74256, "np", lambda: np), "nan")
_l_(74258)
_a_(74260, _n_(74259, "df", lambda: df), "iloc")[3, 3] = _a_(74262, _n_(74261, "np", lambda: np), "nan")
_l_(74263)
_a_(74265, _n_(74264, "df", lambda: df), "iloc")[4, 1] = _a_(74267, _n_(74266, "np", lambda: np), "nan")
_l_(74268)
_a_(74270, _n_(74269, "df", lambda: df), "iloc")[9, 4] = _a_(74272, _n_(74271, "np", lambda: np), "nan")
_l_(74273)
_c_(74275, _n_(74274, "print", lambda: print), 'Original array:')
_l_(74276)
_c_(74279, _n_(74277, "print", lambda: print), _n_(74278, "df", lambda: df))
_l_(74280)

def highlight_max(s):
    _l_(74289)

    """
    highlight the maximum in a Series green.
    """
    is_max = _n_(74281, "s", lambda: s) == _c_(74284, _a_(74283, _n_(74282, "s", lambda: s), "max"))
    _l_(74285)
    aux = ['background-color: green' if _n_(74286, "v", lambda: v) else '' for v in _n_(74287, "is_max", lambda: is_max)]
    _l_(74288)
    return aux
_c_(74291, _n_(74290, "print", lambda: print), '\nHighlight the maximum value in each column:')
_l_(74292)
_c_(74299, _a_(74295, _a_(74294, _n_(74293, "df", lambda: df), "style"), "apply"), _n_(74296, "highlight_max", lambda: highlight_max), subset=_a_(74298, _n_(74297, "pd", lambda: pd), "IndexSlice")[:, ['B', 'C', 'D', 'E']])
_l_(74300)