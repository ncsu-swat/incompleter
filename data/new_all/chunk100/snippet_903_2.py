# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(88494)

except ImportError:
    pass
_c_(88496, _n_(88495, "print", lambda: print), 'Subtract two timestamps of same time zone:')
_l_(88497)
date1 = _c_(88500, _a_(88499, _n_(88498, "pd", lambda: pd), "Timestamp"), '2019-03-01 12:00', tz='US/Eastern')
_l_(88501)
_c_(88505, _n_(88502, "print", lambda: print), 'Difference: ', _n_(88503, "date2", lambda: date2) - _n_(88504, "date1", lambda: date1))
_l_(88506)
_c_(88508, _n_(88507, "print", lambda: print), '\nSubtract two timestamps of different time zone:')
_l_(88509)
date1 = _c_(88512, _a_(88511, _n_(88510, "pd", lambda: pd), "Timestamp"), '2019-03-01 12:00', tz='US/Eastern')
_l_(88513)
date2 = _c_(88516, _a_(88515, _n_(88514, "pd", lambda: pd), "Timestamp"), '2019-03-01 07:00', tz='US/Pacific')
_l_(88517)
_c_(88525, _n_(88518, "print", lambda: print), 'Difference: ', _c_(88521, _a_(88520, _n_(88519, "date1", lambda: date1), "tz_localize"), None) - _c_(88524, _a_(88523, _n_(88522, "date2", lambda: date2), "tz_localize"), None))
_l_(88526)