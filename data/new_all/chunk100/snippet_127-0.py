# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(101599)

except ImportError:
    pass
try:
    import numpy as np
    _l_(101601)

except ImportError:
    pass
_c_(101605, _a_(101604, _a_(101603, _n_(101602, "np", lambda: np), "random"), "seed"), 24)
_l_(101606)
df = _c_(101619, _a_(101608, _n_(101607, "pd", lambda: pd), "concat"), [_n_(101609, "df", lambda: df), _c_(101618, _a_(101611, _n_(101610, "pd", lambda: pd), "DataFrame"), _c_(101615, _a_(101614, _a_(101613, _n_(101612, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(101617, _n_(101616, "list", lambda: list), 'BCDE'))], axis=1)
_l_(101620)
_a_(101622, _n_(101621, "df", lambda: df), "iloc")[0, 2] = _a_(101624, _n_(101623, "np", lambda: np), "nan")
_l_(101625)
_a_(101627, _n_(101626, "df", lambda: df), "iloc")[3, 3] = _a_(101629, _n_(101628, "np", lambda: np), "nan")
_l_(101630)
_a_(101632, _n_(101631, "df", lambda: df), "iloc")[4, 1] = _a_(101634, _n_(101633, "np", lambda: np), "nan")
_l_(101635)
_a_(101637, _n_(101636, "df", lambda: df), "iloc")[9, 4] = _a_(101639, _n_(101638, "np", lambda: np), "nan")
_l_(101640)
_c_(101642, _n_(101641, "print", lambda: print), 'Original array:')
_l_(101643)
_c_(101646, _n_(101644, "print", lambda: print), _n_(101645, "df", lambda: df))
_l_(101647)
_c_(101649, _n_(101648, "print", lambda: print), '\nBar charts in dataframe:')
_l_(101650)
_c_(101654, _a_(101653, _a_(101652, _n_(101651, "df", lambda: df), "style"), "bar"), subset=['B', 'C'], color='#d65f5f')
_l_(101655)