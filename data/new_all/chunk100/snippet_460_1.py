# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48955)

except ImportError:
    pass
dateset1 = _c_(48958, _a_(48957, _n_(48956, "pd", lambda: pd), "date_range"), '2029-01-01 00:00:00', periods=20, freq='3h10min')
_l_(48959)
_c_(48961, _n_(48960, "print", lambda: print), 'Time series with frequency 3h10min:')
_l_(48962)
_c_(48965, _n_(48963, "print", lambda: print), _n_(48964, "dateset1", lambda: dateset1))
_l_(48966)
_c_(48968, _n_(48967, "print", lambda: print), '\nTime series with frequency 1 day 10 minutes and 20 microseconds:')
_l_(48969)
_c_(48972, _n_(48970, "print", lambda: print), _n_(48971, "dateset2", lambda: dateset2))
_l_(48973)