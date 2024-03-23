# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87886)

except ImportError:
    pass
try:
    import numpy as np
    _l_(87888)

except ImportError:
    pass
_c_(87892, _a_(87891, _a_(87890, _n_(87889, "np", lambda: np), "random"), "seed"), 24)
_l_(87893)
df = _c_(87906, _a_(87895, _n_(87894, "pd", lambda: pd), "concat"), [_n_(87896, "df", lambda: df), _c_(87905, _a_(87898, _n_(87897, "pd", lambda: pd), "DataFrame"), _c_(87902, _a_(87901, _a_(87900, _n_(87899, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(87904, _n_(87903, "list", lambda: list), 'BCDE'))], axis=1)
_l_(87907)
_a_(87909, _n_(87908, "df", lambda: df), "iloc")[0, 2] = _a_(87911, _n_(87910, "np", lambda: np), "nan")
_l_(87912)
_a_(87914, _n_(87913, "df", lambda: df), "iloc")[3, 3] = _a_(87916, _n_(87915, "np", lambda: np), "nan")
_l_(87917)
_a_(87919, _n_(87918, "df", lambda: df), "iloc")[4, 1] = _a_(87921, _n_(87920, "np", lambda: np), "nan")
_l_(87922)
_a_(87924, _n_(87923, "df", lambda: df), "iloc")[9, 4] = _a_(87926, _n_(87925, "np", lambda: np), "nan")
_l_(87927)
_c_(87929, _n_(87928, "print", lambda: print), 'Original array:')
_l_(87930)
_c_(87933, _n_(87931, "print", lambda: print), _n_(87932, "df", lambda: df))
_l_(87934)

def highlight_min(s):
    _l_(87943)

    """
    highlight the minimum in a Series red.
    """
    is_max = _n_(87935, "s", lambda: s) == _c_(87938, _a_(87937, _n_(87936, "s", lambda: s), "min"))
    _l_(87939)
    aux = ['background-color: red' if _n_(87940, "v", lambda: v) else '' for v in _n_(87941, "is_max", lambda: is_max)]
    _l_(87942)
    return aux
_c_(87945, _n_(87944, "print", lambda: print), '\nHighlight the minimum value in each column:')
_l_(87946)
_c_(87953, _a_(87949, _a_(87948, _n_(87947, "df", lambda: df), "style"), "apply"), _n_(87950, "highlight_min", lambda: highlight_min), subset=_a_(87952, _n_(87951, "pd", lambda: pd), "IndexSlice")[:, ['B', 'C', 'D', 'E']])
_l_(87954)