# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75659)

except ImportError:
    pass
try:
    import datetime
    _l_(75661)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(75663)

except ImportError:
    pass
today = _c_(75665, _n_(75664, "datetime", lambda: datetime), 2012, 10, 30)
_l_(75666)
_c_(75669, _n_(75667, "print", lambda: print), 'Current date:', _n_(75668, "today", lambda: today))
_l_(75670)
_c_(75673, _n_(75671, "print", lambda: print), 'Tomorrow:', _n_(75672, "tomorrow", lambda: tomorrow))
_l_(75674)
yesterday = _n_(75675, "today", lambda: today) - _c_(75678, _a_(75677, _n_(75676, "pd", lambda: pd), "Timedelta"), days=1)
_l_(75679)
_c_(75682, _n_(75680, "print", lambda: print), 'Yesterday:', _n_(75681, "yesterday", lambda: yesterday))
_l_(75683)
date1 = _c_(75685, _n_(75684, "datetime", lambda: datetime), 2016, 8, 2)
_l_(75686)
date2 = _c_(75688, _n_(75687, "datetime", lambda: datetime), 2016, 7, 19)
_l_(75689)
_c_(75693, _n_(75690, "print", lambda: print), '\nDifference between two dates: ', _n_(75691, "date1", lambda: date1) - _n_(75692, "date2", lambda: date2))
_l_(75694)