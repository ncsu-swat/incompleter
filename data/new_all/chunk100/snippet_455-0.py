# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(117008)

except ImportError:
    pass
_c_(117010, _n_(117009, "print", lambda: print), 'Original DataFrame:')
_l_(117011)
_c_(117014, _n_(117012, "print", lambda: print), _n_(117013, "df", lambda: df))
_l_(117015)
_c_(117017, _n_(117016, "print", lambda: print), 'Count unique values:')
_l_(117018)
_c_(117025, _n_(117019, "print", lambda: print), _c_(117024, _a_(117023, _c_(117022, _a_(117021, _n_(117020, "df", lambda: df), "groupby"), 'value')['id'], "nunique")))
_l_(117026)