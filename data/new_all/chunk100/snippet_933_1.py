# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94386)

except ImportError:
    pass
s = _c_(94389, _a_(94388, _n_(94387, "pd", lambda: pd), "date_range"), '2021-01-01', periods=12, freq='BM')
_l_(94390)
_c_(94392, _n_(94391, "print", lambda: print), 'last working days of each month of a specific year:')
_l_(94393)
_c_(94396, _n_(94394, "print", lambda: print), _n_(94395, "df", lambda: df))
_l_(94397)