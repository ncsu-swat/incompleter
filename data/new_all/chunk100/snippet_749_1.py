# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75696)

except ImportError:
    pass
try:
    import datetime
    _l_(75698)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(75700)

except ImportError:
    pass
_c_(75703, _n_(75701, "print", lambda: print), 'Current date:', _n_(75702, "today", lambda: today))
_l_(75704)
tomorrow = _n_(75705, "today", lambda: today) + _c_(75708, _a_(75707, _n_(75706, "pd", lambda: pd), "Timedelta"), days=1)
_l_(75709)
_c_(75712, _n_(75710, "print", lambda: print), 'Tomorrow:', _n_(75711, "tomorrow", lambda: tomorrow))
_l_(75713)
yesterday = _n_(75714, "today", lambda: today) - _c_(75717, _a_(75716, _n_(75715, "pd", lambda: pd), "Timedelta"), days=1)
_l_(75718)
_c_(75721, _n_(75719, "print", lambda: print), 'Yesterday:', _n_(75720, "yesterday", lambda: yesterday))
_l_(75722)
date1 = _c_(75724, _n_(75723, "datetime", lambda: datetime), 2016, 8, 2)
_l_(75725)
date2 = _c_(75727, _n_(75726, "datetime", lambda: datetime), 2016, 7, 19)
_l_(75728)
_c_(75732, _n_(75729, "print", lambda: print), '\nDifference between two dates: ', _n_(75730, "date1", lambda: date1) - _n_(75731, "date2", lambda: date2))
_l_(75733)