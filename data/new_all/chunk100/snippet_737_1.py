# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(74302)

except ImportError:
    pass
try:
    import numpy as np
    _l_(74304)

except ImportError:
    pass
_c_(74308, _a_(74307, _a_(74306, _n_(74305, "np", lambda: np), "random"), "seed"), 24)
_l_(74309)
df = _c_(74315, _a_(74311, _n_(74310, "pd", lambda: pd), "DataFrame"), {'A': _c_(74314, _a_(74313, _n_(74312, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(74316)
_a_(74318, _n_(74317, "df", lambda: df), "iloc")[0, 2] = _a_(74320, _n_(74319, "np", lambda: np), "nan")
_l_(74321)
_a_(74323, _n_(74322, "df", lambda: df), "iloc")[3, 3] = _a_(74325, _n_(74324, "np", lambda: np), "nan")
_l_(74326)
_a_(74328, _n_(74327, "df", lambda: df), "iloc")[4, 1] = _a_(74330, _n_(74329, "np", lambda: np), "nan")
_l_(74331)
_a_(74333, _n_(74332, "df", lambda: df), "iloc")[9, 4] = _a_(74335, _n_(74334, "np", lambda: np), "nan")
_l_(74336)
_c_(74338, _n_(74337, "print", lambda: print), 'Original array:')
_l_(74339)
_c_(74342, _n_(74340, "print", lambda: print), _n_(74341, "df", lambda: df))
_l_(74343)

def highlight_max(s):
    _l_(74352)

    """
    highlight the maximum in a Series green.
    """
    is_max = _n_(74344, "s", lambda: s) == _c_(74347, _a_(74346, _n_(74345, "s", lambda: s), "max"))
    _l_(74348)
    aux = ['background-color: green' if _n_(74349, "v", lambda: v) else '' for v in _n_(74350, "is_max", lambda: is_max)]
    _l_(74351)
    return aux
_c_(74354, _n_(74353, "print", lambda: print), '\nHighlight the maximum value in each column:')
_l_(74355)
_c_(74362, _a_(74358, _a_(74357, _n_(74356, "df", lambda: df), "style"), "apply"), _n_(74359, "highlight_max", lambda: highlight_max), subset=_a_(74361, _n_(74360, "pd", lambda: pd), "IndexSlice")[:, ['B', 'C', 'D', 'E']])
_l_(74363)