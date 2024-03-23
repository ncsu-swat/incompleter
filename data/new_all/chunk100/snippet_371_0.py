# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(36459)

except ImportError:
    pass
try:
    import numpy as np
    _l_(36461)

except ImportError:
    pass
_c_(36465, _a_(36464, _a_(36463, _n_(36462, "np", lambda: np), "random"), "seed"), 24)
_l_(36466)
df = _c_(36479, _a_(36468, _n_(36467, "pd", lambda: pd), "concat"), [_n_(36469, "df", lambda: df), _c_(36478, _a_(36471, _n_(36470, "pd", lambda: pd), "DataFrame"), _c_(36475, _a_(36474, _a_(36473, _n_(36472, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(36477, _n_(36476, "list", lambda: list), 'BCDE'))], axis=1)
_l_(36480)
_a_(36482, _n_(36481, "df", lambda: df), "iloc")[0, 2] = _a_(36484, _n_(36483, "np", lambda: np), "nan")
_l_(36485)
_a_(36487, _n_(36486, "df", lambda: df), "iloc")[3, 3] = _a_(36489, _n_(36488, "np", lambda: np), "nan")
_l_(36490)
_a_(36492, _n_(36491, "df", lambda: df), "iloc")[4, 1] = _a_(36494, _n_(36493, "np", lambda: np), "nan")
_l_(36495)
_a_(36497, _n_(36496, "df", lambda: df), "iloc")[9, 4] = _a_(36499, _n_(36498, "np", lambda: np), "nan")
_l_(36500)
_c_(36502, _n_(36501, "print", lambda: print), 'Original array:')
_l_(36503)
_c_(36506, _n_(36504, "print", lambda: print), _n_(36505, "df", lambda: df))
_l_(36507)
_c_(36509, _n_(36508, "print", lambda: print), '\nDataframe - table style:')
_l_(36510)
th_props = [('font-size', '12px'), ('text-align', 'center'), ('font-weight', 'bold'), ('color', '#6d6d6d'), ('background-color', '#f7ffff')]
_l_(36511)
td_props = [('font-size', '12px')]
_l_(36512)
styles = [_c_(36515, _n_(36513, "dict", lambda: dict), selector='th', props=_n_(36514, "th_props", lambda: th_props)), _c_(36518, _n_(36516, "dict", lambda: dict), selector='td', props=_n_(36517, "td_props", lambda: td_props))]
_l_(36519)
_c_(36524, _a_(36522, _a_(36521, _n_(36520, "df", lambda: df), "style"), "set_table_styles"), _n_(36523, "styles", lambda: styles))
_l_(36525)