# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(36527)

except ImportError:
    pass
try:
    import numpy as np
    _l_(36529)

except ImportError:
    pass
_c_(36533, _a_(36532, _a_(36531, _n_(36530, "np", lambda: np), "random"), "seed"), 24)
_l_(36534)
df = _c_(36540, _a_(36536, _n_(36535, "pd", lambda: pd), "DataFrame"), {'A': _c_(36539, _a_(36538, _n_(36537, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(36541)
_a_(36543, _n_(36542, "df", lambda: df), "iloc")[0, 2] = _a_(36545, _n_(36544, "np", lambda: np), "nan")
_l_(36546)
_a_(36548, _n_(36547, "df", lambda: df), "iloc")[3, 3] = _a_(36550, _n_(36549, "np", lambda: np), "nan")
_l_(36551)
_a_(36553, _n_(36552, "df", lambda: df), "iloc")[4, 1] = _a_(36555, _n_(36554, "np", lambda: np), "nan")
_l_(36556)
_a_(36558, _n_(36557, "df", lambda: df), "iloc")[9, 4] = _a_(36560, _n_(36559, "np", lambda: np), "nan")
_l_(36561)
_c_(36563, _n_(36562, "print", lambda: print), 'Original array:')
_l_(36564)
_c_(36567, _n_(36565, "print", lambda: print), _n_(36566, "df", lambda: df))
_l_(36568)
_c_(36570, _n_(36569, "print", lambda: print), '\nDataframe - table style:')
_l_(36571)
th_props = [('font-size', '12px'), ('text-align', 'center'), ('font-weight', 'bold'), ('color', '#6d6d6d'), ('background-color', '#f7ffff')]
_l_(36572)
td_props = [('font-size', '12px')]
_l_(36573)
styles = [_c_(36576, _n_(36574, "dict", lambda: dict), selector='th', props=_n_(36575, "th_props", lambda: th_props)), _c_(36579, _n_(36577, "dict", lambda: dict), selector='td', props=_n_(36578, "td_props", lambda: td_props))]
_l_(36580)
_c_(36585, _a_(36583, _a_(36582, _n_(36581, "df", lambda: df), "style"), "set_table_styles"), _n_(36584, "styles", lambda: styles))
_l_(36586)