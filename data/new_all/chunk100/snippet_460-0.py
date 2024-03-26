# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(117218)

except ImportError:
    pass
dateset1 = _c_(117221, _a_(117220, _n_(117219, "pd", lambda: pd), "date_range"), '2029-01-01 00:00:00', periods=20, freq='3h10min')
_l_(117222)
_c_(117224, _n_(117223, "print", lambda: print), 'Time series with frequency 3h10min:')
_l_(117225)
_c_(117228, _n_(117226, "print", lambda: print), _n_(117227, "dateset1", lambda: dateset1))
_l_(117229)
_c_(117231, _n_(117230, "print", lambda: print), '\nTime series with frequency 1 day 10 minutes and 20 microseconds:')
_l_(117232)
_c_(117235, _n_(117233, "print", lambda: print), _n_(117234, "dateset2", lambda: dateset2))
_l_(117236)