# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(97276)

except ImportError:
    pass
time_stamp = _c_(97280, _a_(97278, _n_(97277, "pd", lambda: pd), "to_datetime"), _n_(97279, "epoch_t", lambda: epoch_t), unit='s')
_l_(97281)
_c_(97283, _n_(97282, "print", lambda: print), 'Regular time stamp in UTC:')
_l_(97284)
_c_(97287, _n_(97285, "print", lambda: print), _n_(97286, "time_stamp", lambda: time_stamp))
_l_(97288)
_c_(97290, _n_(97289, "print", lambda: print), '\nConvert the said timestamp in to US/Pacific:')
_l_(97291)
_c_(97298, _n_(97292, "print", lambda: print), _c_(97297, _a_(97296, _c_(97295, _a_(97294, _n_(97293, "time_stamp", lambda: time_stamp), "tz_localize"), 'UTC'), "tz_convert"), 'US/Pacific'))
_l_(97299)
_c_(97301, _n_(97300, "print", lambda: print), '\nConvert the said timestamp in to Europe/Berlin:')
_l_(97302)
_c_(97309, _n_(97303, "print", lambda: print), _c_(97308, _a_(97307, _c_(97306, _a_(97305, _n_(97304, "time_stamp", lambda: time_stamp), "tz_localize"), 'UTC'), "tz_convert"), 'Europe/Berlin'))
_l_(97310)