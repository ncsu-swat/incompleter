# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48935)

except ImportError:
    pass
_c_(48937, _n_(48936, "print", lambda: print), 'Time series with frequency 3h10min:')
_l_(48938)
_c_(48941, _n_(48939, "print", lambda: print), _n_(48940, "dateset1", lambda: dateset1))
_l_(48942)
dateset2 = _c_(48945, _a_(48944, _n_(48943, "pd", lambda: pd), "date_range"), '2029-01-01 00:00:00', periods=20, freq='1D10min20U')
_l_(48946)
_c_(48948, _n_(48947, "print", lambda: print), '\nTime series with frequency 1 day 10 minutes and 20 microseconds:')
_l_(48949)
_c_(48952, _n_(48950, "print", lambda: print), _n_(48951, "dateset2", lambda: dateset2))
_l_(48953)