# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(79342)

except ImportError:
    pass
try:
    import numpy as np
    _l_(79344)

except ImportError:
    pass
_c_(79347, _a_(79346, _n_(79345, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(79348)
_c_(79350, _n_(79349, "print", lambda: print), 'Original Orders DataFrame:')
_l_(79351)
_c_(79354, _n_(79352, "print", lambda: print), _n_(79353, "df", lambda: df))
_l_(79355)
_c_(79357, _n_(79356, "print", lambda: print), '\nMissing values in purch_amt column:')
_l_(79358)
result = _a_(79362, _c_(79361, _a_(79360, _n_(79359, "df", lambda: df)['purch_amt'], "value_counts"), dropna=False), "loc")[_a_(79364, _n_(79363, "np", lambda: np), "nan")]
_l_(79365)
_c_(79368, _n_(79366, "print", lambda: print), _n_(79367, "result", lambda: result))
_l_(79369)