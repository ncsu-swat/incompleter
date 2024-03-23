# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85585)

except ImportError:
    pass
_c_(85587, _n_(85586, "print", lambda: print), 'Convert integer or float epoch times to Timestamp and DatetimeIndex upto second:')
_l_(85588)
_c_(85591, _n_(85589, "print", lambda: print), _n_(85590, "dates1", lambda: dates1))
_l_(85592)
_c_(85594, _n_(85593, "print", lambda: print), '\nConvert integer or float epoch times to Timestamp and DatetimeIndex upto milisecond:')
_l_(85595)
dates2 = _c_(85598, _a_(85597, _n_(85596, "pd", lambda: pd), "to_datetime"), [1249720105100, 1249720105200, 1249720105300, 1249720105400, 1249720105500], unit='ms')
_l_(85599)
_c_(85602, _n_(85600, "print", lambda: print), _n_(85601, "dates2", lambda: dates2))
_l_(85603)