# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75811)

except ImportError:
    pass
try:
    import datetime
    _l_(75813)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(75815)

except ImportError:
    pass
today = _c_(75817, _n_(75816, "datetime", lambda: datetime), 2012, 10, 30)
_l_(75818)
_c_(75821, _n_(75819, "print", lambda: print), 'Current date:', _n_(75820, "today", lambda: today))
_l_(75822)
tomorrow = _n_(75823, "today", lambda: today) + _c_(75826, _a_(75825, _n_(75824, "pd", lambda: pd), "Timedelta"), days=1)
_l_(75827)
_c_(75830, _n_(75828, "print", lambda: print), 'Tomorrow:', _n_(75829, "tomorrow", lambda: tomorrow))
_l_(75831)
yesterday = _n_(75832, "today", lambda: today) - _c_(75835, _a_(75834, _n_(75833, "pd", lambda: pd), "Timedelta"), days=1)
_l_(75836)
_c_(75839, _n_(75837, "print", lambda: print), 'Yesterday:', _n_(75838, "yesterday", lambda: yesterday))
_l_(75840)
date2 = _c_(75842, _n_(75841, "datetime", lambda: datetime), 2016, 7, 19)
_l_(75843)
_c_(75847, _n_(75844, "print", lambda: print), '\nDifference between two dates: ', _n_(75845, "date1", lambda: date1) - _n_(75846, "date2", lambda: date2))
_l_(75848)