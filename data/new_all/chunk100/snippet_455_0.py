# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48625)

except ImportError:
    pass
_c_(48627, _n_(48626, "print", lambda: print), 'Original DataFrame:')
_l_(48628)
_c_(48631, _n_(48629, "print", lambda: print), _n_(48630, "df", lambda: df))
_l_(48632)
_c_(48634, _n_(48633, "print", lambda: print), 'Count unique values:')
_l_(48635)
_c_(48642, _n_(48636, "print", lambda: print), _c_(48641, _a_(48640, _c_(48639, _a_(48638, _n_(48637, "df", lambda: df), "groupby"), 'value')['id'], "nunique")))
_l_(48643)