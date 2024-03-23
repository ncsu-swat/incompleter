# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(36588)

except ImportError:
    pass
try:
    import numpy as np
    _l_(36590)

except ImportError:
    pass
_c_(36594, _a_(36593, _a_(36592, _n_(36591, "np", lambda: np), "random"), "seed"), 24)
_l_(36595)
df = _c_(36601, _a_(36597, _n_(36596, "pd", lambda: pd), "DataFrame"), {'A': _c_(36600, _a_(36599, _n_(36598, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(36602)
df = _c_(36615, _a_(36604, _n_(36603, "pd", lambda: pd), "concat"), [_n_(36605, "df", lambda: df), _c_(36614, _a_(36607, _n_(36606, "pd", lambda: pd), "DataFrame"), _c_(36611, _a_(36610, _a_(36609, _n_(36608, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(36613, _n_(36612, "list", lambda: list), 'BCDE'))], axis=1)
_l_(36616)
_a_(36618, _n_(36617, "df", lambda: df), "iloc")[0, 2] = _a_(36620, _n_(36619, "np", lambda: np), "nan")
_l_(36621)
_a_(36623, _n_(36622, "df", lambda: df), "iloc")[3, 3] = _a_(36625, _n_(36624, "np", lambda: np), "nan")
_l_(36626)
_a_(36628, _n_(36627, "df", lambda: df), "iloc")[4, 1] = _a_(36630, _n_(36629, "np", lambda: np), "nan")
_l_(36631)
_a_(36633, _n_(36632, "df", lambda: df), "iloc")[9, 4] = _a_(36635, _n_(36634, "np", lambda: np), "nan")
_l_(36636)
_c_(36638, _n_(36637, "print", lambda: print), 'Original array:')
_l_(36639)
_c_(36642, _n_(36640, "print", lambda: print), _n_(36641, "df", lambda: df))
_l_(36643)
_c_(36645, _n_(36644, "print", lambda: print), '\nDataframe - table style:')
_l_(36646)
th_props = [('font-size', '12px'), ('text-align', 'center'), ('font-weight', 'bold'), ('color', '#6d6d6d'), ('background-color', '#f7ffff')]
_l_(36647)
td_props = [('font-size', '12px')]
_l_(36648)
_c_(36653, _a_(36651, _a_(36650, _n_(36649, "df", lambda: df), "style"), "set_table_styles"), _n_(36652, "styles", lambda: styles))
_l_(36654)