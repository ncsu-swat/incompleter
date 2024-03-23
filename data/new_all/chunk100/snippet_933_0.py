# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94372)

except ImportError:
    pass
df = _c_(94376, _a_(94374, _n_(94373, "pd", lambda: pd), "DataFrame"), _n_(94375, "s", lambda: s), columns=['Date'])
_l_(94377)
_c_(94379, _n_(94378, "print", lambda: print), 'last working days of each month of a specific year:')
_l_(94380)
_c_(94383, _n_(94381, "print", lambda: print), _n_(94382, "df", lambda: df))
_l_(94384)