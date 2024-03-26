# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112752)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112754)

except ImportError:
    pass
_c_(112758, _a_(112757, _a_(112756, _n_(112755, "np", lambda: np), "random"), "seed"), 24)
_l_(112759)
df = _c_(112765, _a_(112761, _n_(112760, "pd", lambda: pd), "DataFrame"), {'A': _c_(112764, _a_(112763, _n_(112762, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(112766)
df = _c_(112779, _a_(112768, _n_(112767, "pd", lambda: pd), "concat"), [_n_(112769, "df", lambda: df), _c_(112778, _a_(112771, _n_(112770, "pd", lambda: pd), "DataFrame"), _c_(112775, _a_(112774, _a_(112773, _n_(112772, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(112777, _n_(112776, "list", lambda: list), 'BCDE'))], axis=1)
_l_(112780)
_a_(112782, _n_(112781, "df", lambda: df), "iloc")[0, 2] = _a_(112784, _n_(112783, "np", lambda: np), "nan")
_l_(112785)
_a_(112787, _n_(112786, "df", lambda: df), "iloc")[3, 3] = _a_(112789, _n_(112788, "np", lambda: np), "nan")
_l_(112790)
_a_(112792, _n_(112791, "df", lambda: df), "iloc")[4, 1] = _a_(112794, _n_(112793, "np", lambda: np), "nan")
_l_(112795)
_a_(112797, _n_(112796, "df", lambda: df), "iloc")[9, 4] = _a_(112799, _n_(112798, "np", lambda: np), "nan")
_l_(112800)
_c_(112802, _n_(112801, "print", lambda: print), 'Original array:')
_l_(112803)
_c_(112806, _n_(112804, "print", lambda: print), _n_(112805, "df", lambda: df))
_l_(112807)
_c_(112809, _n_(112808, "print", lambda: print), '\nDataframe - table style:')
_l_(112810)
td_props = [('font-size', '12px')]
_l_(112811)
styles = [_c_(112814, _n_(112812, "dict", lambda: dict), selector='th', props=_n_(112813, "th_props", lambda: th_props)), _c_(112817, _n_(112815, "dict", lambda: dict), selector='td', props=_n_(112816, "td_props", lambda: td_props))]
_l_(112818)
_c_(112823, _a_(112821, _a_(112820, _n_(112819, "df", lambda: df), "style"), "set_table_styles"), _n_(112822, "styles", lambda: styles))
_l_(112824)