# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(117238)

except ImportError:
    pass
_c_(117240, _n_(117239, "print", lambda: print), 'Time series with frequency 3h10min:')
_l_(117241)
_c_(117244, _n_(117242, "print", lambda: print), _n_(117243, "dateset1", lambda: dateset1))
_l_(117245)
dateset2 = _c_(117248, _a_(117247, _n_(117246, "pd", lambda: pd), "date_range"), '2029-01-01 00:00:00', periods=20, freq='1D10min20U')
_l_(117249)
_c_(117251, _n_(117250, "print", lambda: print), '\nTime series with frequency 1 day 10 minutes and 20 microseconds:')
_l_(117252)
_c_(117255, _n_(117253, "print", lambda: print), _n_(117254, "dateset2", lambda: dateset2))
_l_(117256)