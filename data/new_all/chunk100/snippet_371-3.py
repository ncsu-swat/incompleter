# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112826)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112828)

except ImportError:
    pass
_c_(112832, _a_(112831, _a_(112830, _n_(112829, "np", lambda: np), "random"), "seed"), 24)
_l_(112833)
df = _c_(112839, _a_(112835, _n_(112834, "pd", lambda: pd), "DataFrame"), {'A': _c_(112838, _a_(112837, _n_(112836, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(112840)
df = _c_(112853, _a_(112842, _n_(112841, "pd", lambda: pd), "concat"), [_n_(112843, "df", lambda: df), _c_(112852, _a_(112845, _n_(112844, "pd", lambda: pd), "DataFrame"), _c_(112849, _a_(112848, _a_(112847, _n_(112846, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(112851, _n_(112850, "list", lambda: list), 'BCDE'))], axis=1)
_l_(112854)
_a_(112856, _n_(112855, "df", lambda: df), "iloc")[0, 2] = _a_(112858, _n_(112857, "np", lambda: np), "nan")
_l_(112859)
_a_(112861, _n_(112860, "df", lambda: df), "iloc")[3, 3] = _a_(112863, _n_(112862, "np", lambda: np), "nan")
_l_(112864)
_a_(112866, _n_(112865, "df", lambda: df), "iloc")[4, 1] = _a_(112868, _n_(112867, "np", lambda: np), "nan")
_l_(112869)
_a_(112871, _n_(112870, "df", lambda: df), "iloc")[9, 4] = _a_(112873, _n_(112872, "np", lambda: np), "nan")
_l_(112874)
_c_(112876, _n_(112875, "print", lambda: print), 'Original array:')
_l_(112877)
_c_(112880, _n_(112878, "print", lambda: print), _n_(112879, "df", lambda: df))
_l_(112881)
_c_(112883, _n_(112882, "print", lambda: print), '\nDataframe - table style:')
_l_(112884)
th_props = [('font-size', '12px'), ('text-align', 'center'), ('font-weight', 'bold'), ('color', '#6d6d6d'), ('background-color', '#f7ffff')]
_l_(112885)
styles = [_c_(112888, _n_(112886, "dict", lambda: dict), selector='th', props=_n_(112887, "th_props", lambda: th_props)), _c_(112891, _n_(112889, "dict", lambda: dict), selector='td', props=_n_(112890, "td_props", lambda: td_props))]
_l_(112892)
_c_(112897, _a_(112895, _a_(112894, _n_(112893, "df", lambda: df), "style"), "set_table_styles"), _n_(112896, "styles", lambda: styles))
_l_(112898)