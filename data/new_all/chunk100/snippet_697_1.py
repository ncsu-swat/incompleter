# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(71822)

except ImportError:
    pass
_c_(71824, _n_(71823, "print", lambda: print), 'Original DataFrame:')
_l_(71825)
_c_(71828, _n_(71826, "print", lambda: print), _n_(71827, "df", lambda: df))
_l_(71829)
_c_(71831, _n_(71830, "print", lambda: print), '\nReplace A with c:')
_l_(71832)
df = _c_(71835, _a_(71834, _n_(71833, "df", lambda: df), "replace"), ['A', 'D'], ['X', 'Y'])
_l_(71836)
_c_(71839, _n_(71837, "print", lambda: print), _n_(71838, "df", lambda: df))
_l_(71840)