# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(36656)

except ImportError:
    pass
try:
    import numpy as np
    _l_(36658)

except ImportError:
    pass
_c_(36662, _a_(36661, _a_(36660, _n_(36659, "np", lambda: np), "random"), "seed"), 24)
_l_(36663)
df = _c_(36669, _a_(36665, _n_(36664, "pd", lambda: pd), "DataFrame"), {'A': _c_(36668, _a_(36667, _n_(36666, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(36670)
df = _c_(36683, _a_(36672, _n_(36671, "pd", lambda: pd), "concat"), [_n_(36673, "df", lambda: df), _c_(36682, _a_(36675, _n_(36674, "pd", lambda: pd), "DataFrame"), _c_(36679, _a_(36678, _a_(36677, _n_(36676, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(36681, _n_(36680, "list", lambda: list), 'BCDE'))], axis=1)
_l_(36684)
_a_(36686, _n_(36685, "df", lambda: df), "iloc")[0, 2] = _a_(36688, _n_(36687, "np", lambda: np), "nan")
_l_(36689)
_a_(36691, _n_(36690, "df", lambda: df), "iloc")[3, 3] = _a_(36693, _n_(36692, "np", lambda: np), "nan")
_l_(36694)
_a_(36696, _n_(36695, "df", lambda: df), "iloc")[4, 1] = _a_(36698, _n_(36697, "np", lambda: np), "nan")
_l_(36699)
_a_(36701, _n_(36700, "df", lambda: df), "iloc")[9, 4] = _a_(36703, _n_(36702, "np", lambda: np), "nan")
_l_(36704)
_c_(36706, _n_(36705, "print", lambda: print), 'Original array:')
_l_(36707)
_c_(36710, _n_(36708, "print", lambda: print), _n_(36709, "df", lambda: df))
_l_(36711)
_c_(36713, _n_(36712, "print", lambda: print), '\nDataframe - table style:')
_l_(36714)
th_props = [('font-size', '12px'), ('text-align', 'center'), ('font-weight', 'bold'), ('color', '#6d6d6d'), ('background-color', '#f7ffff')]
_l_(36715)
styles = [_c_(36718, _n_(36716, "dict", lambda: dict), selector='th', props=_n_(36717, "th_props", lambda: th_props)), _c_(36721, _n_(36719, "dict", lambda: dict), selector='td', props=_n_(36720, "td_props", lambda: td_props))]
_l_(36722)
_c_(36727, _a_(36725, _a_(36724, _n_(36723, "df", lambda: df), "style"), "set_table_styles"), _n_(36726, "styles", lambda: styles))
_l_(36728)