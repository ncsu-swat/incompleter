# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(88426)

except ImportError:
    pass
_c_(88428, _n_(88427, "print", lambda: print), 'Subtract two timestamps of same time zone:')
_l_(88429)
date1 = _c_(88432, _a_(88431, _n_(88430, "pd", lambda: pd), "Timestamp"), '2019-03-01 12:00', tz='US/Eastern')
_l_(88433)
date2 = _c_(88436, _a_(88435, _n_(88434, "pd", lambda: pd), "Timestamp"), '2019-04-01 07:00', tz='US/Eastern')
_l_(88437)
_c_(88441, _n_(88438, "print", lambda: print), 'Difference: ', _n_(88439, "date2", lambda: date2) - _n_(88440, "date1", lambda: date1))
_l_(88442)
_c_(88444, _n_(88443, "print", lambda: print), '\nSubtract two timestamps of different time zone:')
_l_(88445)
date2 = _c_(88448, _a_(88447, _n_(88446, "pd", lambda: pd), "Timestamp"), '2019-03-01 07:00', tz='US/Pacific')
_l_(88449)
_c_(88457, _n_(88450, "print", lambda: print), 'Difference: ', _c_(88453, _a_(88452, _n_(88451, "date1", lambda: date1), "tz_localize"), None) - _c_(88456, _a_(88455, _n_(88454, "date2", lambda: date2), "tz_localize"), None))
_l_(88458)