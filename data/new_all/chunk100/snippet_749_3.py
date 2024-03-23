# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75772)

except ImportError:
    pass
try:
    import datetime
    _l_(75774)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(75776)

except ImportError:
    pass
today = _c_(75778, _n_(75777, "datetime", lambda: datetime), 2012, 10, 30)
_l_(75779)
_c_(75782, _n_(75780, "print", lambda: print), 'Current date:', _n_(75781, "today", lambda: today))
_l_(75783)
tomorrow = _n_(75784, "today", lambda: today) + _c_(75787, _a_(75786, _n_(75785, "pd", lambda: pd), "Timedelta"), days=1)
_l_(75788)
_c_(75791, _n_(75789, "print", lambda: print), 'Tomorrow:', _n_(75790, "tomorrow", lambda: tomorrow))
_l_(75792)
yesterday = _n_(75793, "today", lambda: today) - _c_(75796, _a_(75795, _n_(75794, "pd", lambda: pd), "Timedelta"), days=1)
_l_(75797)
_c_(75800, _n_(75798, "print", lambda: print), 'Yesterday:', _n_(75799, "yesterday", lambda: yesterday))
_l_(75801)
date1 = _c_(75803, _n_(75802, "datetime", lambda: datetime), 2016, 8, 2)
_l_(75804)
_c_(75808, _n_(75805, "print", lambda: print), '\nDifference between two dates: ', _n_(75806, "date1", lambda: date1) - _n_(75807, "date2", lambda: date2))
_l_(75809)