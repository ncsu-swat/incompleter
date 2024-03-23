# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85605)

except ImportError:
    pass
dates1 = _c_(85608, _a_(85607, _n_(85606, "pd", lambda: pd), "to_datetime"), [1329806505, 129806505, 1249892905, 1249979305, 1250065705], unit='s')
_l_(85609)
_c_(85611, _n_(85610, "print", lambda: print), 'Convert integer or float epoch times to Timestamp and DatetimeIndex upto second:')
_l_(85612)
_c_(85615, _n_(85613, "print", lambda: print), _n_(85614, "dates1", lambda: dates1))
_l_(85616)
_c_(85618, _n_(85617, "print", lambda: print), '\nConvert integer or float epoch times to Timestamp and DatetimeIndex upto milisecond:')
_l_(85619)
_c_(85622, _n_(85620, "print", lambda: print), _n_(85621, "dates2", lambda: dates2))
_l_(85623)