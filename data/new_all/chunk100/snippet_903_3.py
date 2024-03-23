# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(88528)

except ImportError:
    pass
_c_(88530, _n_(88529, "print", lambda: print), 'Subtract two timestamps of same time zone:')
_l_(88531)
date1 = _c_(88534, _a_(88533, _n_(88532, "pd", lambda: pd), "Timestamp"), '2019-03-01 12:00', tz='US/Eastern')
_l_(88535)
date2 = _c_(88538, _a_(88537, _n_(88536, "pd", lambda: pd), "Timestamp"), '2019-04-01 07:00', tz='US/Eastern')
_l_(88539)
_c_(88543, _n_(88540, "print", lambda: print), 'Difference: ', _n_(88541, "date2", lambda: date2) - _n_(88542, "date1", lambda: date1))
_l_(88544)
_c_(88546, _n_(88545, "print", lambda: print), '\nSubtract two timestamps of different time zone:')
_l_(88547)
date1 = _c_(88550, _a_(88549, _n_(88548, "pd", lambda: pd), "Timestamp"), '2019-03-01 12:00', tz='US/Eastern')
_l_(88551)
_c_(88559, _n_(88552, "print", lambda: print), 'Difference: ', _c_(88555, _a_(88554, _n_(88553, "date1", lambda: date1), "tz_localize"), None) - _c_(88558, _a_(88557, _n_(88556, "date2", lambda: date2), "tz_localize"), None))
_l_(88560)