# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(110882)

except ImportError:
    pass
_c_(110884, _n_(110883, "print", lambda: print), 'Original DataFrame with single index:')
_l_(110885)
_c_(110888, _n_(110886, "print", lambda: print), _n_(110887, "df", lambda: df))
_l_(110889)
_c_(110891, _n_(110890, "print", lambda: print), '\nDataFrame without index:')
_l_(110892)
_c_(110897, _n_(110893, "print", lambda: print), _c_(110896, _a_(110895, _n_(110894, "df", lambda: df), "to_string"), index=False))
_l_(110898)