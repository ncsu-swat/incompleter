# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112684)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112686)

except ImportError:
    pass
_c_(112690, _a_(112689, _a_(112688, _n_(112687, "np", lambda: np), "random"), "seed"), 24)
_l_(112691)
df = _c_(112697, _a_(112693, _n_(112692, "pd", lambda: pd), "DataFrame"), {'A': _c_(112696, _a_(112695, _n_(112694, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(112698)
df = _c_(112711, _a_(112700, _n_(112699, "pd", lambda: pd), "concat"), [_n_(112701, "df", lambda: df), _c_(112710, _a_(112703, _n_(112702, "pd", lambda: pd), "DataFrame"), _c_(112707, _a_(112706, _a_(112705, _n_(112704, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(112709, _n_(112708, "list", lambda: list), 'BCDE'))], axis=1)
_l_(112712)
_a_(112714, _n_(112713, "df", lambda: df), "iloc")[0, 2] = _a_(112716, _n_(112715, "np", lambda: np), "nan")
_l_(112717)
_a_(112719, _n_(112718, "df", lambda: df), "iloc")[3, 3] = _a_(112721, _n_(112720, "np", lambda: np), "nan")
_l_(112722)
_a_(112724, _n_(112723, "df", lambda: df), "iloc")[4, 1] = _a_(112726, _n_(112725, "np", lambda: np), "nan")
_l_(112727)
_a_(112729, _n_(112728, "df", lambda: df), "iloc")[9, 4] = _a_(112731, _n_(112730, "np", lambda: np), "nan")
_l_(112732)
_c_(112734, _n_(112733, "print", lambda: print), 'Original array:')
_l_(112735)
_c_(112738, _n_(112736, "print", lambda: print), _n_(112737, "df", lambda: df))
_l_(112739)
_c_(112741, _n_(112740, "print", lambda: print), '\nDataframe - table style:')
_l_(112742)
th_props = [('font-size', '12px'), ('text-align', 'center'), ('font-weight', 'bold'), ('color', '#6d6d6d'), ('background-color', '#f7ffff')]
_l_(112743)
td_props = [('font-size', '12px')]
_l_(112744)
_c_(112749, _a_(112747, _a_(112746, _n_(112745, "df", lambda: df), "style"), "set_table_styles"), _n_(112748, "styles", lambda: styles))
_l_(112750)