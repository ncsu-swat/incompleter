# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112616)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112618)

except ImportError:
    pass
_c_(112622, _a_(112621, _a_(112620, _n_(112619, "np", lambda: np), "random"), "seed"), 24)
_l_(112623)
df = _c_(112636, _a_(112625, _n_(112624, "pd", lambda: pd), "concat"), [_n_(112626, "df", lambda: df), _c_(112635, _a_(112628, _n_(112627, "pd", lambda: pd), "DataFrame"), _c_(112632, _a_(112631, _a_(112630, _n_(112629, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(112634, _n_(112633, "list", lambda: list), 'BCDE'))], axis=1)
_l_(112637)
_a_(112639, _n_(112638, "df", lambda: df), "iloc")[0, 2] = _a_(112641, _n_(112640, "np", lambda: np), "nan")
_l_(112642)
_a_(112644, _n_(112643, "df", lambda: df), "iloc")[3, 3] = _a_(112646, _n_(112645, "np", lambda: np), "nan")
_l_(112647)
_a_(112649, _n_(112648, "df", lambda: df), "iloc")[4, 1] = _a_(112651, _n_(112650, "np", lambda: np), "nan")
_l_(112652)
_a_(112654, _n_(112653, "df", lambda: df), "iloc")[9, 4] = _a_(112656, _n_(112655, "np", lambda: np), "nan")
_l_(112657)
_c_(112659, _n_(112658, "print", lambda: print), 'Original array:')
_l_(112660)
_c_(112663, _n_(112661, "print", lambda: print), _n_(112662, "df", lambda: df))
_l_(112664)
_c_(112666, _n_(112665, "print", lambda: print), '\nDataframe - table style:')
_l_(112667)
th_props = [('font-size', '12px'), ('text-align', 'center'), ('font-weight', 'bold'), ('color', '#6d6d6d'), ('background-color', '#f7ffff')]
_l_(112668)
td_props = [('font-size', '12px')]
_l_(112669)
styles = [_c_(112672, _n_(112670, "dict", lambda: dict), selector='th', props=_n_(112671, "th_props", lambda: th_props)), _c_(112675, _n_(112673, "dict", lambda: dict), selector='td', props=_n_(112674, "td_props", lambda: td_props))]
_l_(112676)
_c_(112681, _a_(112679, _a_(112678, _n_(112677, "df", lambda: df), "style"), "set_table_styles"), _n_(112680, "styles", lambda: styles))
_l_(112682)