# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(36730)

except ImportError:
    pass
try:
    import numpy as np
    _l_(36732)

except ImportError:
    pass
_c_(36736, _a_(36735, _a_(36734, _n_(36733, "np", lambda: np), "random"), "seed"), 24)
_l_(36737)
df = _c_(36743, _a_(36739, _n_(36738, "pd", lambda: pd), "DataFrame"), {'A': _c_(36742, _a_(36741, _n_(36740, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(36744)
df = _c_(36757, _a_(36746, _n_(36745, "pd", lambda: pd), "concat"), [_n_(36747, "df", lambda: df), _c_(36756, _a_(36749, _n_(36748, "pd", lambda: pd), "DataFrame"), _c_(36753, _a_(36752, _a_(36751, _n_(36750, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(36755, _n_(36754, "list", lambda: list), 'BCDE'))], axis=1)
_l_(36758)
_a_(36760, _n_(36759, "df", lambda: df), "iloc")[0, 2] = _a_(36762, _n_(36761, "np", lambda: np), "nan")
_l_(36763)
_a_(36765, _n_(36764, "df", lambda: df), "iloc")[3, 3] = _a_(36767, _n_(36766, "np", lambda: np), "nan")
_l_(36768)
_a_(36770, _n_(36769, "df", lambda: df), "iloc")[4, 1] = _a_(36772, _n_(36771, "np", lambda: np), "nan")
_l_(36773)
_a_(36775, _n_(36774, "df", lambda: df), "iloc")[9, 4] = _a_(36777, _n_(36776, "np", lambda: np), "nan")
_l_(36778)
_c_(36780, _n_(36779, "print", lambda: print), 'Original array:')
_l_(36781)
_c_(36784, _n_(36782, "print", lambda: print), _n_(36783, "df", lambda: df))
_l_(36785)
_c_(36787, _n_(36786, "print", lambda: print), '\nDataframe - table style:')
_l_(36788)
td_props = [('font-size', '12px')]
_l_(36789)
styles = [_c_(36792, _n_(36790, "dict", lambda: dict), selector='th', props=_n_(36791, "th_props", lambda: th_props)), _c_(36795, _n_(36793, "dict", lambda: dict), selector='td', props=_n_(36794, "td_props", lambda: td_props))]
_l_(36796)
_c_(36801, _a_(36799, _a_(36798, _n_(36797, "df", lambda: df), "style"), "set_table_styles"), _n_(36800, "styles", lambda: styles))
_l_(36802)