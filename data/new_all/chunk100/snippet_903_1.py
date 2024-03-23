# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(88460)

except ImportError:
    pass
_c_(88462, _n_(88461, "print", lambda: print), 'Subtract two timestamps of same time zone:')
_l_(88463)
date2 = _c_(88466, _a_(88465, _n_(88464, "pd", lambda: pd), "Timestamp"), '2019-04-01 07:00', tz='US/Eastern')
_l_(88467)
_c_(88471, _n_(88468, "print", lambda: print), 'Difference: ', _n_(88469, "date2", lambda: date2) - _n_(88470, "date1", lambda: date1))
_l_(88472)
_c_(88474, _n_(88473, "print", lambda: print), '\nSubtract two timestamps of different time zone:')
_l_(88475)
date1 = _c_(88478, _a_(88477, _n_(88476, "pd", lambda: pd), "Timestamp"), '2019-03-01 12:00', tz='US/Eastern')
_l_(88479)
date2 = _c_(88482, _a_(88481, _n_(88480, "pd", lambda: pd), "Timestamp"), '2019-03-01 07:00', tz='US/Pacific')
_l_(88483)
_c_(88491, _n_(88484, "print", lambda: print), 'Difference: ', _c_(88487, _a_(88486, _n_(88485, "date1", lambda: date1), "tz_localize"), None) - _c_(88490, _a_(88489, _n_(88488, "date2", lambda: date2), "tz_localize"), None))
_l_(88492)